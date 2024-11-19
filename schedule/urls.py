from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('new/', views.create_schedule, name='create-schedule'),
    path('all/', views.view_schedules, name='view-schedules'),
]