from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.ListPostsView.as_view(), name='post_list'),
    path('new/', views.CreatePostView.as_view(), name='new'),
    url(r'by/(?P<username>[-\w]+)/all/', views.UserPostsView.as_view(), name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='single'),
    url(r'delete/(?P<pk>\d+)/$', views.DeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
