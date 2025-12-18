from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form to create or update a Note."""

    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your note here...'}),
        }
