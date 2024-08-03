from django.urls import path

from apps.todoApp.views import add_list, add_todo, list_todo_items, list_todo_lists

urlpatterns = [
    # paginas principales
    path("", list_todo_lists),
    path("todos/<int:list_id>", list_todo_items, name="todos_index"),
    # operaciones CRUD separadas
    path("todos/<int:list_id>/add_item", add_todo, name="add_todo"),
    path("add_list", add_list, name="add_list"),
]
