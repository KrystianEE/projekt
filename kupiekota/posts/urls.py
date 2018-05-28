from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ListPostsView.as_view(), name='post_list'),
    path('new/', views.CreatePostView.as_view(), name='new')
]
