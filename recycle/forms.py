from django import forms

from .models import Recycle


class RecycleForm(forms.ModelForm):
    class Meta:
        model = Recycle
        fields =['type','quantity']