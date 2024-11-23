from django.shortcuts import render, redirect
from .forms import NoteForm


def note_create(request):
    """
    Create a new note
    """
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')  # Redirect to the list of notes after creation
    return render(request, 'notes/note_form.html', {'form': form})