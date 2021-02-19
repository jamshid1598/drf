from django.urls import path
from .views import (
    TaskListView,
    
)

app_name = 'core'

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
]