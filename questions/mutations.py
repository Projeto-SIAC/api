import graphene
from questions.types import QuestionType, DifficultyType
from questions.models import Question, Difficulty
from management.models import User

class CreateQuestion(graphene.Mutation):
    question = graphene.Field(QuestionType)

    class Arguments:
        description = graphene.String()
        objective = graphene.String()
        comment = graphene.String()
        answer = graphene.String()
        difficulty_id = graphene.String()

    def mutate(self, info, description, objective, comment, answer, difficulty_id):
        user = info.context.user

        if not user.id:
            raise Exception('Not logged!')

        difficulty = Difficulty.objects.filter(id=difficulty_id).first()

        question = Question(description=description,
                            objective=objective,
                            comment=comment,
                            answer=answer,
                            difficulty=difficulty,
                            created_by=user.id)
        question.save()

        return CreateQuestion(question=question)

class CreateDifficulty(graphene.Mutation):
    difficulty = graphene.Field(DifficultyType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, description):
        difficulty = Difficulty(name=name, description=description)
        difficulty.save()

        return CreateDifficulty(difficulty=difficulty)

class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    create_difficulty = CreateDifficulty.Field()
