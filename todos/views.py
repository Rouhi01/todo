from django.shortcuts import render, redirect, get_object_or_404
from django import views
from .models import Task


class AddTodoView(views.View):
    def post(self, request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('todos_page')

class DoneTodoView(views.View):
    def get(self, request, todo_id):
        task = get_object_or_404(Task, id=todo_id)
        task.is_completed = True
        task.save()
        return redirect('todos_page')

class UnDoneTodoView(views.View):
    def get(self, request, todo_id):
        task = get_object_or_404(Task, id=todo_id)
        task.is_completed = False
        task.save()
        return redirect('todos_page')

class EditTodoView(views.View):
    def get(self, request, todo_id):
        get_task = get_object_or_404(Task, id=todo_id)
        return render(request, 'todos/edit_todo.html', {'get_task':get_task})

    def post(self, request, todo_id):
        get_task = get_object_or_404(Task, id=todo_id)
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('todos_page')

class DeleteTodoView(views.View):
    def get(self, request, todo_id):
        get_task = get_object_or_404(Task, id=todo_id)
        get_task.delete()
        return redirect('todos_page')

