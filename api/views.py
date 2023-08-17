from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.http.response import JsonResponse
from .models import *
from .serializers import *


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = "add.html"
    fields = ['title', 'author', 'body']


    
    
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')

def some(req):
    one_post = Post.objects.all()
    return JsonResponse(one_post)

class BlogView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()