from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView ,UpdateView

from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'anything_you_want'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post_edit.html'




