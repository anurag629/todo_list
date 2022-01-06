from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tasks


class TaskList(ListView):
    model = Tasks
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'base/task.html'
