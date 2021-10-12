from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("faq", views.faq, name="faq"),
    path("shipping_info", views.shipping_info, name="shipping_info"),
]
