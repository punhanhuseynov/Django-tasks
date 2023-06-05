from django import forms
from app.models import *
from ckeditor.widgets import CKEditorWidget

class ReviewForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorWidget(),strip=False)
    class Meta:
        model=Reviews
        fields="__all__"
