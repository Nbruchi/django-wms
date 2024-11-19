from django import forms

from .models import RecyclingLog


class RecyclingLogForm(forms.ModelForm):
    class Meta:
        model = RecyclingLog
        fields =['recyclable_type','quantity']