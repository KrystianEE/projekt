from django.urls import path
from . import views

app_name = 'usermsg'

urlpatterns = [
    path('<username>/', views.UserBoxListView.as_view(), name='userboxlist'),
    path('<username>/<int:pk>/', views.detail_box, name='boxdetail'),
    path('new/<post_user>/', views.create_box, name='new_box'),
]
