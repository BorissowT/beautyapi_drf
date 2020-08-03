from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from api.models import ProductSets, Recipient, Order


class ProductSetsSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = '__all__'

    def create(self, data):
        return ProductSets.objects.create(**data)


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

    def create(self, data):
        return Recipient.objects.create(**data)


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, data):
        return Order.objects.create(

        )
