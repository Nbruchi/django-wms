from schedule.models import Schedule
from schedule.forms import ScheduleForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login')
def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('schedules:view-schedules')
    else:
        form = ScheduleForm()
    return render(request, 'create-schedule.html', {'form': form})


def view_schedules(request):
    schedules = Schedule.objects.filter(user=request.user)

    # Set up pagination (30 schedules per page)
    paginator = Paginator(schedules, 20)  # Show 30 schedules per page

    # Get the page number from the request query parameters
    page_number = request.GET.get('page')

    # Get the corresponding page of schedules
    page_schedules = paginator.get_page(page_number)

    # Pass the paginated schedules to the template
    return render(request, 'view-schedules.html', {'schedules': page_schedules})
