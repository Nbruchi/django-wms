from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['week_day', 'day_time', 'frequency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['week_day'].choices = Schedule.WEEK_DAYS
        self.fields['frequency'].choices = Schedule.FREQUENCIES