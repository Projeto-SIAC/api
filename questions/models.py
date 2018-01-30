import uuid
from django.db import models


class Difficulty(models.Model):

    class Meta:
        verbose_name_plural = 'difficulties'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    objective = models.CharField(max_length=250)
    comment = models.CharField(max_length=250, blank=True, null=True)
    answer = models.CharField(max_length=250, blank=True, null=True)
    difficulty = models.ForeignKey(Difficulty, related_name='questions', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class QuestionTopic(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'topic',)

    def __str__(self):
        return 'QuestionTopic <{}.{}>'.format(self.question.id, self.topic)


class Option(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    comment = models.CharField(max_length=250, blank=True, null=True)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Attachment(models.Model):

    IMAGE = 'IMG'
    TEXT = 'TEXT'
    CODE = 'CODE'

    ATTACHMENT_KIND = (
        (IMAGE, 'Image'),
        (TEXT, 'Text'),
        (CODE, 'Code'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    source = models.CharField(max_length=250, blank=True, null=True)
    question = models.ForeignKey(Question, related_name='attachments', on_delete=models.CASCADE)
    kind = models.CharField(max_length=10, choices=ATTACHMENT_KIND)

    def __str__(self):
        return self.title
