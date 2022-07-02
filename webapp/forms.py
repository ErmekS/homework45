from django import forms
from django.forms import widgets

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class SketchpadForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Title')
    description = forms.CharField(max_length=2000, required=True, label='Description', widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES, label="Статус")
    date_of_completion = forms.DateField(required=False, label="Дата выполнения")


