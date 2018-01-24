import uuid
from django.db import models


class AssessmentTest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)
    questions = models.ManyToManyField('questions.Question')


class Answer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey('questions.Question', related_name='answers', on_delete=models.CASCADE)
    assessment_test = models.ForeignKey(AssessmentTest, related_name='answers', on_delete=models.CASCADE)
