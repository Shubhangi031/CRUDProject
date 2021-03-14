from django import forms
from testapp.models import Library


class SForm(forms.ModelForm):
    class Meta:
        model=Library
        fields="__all__"
    