from rest_framework import filters

from api.models import ProductSets


class FilterBackend(filters.BaseFilterBackend):

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



