from django import forms
from CRUDOperation.models import EmpModel


class Empforms(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = "__all__"
