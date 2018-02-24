from django.contrib import admin
from questions.models import Difficulty, Question, Option, Attachment, QuestionTopic


class TopicInline(admin.TabularInline):

    model = QuestionTopic
    verbose_name = 'topic'
    verbose_name_plural = 'topics'


class OptionInline(admin.TabularInline):

    model = Option


class AttachmentInline(admin.StackedInline):

    model = Attachment
    extra = 0


class QuestionAdmin(admin.ModelAdmin):

    inlines = (TopicInline, OptionInline, AttachmentInline, )


admin.site.register(Difficulty)
admin.site.register(Question, QuestionAdmin)
