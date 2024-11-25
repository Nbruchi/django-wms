import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from recycle_logs.models import RecyclingLog
from reports.forms import ReportForm
from django.core.paginator import Paginator
from schedule.models import Schedule

@csrf_exempt
def generate_report(request):
    try:
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.user = request.user
                report.generated_on = timezone.now()
                report.data = json.dumps(generate_report_data(report.report_type, request.user))
                report.save()

                return HttpResponseRedirect(reverse("view_reports")+ f"?report={report.report_type}")
        else:
            form = ReportForm()
    except Exception as e:
        messages.error(request, f"Error occurred: {str(e)}")
        form = ReportForm()

    return render(request, 'generate-report.html', {'form': form})

def generate_report_data(report_type, user):
    if report_type == 'collection':
        schedules = Schedule.objects.filter(user=user)
        return [{'week_day': s.week_day, 'day_time': s.day_time.strftime('%Y-%m-%d %H:%M:%S'), 'frequency': s.frequency} for s in schedules]
    elif report_type == 'recycling':
        logs = RecyclingLog.objects.filter(user=user)
        return [{'type': l.recyclable_type, 'quantity': l.quantity, 'date': l.date.strftime('%Y-%m-%d %H:%M:%S')} for l in logs]
    else:
        raise ValueError("Invalid report type provided.")

def view_reports(request):
    # Get the report type from the form or default to 'recycling'
    report_type = request.GET.get('report_type', 'recycling')

    # Based on report_type, fetch data
    if report_type == 'collection':
        report_data = Schedule.objects.filter(user=request.user)
    else:
        report_data = RecyclingLog.objects.filter(user=request.user).values('recyclable_type', 'quantity', 'date')

    # Paginate the data (adjust number of items per page as needed)
    paginator = Paginator(report_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template and pass the report type and paginated data
    return render(request, 'view-reports.html', {'page_obj': page_obj, 'report_type': report_type})