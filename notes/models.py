import uuid
from django.db import models


class Note(models.Model):
    # 1. ID Unik (UUID)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 2. Judul Catatan
    title = models.CharField(max_length=200)

    # 3. Isi Catatan
    body = models.TextField()

    # 4. Tags/Label
    tags = models.TextField(default="General")

    # 5. Waktu Dibuat (createdAt)
    createdAt = models.DateTimeField(auto_now_add=True)

    # 6. Waktu Diedit (updatedAt)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title