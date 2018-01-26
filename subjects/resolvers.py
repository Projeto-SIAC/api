from subjects.models import Subject


def resolve_subject(id):
    return Subject.object.get(pk=id)


def resolve_subjects(**kwargs):
    return Subject.objects.filter(**kwargs)
