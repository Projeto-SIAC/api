from subjects.models import Subject, Topic


def resolve_subject(pk):
    return Subject.object.get(pk=pk)


def resolve_subjects(pks):
    return Subject.objects.filter(pk__in=pks)


def resolve_topic(pk):
    return Topic.object.get(pk=pk)


def resolve_topic(pks):
    return Topic.objects.filter(pk__in=pks)
