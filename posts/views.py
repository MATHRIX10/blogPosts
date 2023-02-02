from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView
from .models import Post 

class Index(ListView) : 
    model = Post 
    template_name = 'posts/home.html'

class Details(DetailView) : 
    model = Post
    template_name = "posts/details.html"

class NewPost(CreateView) : 
    model = Post 
    template_name = 'posts/new_post.html'
    fields = ['title','author','body']

class EditPost(UpdateView) : 
    model = Post 
    template_name = 'posts/edit_post.html'
    fields = ['title','body']


class DeletePost(DeleteView) : 
    model = Post 
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')