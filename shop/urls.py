from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="SearchProduct"),
    path("products/<int:myid>", views.products, name="ViewProduct"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handleRequest/",views.handleRequest,name='handleRequest'),
]
