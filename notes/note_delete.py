from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import NoteForm
from .models import Note


def note_delete(request, pk):
    """
    Delete a note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, "Note deleted successfully.")
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})