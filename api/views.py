import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ProductSets, Recipient, Order
from api.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer, \
    UserSerializer
from beautyapi.filters import BeautyBoxesFilterBackend, OrdersFilterBackend, RecipientsFilterBackend


class BeautyBoxesList(ListAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    filter_backends = [BeautyBoxesFilterBackend]


class BeautyBoxDetail(RetrieveAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer


class RecipientsList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    filter_backends = [RecipientsFilterBackend]

    def post(self, request, *args):
        if Recipient.objects.filter(name=request.user.first_name,
                                    surname=request.user.last_name).first():
            content = {"warning": "a recipient with this name and surname already exists"}
            return HttpResponse(json.dumps(content), status=status.HTTP_304_NOT_MODIFIED)
        else:
            user = request.user
            user.first_name = request.data['name']
            user.last_name = request.data['surname']
            user.save()
            serializer_class = RecipientSerializer(data=request.data)
            if not serializer_class.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class RecipientDetail(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientNameEdit(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def editname(self, request, pk=None):
        recipient = Recipient.objects.filter(id=pk).first()
        order = Order.objects.filter(recipient=recipient).first()
        surname = request.query_params.get("surname")
        name = request.query_params.get("name")
        patronymic = request.query_params.get("patronymic")
        if order.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if not surname and not name and not patronymic:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if surname:
                recipient.surname = surname
                recipient.save()
            if name:
                recipient.name = name
                recipient.save()
            if patronymic:
                recipient.patronymic = patronymic
                recipient.save()
            return Response(status=status.HTTP_202_ACCEPTED)


class OrderAddressEdit(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request, pk):
        order = Order.objects.filter(id=pk).first()
        if not order:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if order.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if request.data.get("delivery_address"):
            order.delivery_address = request.data.get("delivery_address")
            order.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class OrdersList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    filter_backends = [OrdersFilterBackend]
    serializer_class = OrderSerializer

    def post(self, request, *args):
        if not request.user.first_name or not request.user.last_name:
            content = {"warning": "to make an order user has to register a recipient first"}
            return HttpResponse(json.dumps(content), status=status.HTTP_304_NOT_MODIFIED)
        recipient = Recipient.objects.filter(name=request.user.first_name,
                                             surname=request.user.last_name).first()
        if not recipient:
            content = {"warning": "the recipient doesn't found. try to set up a new one"}
            return HttpResponse(json.dumps(content), status=status.HTTP_304_NOT_MODIFIED)
        serializer_class = OrderSerializer(data={
            'delivery_address': request.data['delivery_address'],
            'product_set': request.data['product_set'],
            'user': request.user.pk,
            'recipient': recipient.pk
        })
        if not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)


class OrderDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [OrdersFilterBackend]


class OrderClose(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, format=None):
        order = Order.objects.filter(id=pk).first()
        if order.user != request.user:
            return Response(status.HTTP_403_FORBIDDEN)
        order.status = "CANCELLED"
        order.save()
        return Response(status.HTTP_202_ACCEPTED)


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


