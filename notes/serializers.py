from rest_framework import serializers
from notes.models import Note
from rest_framework.reverse import reverse


class NoteSerializer(serializers.ModelSerializer):
    # 1. WAJIB DEFINISIKAN INI (Sering Lupa!)
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Note
        # 2. WAJIB TULIS '_links' DI SINI
        # Jangan pakai '__all__', tulis manual satu-satu biar aman
        fields = ['id', 'title', 'body', 'tags', 'createdAt', 'updatedAt', '_links']

    # 3. Logika pembuatan link
    def get__links(self, obj):
        request = self.context.get('request')
        # Jika request tidak ada (lupa context di views), kembalikan null
        if request is None:
            return None

        # Membuat link dinamis ke 'note-detail'
        detail_url = reverse('note-detail', kwargs={'note_id': obj.id}, request=request)

        return [
            {
                "rel": "self",
                "href": detail_url,
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "DELETE",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('note-detail', kwargs={'note_id': obj.id}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,  # Gunakan variabel detail_url yang sudah kita perbaiki tadi
                "action": "PUT",  # <--- INI TAMBAHANNYA
                "types": ["application/json"]
            },

        ]
