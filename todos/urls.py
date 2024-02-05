from django.urls import path
from . import views


app_name = 'todos'
urlpatterns = [
    path('add_todo/', views.AddTodoView.as_view(), name='add_todo'),
]