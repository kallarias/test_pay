from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    ProductPageView,
    # product_page,
    CancelView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('item/<int:pk>/', ProductPageView.as_view(), name='item')
    # path('create-checkout-session/<int:pk>/', product_page, name='create-checkout-session')
]
