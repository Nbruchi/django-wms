from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from recycle.forms import RecycleForm
from recycle.models import Recycle

# Create your views here.
@csrf_exempt
def log_recycle(request):
    if request.method == 'POST':
        form = RecycleForm(request.POST)
        if form.is_valid():
            recycling_log = form.save(commit=False)
            recycling_log.user = request.user
            recycling_log.save()
            return redirect('recycle-logs:view-logs')
    else:
        form = RecycleForm()
    return render(request, 'log-recycle.html', {'form': form})

def view_recycle_logs(request):
    logs = Recycle.objects.all().order_by('id')

    # Paginate logs, showing 30 logs per page
    paginator = Paginator(logs, 40)  # Show 30 logs per page
    page_number = request.GET.get('page')  # Get the page number from the query parameters
    page_obj = paginator.get_page(page_number)

    return render(request, 'view-logs.html', {'logs': page_obj})