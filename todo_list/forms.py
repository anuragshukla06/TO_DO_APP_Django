from django import forms
from .models import List

class ListForms(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]