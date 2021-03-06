import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    @property
    def is_teacher(self):
        return self.teachersubject_set.count() > 0


class TeacherSubject(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
