from django.shortcuts import render
from django.views.generic import(
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post

class PostListView(ListView):

    template_name = "posts/list.html"

    model = Post

    context_object_name = "posts"
#