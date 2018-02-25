import graphene

from questions.models import Difficulty, Question
from questions.types import DifficultyType, QuestionType
from management.decorators import login_required

class DifficultyQuery(graphene.ObjectType):

    difficulty = graphene.Field(DifficultyType, id=graphene.UUID())
    difficulties = graphene.List(DifficultyType)

    def resolve_difficulty(self, info, id, **kwargs):
        return Difficulty.objects.get(pk=id)

    def  resolve_difficulties(self, info, **kwargs):
        return Difficulty.objects.all()


class QuestionQuery(graphene.ObjectType):

    question = graphene.Field(QuestionType, id=graphene.UUID())
    questions = graphene.List(QuestionType)
    my_questions = graphene.List(QuestionType)

    def resolve_question(self, info, id, **kwargs):
        return Question.objects.get(pk=id)

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    @login_required
    def resolve_my_questions(self, info, **kwargs):
        user = info.context.user
        questions = Question.objects.filter(created_by=user.id)
        return questions
