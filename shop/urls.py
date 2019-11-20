from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("index", views.index, name="shophome"),
    path("signup", views.signup, name="Signup"),
    path("login", views.login, name="Login"),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("contact_login", views.contact_login, name="ContactUsLogin"),
    path("tracker", views.tracker, name="TrackingStatus"),
    path("operator_tracker", views.operator_tracker, name="Operator_tracking"),
    path("search", views.search, name="Search"),
    path("products/<str:myid>", views.productView, name="productview"),
    path("checkout", views.checkout, name="Checkout"),
    path("checkout_login", views.checkout_login, name="Checkout_login"),
    path("vendor_request", views.ven_request, name="VendorRequest"),
    path("request_list", views.request_list, name="RequestsList"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
