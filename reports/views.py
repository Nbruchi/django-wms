import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from recycle.models import Recycle
from reports.forms import ReportForm
from django.core.paginator import Paginator
from schedule.models import Schedule

@login_required
@csrf_exempt
def generate_report(request):
    try:
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.generated_on = timezone.now()
                report.user = request.user
                report.data = json.dumps(generate_report_data(report.type))
                report.save()

                return HttpResponseRedirect(reverse("reports:view-reports")+ f"?report={report.type}")
        else:
            form = ReportForm()
    except Exception as e:
        messages.error(request, f"Error occurred: {str(e)}")
        form = ReportForm()

    return render(request, 'generate-report.html', {'form': form})

def generate_report_data(type):
    if type == 'collection':
        schedules = Schedule.objects.all().order_by('id')
        return [{'day': s.day, 'time': s.time.strftime('%Y-%m-%d %H:%M:%S'), 'frequency': s.frequency} for s in schedules]
    elif type == 'recycling':
        logs = Recycle.objects.all().order_by('id')
        return [{'type': l.type, 'quantity': l.quantity, 'date': l.date.strftime('%Y-%m-%d %H:%M:%S')} for l in logs]
    else:
        raise ValueError("Invalid report type provided.")

def view_reports(request):
    # Get the report type from the form or default to 'recycling'
    type = request.GET.get('type', 'recycling')

    # Based on type, fetch data
    if type == 'collection':
        report_data = Schedule.objects.all().order_by('id')
    else:
        report_data = Recycle.objects.all().order_by('id').values('type', 'quantity', 'date')

    # Paginate the data (adjust number of items per page as needed)
    paginator = Paginator(report_data, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template and pass the report type and paginated data
    return render(request, 'view-reports.html', {'page_obj': page_obj, 'type': type})