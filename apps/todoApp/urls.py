from django.urls import path

from apps.todoApp.views import (add_list, add_todo, delete_list,
                                list_todo_items, list_todo_lists, delete_todo)

urlpatterns = [
    # paginas principales
    path("", list_todo_lists),
    path("todos/<int:list_id>", list_todo_items, name="todos_index"),
    # operaciones CRUD separadas
    path("todos/<int:list_id>/add_item", add_todo, name="add_item"),
    path("todos/<int:list_id>/<int:todo_id>/delete_item", delete_todo, name="delete_item"),
    path("add_list", add_list, name="add_list"),
    path("delete_list/<int:lista_id>", delete_list, name="delete_list"),
]
