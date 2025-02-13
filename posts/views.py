from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)

from .models import Post
from django.urls import reverse


class PostListView(ListView):
    template_name="post/list.html" #object, modelname_list
    model=Post #retrieve all of the modual for us to render the html


class PostDetailView(DetailView):
    template_name="post/detail.html"
    model=Post

class PostCreateView(CreateView):
    template_name="post/new.html"
    model=Post
    success_url =reverse("List")

# Create your views here.

