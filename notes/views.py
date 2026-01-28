from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notes.models import Note
from notes.serializers import NoteSerializer


class NoteList(APIView):
    # 1. Fitur GET (Melihat Semua Catatan)
    def get(self, request):
        notes = Note.objects.all()
        # PENTING: context={'request': request} wajib ada agar _links muncul
        serializer = NoteSerializer(notes, many=True, context={'request': request})

        # Format Response sesuai PDF (Langsung "notes": data)
        return Response({
            "notes": serializer.data
        }, status=status.HTTP_200_OK)

    # 2. Fitur POST (Menambah Catatan)
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PENGGANTI notes_list
class NoteList(APIView):
    # Menangani GET (Lihat Semua)
    def get(self, request):
        notes = Note.objects.all()
        # Perhatikan: context={'request': request} PENTING agar link url bisa dibuat
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response({
            "status": "success",
            "data": {
                "notes": serializer.data
            }
        })

    # Menangani POST (Tambah Baru)
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Catatan berhasil ditambahkan",
                "data": {
                    "noteId": serializer.data['id']
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "status": "fail",
            "message": "Gagal menambahkan catatan",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# PENGGANTI note_detail
class NoteDetail(APIView):
    def get_object(self, note_id):
        try:
            return Note.objects.get(pk=note_id)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, note_id):
        note = self.get_object(note_id)
        serializer = NoteSerializer(note, context={'request': request})
        return Response({
            "status": "success",
            "data": {
                "note": serializer.data
            }
        })

    def put(self, request, note_id):
        note = self.get_object(note_id)
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Catatan berhasil diubah"
            })
        return Response({
            "status": "fail",
            "message": "Gagal mengubah catatan",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):
        note = self.get_object(note_id)
        note.delete()
        return Response({
            "status": "success",
            "message": "Catatan berhasil dihapus"
        })

    def put(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, note_id):  # Perhatikan parameternya note_id
        note = self.get_object(note_id)
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):
        note = self.get_object(note_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)