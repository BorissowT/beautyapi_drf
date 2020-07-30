from django.shortcuts import render
from api.models import ProductSets, Recipient, Order
from rest_framework.generics import ListAPIView
from api.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class BeautyBoxesList(ListAPIView):

    def get(self, request, *args, **kwargs):
        products_queryset = ProductSets.objects.all()
        if request.query_params:
            min_price = request.query_params.get('min_price')
            min_weight = request.query_params.get('min_weight')
            if min_price and not min_weight:
                result = ProductSets.objects.filter(price__gt=min_price)
                serializer_class = ProductSetsSerializer(result, many=True)
                return Response(serializer_class.data)
            if min_weight and not min_price:
                result = ProductSets.objects.filter(weight__gt=min_weight)
                serializer_class = ProductSetsSerializer(result, many=True)
                return Response(serializer_class.data)
            if min_weight and min_price:
                result = ProductSets.objects.filter(price__gt=min_price, weight__gt=min_weight)
                serializer_class = ProductSetsSerializer(result, many=True)
                return Response(serializer_class.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if products_queryset:
            serializer_class = ProductSetsSerializer(products_queryset, many=True)
            return Response(serializer_class.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

