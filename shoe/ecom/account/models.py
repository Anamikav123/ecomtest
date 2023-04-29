from django.db import models
from django.contrib.auth.models import AbstractUser

class CustUser(AbstractUser):
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    options=(
        ("Seller","Seller"),
        ("Custumer","Custumer")
    )
    usertype=models.CharField(max_length=100,choices=options,default="Custumer")
    # device=models.CharField(max_length=200,null=True,blank=True)