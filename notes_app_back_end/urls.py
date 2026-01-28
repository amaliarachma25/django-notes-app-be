from django.contrib import admin
from django.urls import path
from notes.views import NoteList, NoteDetail  # Import Class yang baru

urlpatterns = [
    path('admin/', admin.site.urls),

    # Perhatikan perbedaannya: pakai .as_view()
    path('notes/', NoteList.as_view(), name='note-list'),

    # name='note-detail' ini PENTING untuk serializer tadi
    path('notes/<uuid:note_id>/', NoteDetail.as_view(), name='note-detail'),
]