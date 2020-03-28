from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    myPost=Post.objects.all()
    return render(request,'blog/bl.html',{'myPost':myPost})

def blogPost(request,id):
    post=Post.objects.filter(post_id=id)[0]
    return render(request,'blog/blogPost.html',{'post':post})