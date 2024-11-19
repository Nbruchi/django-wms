from django.urls import path
from . import views

app_name = 'recycle-logs'

urlpatterns = [
    path('new/', views.log_recycle, name='log-recycle'),
    path('view-logs/', views.view_recycle_logs, name='view-logs'),
]