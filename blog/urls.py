from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="blogHome"),
    path("blogPost/<int:id>",views.blogPost,name="blogPome"),
]
