from django.shortcuts import render
from api.models import ProductSets, Recipient, Order
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from beautyapi.filters import FilterBackend


class BeautyBoxesList(ListAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    filter_backends = [FilterBackend]
    

class BeautyBoxDetail(RetrieveAPIView):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer


class RecipientsList(ListAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientDetail(RetrieveAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
