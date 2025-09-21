from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('getOrder', views.getOrders, name="getOrder"),
    path('acceptOrder', views.acceptOrder, name="acceptOrder"),
    path('deleteOrder', views.deleteOrder, name="deleteOrder")
]
