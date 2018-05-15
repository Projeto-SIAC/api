import uuid
from django.db import models
from questions.models import Question


class AssessmentTest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)


class Answer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE
    )
    assessment_test = models.ForeignKey(
        AssessmentTest, related_name='answers', on_delete=models.CASCADE
    )
