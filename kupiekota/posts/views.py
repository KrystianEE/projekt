from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    fields = ['title', 'post_image', 'description', 'price', 'location']
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ListPostsView(generic.ListView):
    model = models.Post


class PostDetailView(generic.DetailView):
    model = models.Post
