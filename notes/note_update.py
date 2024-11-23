from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note


def note_update(request, pk):
    """
    update a note
    """
    note = get_object_or_404(Note, pk=pk)

    # Pre-fill the form with the existing note data
    form = NoteForm(request.POST or None, instance=note) 
    if form.is_valid():
        form.save()

         # Redirect to the list after update
        return redirect('note_list') 
    return render(request, 'notes/note_form.html', {'form': form})