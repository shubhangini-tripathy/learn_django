from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView ,DetailView

from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'


...
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'anything_you_want'

