from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from django.contrib.auth.models import User
from api.models import ProductSets, Recipient, Order


class ProductSetsSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = '__all__'


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
        return Order.objects.create(**data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", 'last_name']

    def create(self, data):
        return User.objects.create_user(**data)
