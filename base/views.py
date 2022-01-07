from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tasks


class TaskList(ListView):
    model = Tasks
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
