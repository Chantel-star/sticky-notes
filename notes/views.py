from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm  

"""Views for displaying and managing sticky notes."""
    
# -----------------------------
# List View
# -----------------------------
class NoteListView(ListView):
    """
    View for displaying a list of notes for current user"""
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    ordering = ['-updated_at']

# -----------------------------
# Detail View
# -----------------------------
class NoteDetailView(DetailView):
    """
    View for displaying the details of a specific note."""
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

# -----------------------------
# Create View
# -----------------------------
class NoteCreateView(CreateView):
    """View for creating a new note."""
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

# -----------------------------
# Update View
# -----------------------------
class NoteUpdateView(UpdateView):
    """View for updating an existing note."""
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

# -----------------------------
# Delete View
# -----------------------------
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')
