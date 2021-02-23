from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from todo.models import (
    Category,
    ToDo,
    Image,
)

# Create your views here.

class TaskListView(ListView):
    model = ToDo
    template_name='index.html'

