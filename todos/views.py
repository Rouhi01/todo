from django.shortcuts import render, redirect
from django import views
from .models import Task


class AddTodoView(views.View):
    def post(self, request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('todos_page')

