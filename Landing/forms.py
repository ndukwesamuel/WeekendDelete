from django import forms

from .models import  UserDetails


class USerForms(forms.ModelForm):
    
    class Meta:
        model = UserDetails
        fields = "__all__"
