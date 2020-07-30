
from api.views import BeautyBoxesList
    # BeautyBoxDetail
#Recipients_list, Beautybox_detail, Recipient_detail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('product-sets/', BeautyBoxesList.as_view(), name='beutyboxes_list'),
    path('product-sets/<int:id>/', beautybox_detail, name='beautybox_detail'),
    #
    # path('recipients/', recipients_list, name='recipients_list'),
    # path('recipients/<int:id>/', recipient_detail, name='recipient_detail'),
]
