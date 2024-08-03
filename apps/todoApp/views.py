from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotAllowed

from apps.todoApp.models import Lista, TodoItem
from apps.todoApp.forms import AddListForm, AddTodoForm

# general views


@login_required
def list_todo_lists(req: HttpRequest):
    return render(
        req,
        "todoApp/index.html",
        {"listas": Lista.objects.filter(usuario=req.user)},
    )


@login_required
def list_todo_items(req: HttpRequest, list_id: int):
    ls = get_object_or_404(Lista, id=list_id)
    return render(
        req,
        "todoApp/index.html",
        {"todos": TodoItem.objects.filter(lista=ls)},
    )


####################
# "component" view #
####################


@login_required
def add_list(req):
    if req.method != "POST":
        return HttpResponseNotAllowed("POST")

    form = AddListForm(req.POST)
    if not form.is_valid():
        return HttpResponseForbidden()

    instance = form.save(commit=False)
    instance.usuario = req.user
    instance.save()

    if req.headers.get("HX-Request"):
        return render(
            req,
            "todoApp/lista/lista.html",
            {"listas": Lista.objects.filter(usuario=req.user)},
        )

    return list_todo_lists(req)


@login_required
def add_todo(req, list_id: int):
    if req.method != "POST":
        return HttpResponseNotAllowed("POST")

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
            "todoApp/todo/lista.html",
            {"todos": TodoItem.objects.filter(usuario=req.user, lista=lista)},
        )

    return list_todo_items(req, list_id)
