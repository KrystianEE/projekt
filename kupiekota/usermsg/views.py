from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms
# Create your views here.
User = get_user_model()


class UserBoxListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = models.MsgBox
    template_name = 'usermsg/userbox_list.html'

    def get_queryset(self):
        self.user = self.request.user
        return models.MsgBox.objects.filter(
            Q(user1=self.user) | Q(user2=self.user)
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['usermne'] = self.request.user.username
    #     return context


class UserBoxDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = models.MsgBox
    template_name = 'usermsg/userbox_detail.html'


# @login_required
# def add_comment_to_post(request, pk):
#     box = get_object_or_404(models.MsgBox, pk=pk)
#     if request.method == "POST":
#         form = forms.MsgForm(request.POST)
#         usr = request.user
#         if form.is_valid():
#             msg = form.save(commit=False)
#             msg.msgbox = box
#             msg.sender = usr
#             msg.save()
#             return redirect('post_detail', pk=box.pk)
#     else:
#         form = forms.MsgForm()
#     return render(request, 'usermsg/userbox_detail.html', {'form': form})


class CreateMsgView(LoginRequiredMixin, generic.CreateView):
    fields = ('content')
    model = models.Usermsg
    template_name = 'usermsg/_msg_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        # add box
        self.object.save()
        return super().form_valid(form)
