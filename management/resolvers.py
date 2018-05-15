from management.models import User


def resolve_user(pk):
    return User.objects.get(pk=pk)


def resolve_users(pks):
    return User.objects.filter(pk__in=pks)
