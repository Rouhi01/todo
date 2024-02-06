from django.urls import path
from . import views


app_name = 'todos'
urlpatterns = [
    path('add_todo/', views.AddTodoView.as_view(), name='add_todo'),
    path('done_todo/<int:todo_id>/', views.DoneTodoView.as_view(), name='done_todo'),
    path('undone_todo/<int:todo_id>/', views.UnDoneTodoView.as_view(), name='undone_todo'),
    path('edit_todo/<int:todo_id>/', views.EditTodoView.as_view(), name='edit_todo'),
    path('delete_todo/<int:todo_id>/', views.DeleteTodoView.as_view(), name='delete_todo'),
]