from django.db.models import CASCADE, DateField, Model
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Lista(Model):
    titulo = CharField(max_length=30)
    descripcion = CharField(max_length=200)
    usuario = ForeignKey(User, on_delete=CASCADE)
    created_at = DateField(auto_now=True, editable=False)


class TodoItem(Model):
    titulo = CharField(max_length=30)
    descripcion = CharField(max_length=200)
    lista = ForeignKey(Lista, on_delete=CASCADE)
    created_at = DateField(auto_now=True, editable=False)
