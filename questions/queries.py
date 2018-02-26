import graphene

from questions.models import Level, Question
from questions.types import LevelType, QuestionType
from management.decorators import teacher_required

class LevelQuery(graphene.ObjectType):

    level = graphene.Field(LevelType, id=graphene.UUID())
    levels = graphene.List(LevelType)

    def resolve_level(self, info, id, **kwargs):
        return Level.objects.get(pk=id)

    def  resolve_levels(self, info, **kwargs):
        return Level.objects.all()


class QuestionQuery(graphene.ObjectType):

    question = graphene.Field(QuestionType, id=graphene.UUID())
    questions = graphene.List(QuestionType)

    def resolve_question(self, info, id, **kwargs):
        return Question.objects.get(pk=id)

    @teacher_required
    def resolve_questions(self, info, **kwargs):
        user = info.context.user
        questions = Question.objects.filter(created_by=user.id)
        return questions
