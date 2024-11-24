from django.test import TestCase
from django.urls import reverse
from notes.models import Note

class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test", content="Test content")
    
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {'title': 'New Note', 'content': 'Note content'})
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Note.objects.filter(title='New Note').exists())
