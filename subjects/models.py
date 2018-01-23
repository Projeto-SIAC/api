import uuid
from django.db import models


class Subject(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Topic(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    parent = models.ForeignKey('self', verbose_name='Parent Topic', on_delete=models.PROTECT, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
