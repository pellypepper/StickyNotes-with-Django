from django.urls import path
from . import views


urlpatterns = [
    path('', views.note_list, name='note_list'),  # List all notes
    path('create/', views.note_create, name='note_create'),  # Create a new note
    path('<int:pk>/update/', views.note_update, name='note_update'),  # Update a specific note
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),  # Delete a specific note
]
