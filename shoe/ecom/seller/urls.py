from django.urls import path
from.views import *

urlpatterns=[
    path("store/",StoreHome.as_view(),name="storehome"),
    path("addpdt/",AddProduct.as_view(),name="addpdt"),
    path("viewpdt/",ViewProduct.as_view(),name="viewpdt"),
    path("delproduct/<int:ssid>",ProductDeleteView.as_view(),name="delpdt"),
    path("editproduct/<int:sid>",ProductEdit.as_view(),name="editpdt"),
   
]
