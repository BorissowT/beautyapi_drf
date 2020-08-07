from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import BeautyBoxesList, BeautyBoxDetail, \
    RecipientsList, RecipientDetail, OrdersList, OrderDetail, Register, OrderClose, \
    OrderAddressEdit, RecipientNameEdit

router = DefaultRouter()
router.register('recipients', RecipientNameEdit, basename='book')

urlpatterns = [
    path('register', Register.as_view(), name='register'),

    path('product-sets/', BeautyBoxesList.as_view(), name='beutyboxes_list'),
    path('product-sets/<int:pk>/', BeautyBoxDetail.as_view(), name='beautybox_detail'),

    path('recipients', RecipientsList.as_view(), name='recipients_list'),
    path('recipients/<int:pk>/', RecipientDetail.as_view(), name='recipient_detail'),


    path('orders', OrdersList.as_view(), name="orders_list"),
    path('orders/<int:pk>/', OrderDetail.as_view(), name="orders_detail"),
    path('orders/close/<int:pk>', OrderClose.as_view(), name="orders_close"),
    path('orders/edit-address/<int:pk>', OrderAddressEdit.as_view(), name='edit_address'),
]

urlpatterns += router.urls
