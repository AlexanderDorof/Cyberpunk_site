from django import forms

from .models import *


class CyberwareForm(forms.ModelForm):
    class Meta:
        model = Cyberware
        fields = "__all__"
