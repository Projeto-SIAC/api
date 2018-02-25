import graphene
from graphene_django import DjangoObjectType

from subjects.models import Subject, Topic
from subjects.types import SubjectType

from management.decorators import teacher_required


class CreateSubject(graphene.Mutation):
    subject = graphene.Field(SubjectType)

    class Arguments:
        name = graphene.String()
        short_name = graphene.String()
        description = graphene.String()

    @teacher_required
    def mutate(self, info, name, short_name, description):
        subject = Subject(name=name,
                          short_name=short_name,
                          description=description)
        subject.save()
        return CreateSubject(subject=subject)


class SubjectMutation(graphene.ObjectType):
    create_subject = CreateSubject.Field()
