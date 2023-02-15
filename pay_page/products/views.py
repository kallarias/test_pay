from django.views import View
from django.views.generic import TemplateView
import stripe
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from .models import Products


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductPageView(TemplateView):
    template_name = "item_info.html"

    def get_context_data(self, *args, **kwargs):
        product = Products.objects.filter(id=self.kwargs['pk'])
        # product = Products.objects.get(name="car")
        context = super(ProductPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,

        })
        return context


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Products.objects.order_by('id')
        # product = Products.objects.get(name="car")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,

        })
        return context


# Create your views here.
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product = get_object_or_404(Products, pk=self.kwargs['pk'])
        # rq = stripe.Product.create(name="T-shirt")
        # rw = stripe.Price.create(product='{{PRODUCT_47}}', unit_amount=2000, currency="usd")
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            # line_items=[
            #     {
            #         # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
            #         'price': 'price_1MbYROK7tAFaffxpXh7o8EVi',
            #         'quantity': 1,
            #     },
            # ],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': product.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)

