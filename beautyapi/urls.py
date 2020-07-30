
from api.views import BeautyBoxesList, BeautyBoxDetail, RecipientsList, RecipientDetail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('product-sets/', BeautyBoxesList.as_view(), name='beutyboxes_list'),
    path('product-sets/<int:pk>/', BeautyBoxDetail.as_view(), name='beautybox_detail'),

    path('recipients/', RecipientsList.as_view(), name='recipients_list'),
    path('recipients/<int:pk>/', RecipientDetail.as_view(), name='recipient_detail'),
]
