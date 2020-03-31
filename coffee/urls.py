from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.index,name=""),
    path("about/",views.about,name="about"),
    path("search/",views.search,name="search"),
    path("contact_us/",views.contact,name="Contact_us"),
    path("track/",views.track,name="track"),
    path("products/<int:myid>",views.product,name="products"),
    path("Login/",views.Login,name="Login"),
    path("Signup/",views.Sign_up,name="Signup"),
    path("checkout/",views.check_out,name="checkout"),
    path("handleRequest/",views.handleRequest,name="handleRequest")
]
