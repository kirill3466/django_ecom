from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

from product.models import Product

from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/partials/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, product_id, action):
    cart = Cart(request)
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
                'slug': product.slug,
            },
            'total_price': (quantity * product.price) / 100,
            'quantity': quantity,
        }
    else:
        item = None
    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    return render(request, 'cart/checkout.html', {'pub_key': pub_key})


class CartMenuView(TemplateView):
    template_name = 'cart/partials/menu_cart.html'


class CartTotalView(TemplateView):
    template_name = 'cart/partials/cart_total.html'


class CartSuccessView(TemplateView):
    template_name = 'cart/success.html'
