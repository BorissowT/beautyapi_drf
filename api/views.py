from django.shortcuts import render
from api.models import ProductSets, Recipient, Order
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from api.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from beautyapi.filters import BeautyBoxesFilterBackend, OrdersFilterBackend


class BeautyBoxesList(ListAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    filter_backends = [BeautyBoxesFilterBackend]


class BeautyBoxDetail(RetrieveAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer


class RecipientsList(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientDetail(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class OrdersList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    filter_backends = [OrdersFilterBackend]
    serializer_class = OrderSerializer

