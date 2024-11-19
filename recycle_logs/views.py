from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from recycle_logs.forms import RecyclingLogForm
from recycle_logs.models import RecyclingLog


# Create your views here.
@csrf_exempt
@login_required(login_url="/users/login/")
def log_recycle(request):
    if request.method == 'POST':
        form = RecyclingLogForm(request.POST)
        if form.is_valid():
            recycling_log = form.save(commit=False)
            recycling_log.user = request.user
            recycling_log.save()
            return redirect('recycle-logs:view-logs')
    else:
        form = RecyclingLogForm()
    return render(request, 'log-recycle.html', {'form': form})

@login_required(login_url="/users/login/")
def view_recycle_logs(request):
    logs = RecyclingLog.objects.filter(user=request.user)

    # Paginate logs, showing 30 logs per page
    paginator = Paginator(logs, 20)  # Show 30 logs per page
    page_number = request.GET.get('page')  # Get the page number from the query parameters
    page_obj = paginator.get_page(page_number)

    return render(request, 'view-logs.html', {'logs': page_obj})