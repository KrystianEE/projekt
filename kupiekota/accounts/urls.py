from django.urls import path
from django.contrib.suth import views as auth_views
from account import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LogInView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogOutView.as_view(), name='logout'),
]
