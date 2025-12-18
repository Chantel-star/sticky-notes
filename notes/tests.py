from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def setUp(self):
        """Create a note for testing."""
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_create_note(self):
        """Test that a note is created successfully."""
        self.assertEqual(Note.objects.count(), 1)

    def test_update_note(self):
        """Test updating a note's title."""
        self.note.title = 'Updated Title'
        self.note.save()
        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Title')

    def test_delete_note(self):
        """Test deleting a note."""
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)
