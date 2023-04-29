from django import forms
from .models import CartItem


class Cartform(forms.ModelForm):
    class Meta:
        model=CartItem
        fields=["quantity"]


        