from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

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


@login_required
def create_box(request, post_user):
    user = User.objects.get(username=post_user)
    box,  = models.MsgBox.objects.get_or_create(user1=request.user, user2=user)
    return redirect('usermsg:boxdetail', username=request.user.username, pk=box.pk)


@login_required
def detail_box(request, username, pk):
    box = get_object_or_404(models.MsgBox, pk=pk)

    if request.user != box.user1 and request.user != box.user2:
        raise PermissionDenied

    msg_list = models.Usermsg.objects.filter(box__pk=pk).order_by('send_at')

    if request.method == "POST":
        form = forms.MsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.box = box
            msg.sender = request.user
            msg.save()
            return redirect('usermsg:boxdetail', username=request.user.username, pk=box.pk)
    else:
        form = forms.MsgForm()

    return render(request, 'usermsg/userbox_detail.html', {
                                                            'usr_msg': msg_list,
                                                            'form': form,
                                                            'cur_user': request.user
                                                            })
