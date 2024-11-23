from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    a function-based view that retrieves all notes 
    from the database and renders them in a template
    """
    try:
        # Debug: Check if notes are being retrieved correctly
        notes = Note.objects.all()
        print(notes) 
        return render(request, 'notes/note_list.html', {'notes': notes})
    except Exception as e:
        # Print the error message for debugging
        print(f"Error: {e}") 
        return render(request, 'error.html', {'message': 'An error occurred!'})


def note_create(request):
    """
    a function-based view that creates a new note
    """
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """
    a function-based view that updates an existing note
    """
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """
    a function-based view that deletes an existing note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})