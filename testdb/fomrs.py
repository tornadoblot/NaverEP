from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    upload = forms.FileField(label='첨부파일', required=False,
    widget=form.FileInput(attrs={'class': 'form'}))

    class Meta:
        model = Docuement
        exclude = ['attached']