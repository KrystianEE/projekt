from django.views.generic import CreateView
from django.urls import reverse_lazy

from accounts import forms
# Create your views here.


class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
