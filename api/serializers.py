from rest_framework.serializers import Serializer, ModelSerializer, HyperlinkedModelSerializer

from api.models import ProductSets, Recipient, Order


class ProductSetsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductSets
        fields = '__all__'

    def create(self, data):
        return ProductSets.objects.create(**data)


class RecipientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

    def create(self, data):
        return Recipient.objects.create(**data)


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
