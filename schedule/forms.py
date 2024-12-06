from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'time', 'frequency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].choices = Schedule.dayS
        self.fields['frequency'].choices = Schedule.FREQUENCIES