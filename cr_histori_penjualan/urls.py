from django.urls import path

from . import views

app_name = 'cr_histori_penjualan'

urlpatterns = [
    path('list-histori-penjualan', views.list_histori_penjualan, name='list-histori-penjualan'),
    path('detail/<str:email>/<str:id>', views.detail_penjualan, name='detail-penjualan')
]