from django.shortcuts import render, redirect
from django import views
from todos.models import Task


class TodosPageView(views.View):
    template_name = 'todos_page.html'
    def get(self, request):
        tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
        return render(request, self.template_name, {'tasks':tasks})