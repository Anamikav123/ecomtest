from django.urls import path
from .views import *

urlpatterns=[
    path("viewpdt/",ViewProduct.as_view(),name="viewprdt"), 
     path("cart",CartView.as_view(),name="cart"),
    path("addcart/<int:pid>",AddCart.as_view(),name="addcart"),
    path('Remove_cart/<int:ssid>',RemoveCart.as_view(), name='remove'),  
]


