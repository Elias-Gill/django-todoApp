from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render

from apps.todoApp.forms import AddListForm, AddTodoForm
from apps.todoApp.models import Lista, TodoItem

# general views


@login_required
def list_todo_lists(req: HttpRequest):
    return render(
        req,
        "todoApp/index.html",
        {"listas": Lista.objects.filter(usuario=req.user)},
    )


@login_required
def delete_list(req, lista_id):
    instance = Lista.objects.filter(id=lista_id)
    instance.delete()

    if req.headers.get("HX-Request"):
        return render(
            req,
            "todoApp/listar_listas.html",
            {"listas": Lista.objects.filter(usuario=req.user)},
        )

    return list_todo_lists(req)


@login_required
def add_list(req):
    if req.method == "GET":
        return render(
            req,
            "todoApp/form_nueva_lista.html",
        )

    form = AddListForm(req.POST)
    if not form.is_valid():
        return HttpResponseForbidden()

    instance = form.save(commit=False)
    instance.usuario = req.user
    instance.save()

    if req.headers.get("HX-Request"):
        return render(
            req,
            "todoApp/listar_listas.html",
            {"listas": Lista.objects.filter(usuario=req.user)},
        )

    return list_todo_lists(req)


def delete_todo(req, todo_id, list_id):
    instance = TodoItem.objects.filter(id=todo_id)
    instance.delete()

    if req.headers.get("HX-Request"):
        ls = get_object_or_404(Lista, id=list_id)
        return render(
            req,
            "todoApp/listar_todos.html",
            {"list_id": list_id, "todos": TodoItem.objects.filter(lista=ls)},
        )

    return list_todo_lists(req)


@login_required
def list_todo_items(req: HttpRequest, list_id: int):
    ls = get_object_or_404(Lista, id=list_id)
    return render(
        req,
        "todoApp/todos.html",
        {"list_id": list_id, "todos": TodoItem.objects.filter(lista=ls)},
    )


@login_required
def add_todo(req, list_id: int):
    if req.method == "GET":
        return render(
            req,
            "todoApp/form_nuevo_todo.html",
            {"list_id": list_id},
        )

    form = AddTodoForm(req.POST)
    if not form.is_valid():
        return HttpResponseForbidden()

    lista = Lista.objects.get(id=list_id)

    instance = form.save(commit=False)
    instance.lista = lista
    instance.save()

    if req.headers.get("HX-Request"):
        return render(
            req,
            "todoApp/listar_todos.html",
            {
                "list_id": list_id,
                "todos": TodoItem.objects.filter(lista=lista),
            },
        )

    return list_todo_items(req, list_id)
