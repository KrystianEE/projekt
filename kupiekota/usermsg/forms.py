from django import forms
from . import models


class MsgForm(forms.ModelForm):

    class Meta():
        model = models.Usermsg
        fields = ('content', )
