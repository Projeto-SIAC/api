import graphene
from graphene_django import DjangoObjectType

from management.models import User

from subjects.schema import SubjectType
from subjects.resolvers import resolve_subjects


class UserType(DjangoObjectType):

    class Meta:
        model = User


class TeacherType(DjangoObjectType):

    subjects = graphene.List(SubjectType)

    class Meta:
        model = User

    def resolve_subjects(self, info, **kwargs):
        subjects = [s.subject for s in self.teachersubject_set.all()]
        return resolve_subjects(pk__in=subjects)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    teachers = graphene.List(TeacherType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_teachers(self, info, **kwargs):
        return User.objects.exclude(teachersubject=None)
