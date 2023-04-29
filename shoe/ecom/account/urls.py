from django.urls import path
from.views import RegView,LogoutView
urlpatterns=[
   path('reg/',RegView.as_view(),name="reg"),
   path('logout/',LogoutView.as_view(),name="logout"),
]