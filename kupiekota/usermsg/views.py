from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cur_user'] = self.request.user
        return context


@login_required
def create_box(request, post_user):
    user = User.objects.get(username=post_user)
    cur_user = request.user
    box = models.MsgBox.objects.get_or_create(user1=cur_user, user2=user)
    return redirect('usermsg:boxdetail', username=cur_user.username, pk=box[0].pk)


@login_required
def detail_box(request, username, pk):
    box = get_object_or_404(models.MsgBox, pk=pk)
    cur_user = request.user
    msg_list = models.Usermsg.objects.filter(box__pk=pk).order_by('send_at')

    if request.method == "POST":
        form = forms.MsgForm(request.POST)
        usr = request.user
        if form.is_valid():
            msg = form.save(commit=False)
            msg.box = box
            msg.sender = usr
            msg.save()
            return redirect('usermsg:boxdetail', username=usr.username, pk=box.pk)
    else:
        form = forms.MsgForm()

    if cur_user != box.user1 and cur_user != box.user2:
        return redirect('home')
    return render(request, 'usermsg/userbox_detail.html', {
                                                            'usr_msg': msg_list,
                                                            'form': form,
                                                            'cur_user': cur_user
                                                            })
