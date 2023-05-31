from django import forms
from . import models


#craete forms

class Comment_form(forms.ModelForm):
  class Meta:
    model=models.Comment
    fields=['body']
    widget={
        'body': forms.TextInput(attrs={'class': 'form-control'}),
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'checkin', 'checkout', 'payment', 'service']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'checkin': forms.DateInput(attrs={'class': 'form-control'}),
            'checkout': forms.DateInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
