from django.db import models

# Create your models here.
    
class Product(models.Model):
    productname=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="product_images",null=True)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
