import graphene

from management.models import User
from management.types import UserType, TeacherType
from management.decorators import login_required


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType, username=graphene.String())
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_user(self, info, username, **kwargs):
        return User.objects.get(username=username)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    @login_required
    def resolve_me(self, info, **kwargs):
        return info.context.user


class TeacherQuery(graphene.ObjectType):
    teacher = graphene.Field(TeacherType, username=graphene.String())
    teachers = graphene.List(TeacherType)

    def resolve_teacher(self, info, username, **kwargs):
        return User.objects.exclude(teachersubject=None).get(username=username)

    def resolve_teachers(self, info, **kwargs):
        return User.objects.exclude(teachersubject=None)
