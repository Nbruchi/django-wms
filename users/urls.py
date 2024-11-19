from . import views
from django.urls import path

app_name = 'users'

urlpatterns =[
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('check/', views.check_user_exists, name='check_user_exists'),
    path('list/', views.list_users, name='list-users'),
]