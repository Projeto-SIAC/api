import graphene
from questions.types import QuestionType, DifficultyType
from questions.models import Question, Difficulty
from management.models import User
from management.decorators import login_required

class CreateQuestion(graphene.Mutation):
    question = graphene.Field(QuestionType)

    class Arguments:
        description = graphene.String()
        objective = graphene.String()
        comment = graphene.String()
        answer = graphene.String()
        difficulty_id = graphene.String()

    @login_required
    def mutate(self, info, description, objective, comment, answer, difficulty_id):
        user = info.context.user
        difficulty = Difficulty.objects.filter(id=difficulty_id).first()
        question = Question(description=description,
                            objective=objective,
                            comment=comment,
                            answer=answer,
                            difficulty=difficulty,
                            created_by=user.id)
        question.save()

        return CreateQuestion(question=question)

class QuestionMutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()


class CreateDifficulty(graphene.Mutation):
    difficulty = graphene.Field(DifficultyType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, description):
        difficulty = Difficulty(name=name, description=description)
        difficulty.save()

        return CreateDifficulty(difficulty=difficulty)

class DifficultyMutation(graphene.ObjectType):
    create_difficulty = CreateDifficulty.Field()
