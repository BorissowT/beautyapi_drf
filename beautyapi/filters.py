from rest_framework import filters

from api.models import ProductSets, Order


class BeautyBoxesFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')
        result = ProductSets.objects.filter(title='PARAMETERS ERROR')
        if min_weight and not min_price:
            result = ProductSets.objects.filter(weight__gt=min_weight)
        if min_price and not min_weight:
            result = ProductSets.objects.filter(price__gt=min_price)
        if min_weight and min_price:
            result = ProductSets.objects.filter(price__gt=min_price, weight__gt=min_weight)
        return result


class OrdersFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser:
            result = Order.objects.all()
        else:
            result = Order.objects.filter(user=request.user)
        return result
