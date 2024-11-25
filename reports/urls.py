from django.urls import path
from . import views

app_name = 'reports'

urlpatterns =[
    path('new/', views.generate_report, name='generate-report'),
    path('all/', views.view_reports, name='view-reports'),
]