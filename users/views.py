from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,"register.html",{'form':form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

 # You may want to keep this for testing, but consider CSRF protection in production
def check_user_exists(request):
    if request.method == "GET":
        username = request.GET.get('username', '')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def list_users(request):
    users = User.objects.all().values('id', 'username','email')  # Adjust fields as necessary
    return JsonResponse(list(users), safe=False)