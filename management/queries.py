import graphene

from management.models import User
from management.types import UserType, TeacherType


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType, username=graphene.String())
    users = graphene.List(UserType)

    def resolve_user(self, info, username, **kwargs):
        return User.objects.get(username=username)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class TeacherQuery(graphene.ObjectType):
    teacher = graphene.Field(TeacherType, username=graphene.String())
    teachers = graphene.List(TeacherType)

    def resolve_teacher(self, info, username, **kwargs):
        return User.objects.exclude(teachersubject=None).get(username=username)

    def resolve_teachers(self, info, **kwargs):
        return User.objects.exclude(teachersubject=None)
