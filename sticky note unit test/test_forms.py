from django.test import TestCase
from notes.forms import NoteForm

class NoteFormTest(TestCase):
    def test_valid_form(self):
        form = NoteForm(data={'title': 'Test', 'content': 'Valid content'})
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        form = NoteForm(data={'title': '', 'content': ''})
        self.assertFalse(form.is_valid())
