import graphene
from questions.types import QuestionType, LevelType
from questions.models import Question, Level
from management.models import User
from management.decorators import login_required

class CreateQuestion(graphene.Mutation):
    question = graphene.Field(QuestionType)

    class Arguments:
        description = graphene.String()
        objective = graphene.String()
        comment = graphene.String()
        answer = graphene.String()
        level_index = graphene.Int()

    @login_required
    def mutate(self, info, description, objective, comment, answer, level_index):
        user = info.context.user
        level = Level.objects.filter(index=level_index).first()
        question = Question(description=description,
                            objective=objective,
                            comment=comment,
                            answer=answer,
                            level=level,
                            created_by=user.id)
        question.save()

        return CreateQuestion(question=question)

class QuestionMutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()


class CreateLevel(graphene.Mutation):
    level = graphene.Field(LevelType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        index = graphene.Int()

    def mutate(self, info, index, name, description):
        level = Level(index=index, name=name, description=description)
        level.save()

        return CreateLevel(level=level)

class LevelMutation(graphene.ObjectType):
    create_level = CreateLevel.Field()
