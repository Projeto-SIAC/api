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
    user = graphene.Field(UserType, username=graphene.String())
    users = graphene.List(UserType)

    teacher = graphene.Field(TeacherType, username=graphene.String())
    teachers = graphene.List(TeacherType)

    def resolve_user(self, info, username, **kwargs):
        return User.objects.get(username=username)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_teacher(self, info, username, **kwargs):
        return User.objects.exclude(teachersubject=None).get(username=username)

    def resolve_teachers(self, info, **kwargs):
        return User.objects.exclude(teachersubject=None)
