import graphene
from graphene_django import DjangoObjectType

from management.models import User

from subjects.types import SubjectType
from subjects.resolvers import resolve_subjects


class UserType(DjangoObjectType):

    is_teacher = graphene.Boolean(source='is_teacher')

    class Meta:
        model = User


class TeacherType(DjangoObjectType):

    subjects = graphene.List(SubjectType)

    class Meta:
        model = User

    def resolve_subjects(self, info, **kwargs):
        subjects = [s.subject for s in self.teachersubject_set.all()]
        return resolve_subjects(subjects)
