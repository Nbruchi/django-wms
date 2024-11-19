from django import forms

from reports.models import Report


class ReportForm(forms.ModelForm):
    REPORT_CHOICES = [
        ('collection','Collection schedules'),
        ('recycling', 'Recycling activities'),
    ]

    report_type = forms.ChoiceField(choices=REPORT_CHOICES)
    class Meta:
        model = Report
        fields = ['report_type']