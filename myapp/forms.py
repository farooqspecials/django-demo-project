from django import forms
from .models import Book  # Import the model from the current app

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model the form is based on
        fields = ['title', 'publication_date', 'author']  # Fields to include in the form
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
