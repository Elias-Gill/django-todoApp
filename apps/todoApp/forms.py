from django.forms import ModelForm

from apps.todoApp.models import Lista, TodoItem


class AddListForm(ModelForm):
    class Meta:
        model = Lista
        fields = ["titulo", "descripcion"]


class AddTodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ["titulo", "descripcion"]
