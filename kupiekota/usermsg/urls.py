from django.urls import path
from . import views

app_name = 'usermsg'

urlpatterns = [
    path('<username>/', views.UserBoxListView.as_view(), name='userboxlist'),
    path('<username>/<int:pk>/', views.UserBoxDetailView.as_view(), name='boxdetail'),
]
