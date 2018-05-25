from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

# Create your views here.


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    fields = ['title', 'description', 'price', 'post_image']
    model = models.Post


class ListPostsView(generic.ListView):
    model = models.Post


class PostDetailView(generic.DetailView):
    model = models.Post
