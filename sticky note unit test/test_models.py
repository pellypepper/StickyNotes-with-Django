from django.test import TestCase
from notes.models import Note

class NoteModelTest(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(title="Test Note", content="This is a test note.")
        self.assertEqual(note.title, "Test Note")
        self.assertTrue(note.created_at)
