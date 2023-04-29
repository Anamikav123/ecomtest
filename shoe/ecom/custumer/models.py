from django.db import models
from account.models import CustUser
from seller.models import Product

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
