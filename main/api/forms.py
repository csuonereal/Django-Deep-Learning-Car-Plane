from django import forms
from .models import DL_MODEL

class DL_FORM(forms.ModelForm):
    class Meta:
        model=DL_MODEL
        fields=['dl_image']