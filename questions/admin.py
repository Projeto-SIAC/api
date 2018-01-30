from django.contrib import admin
from questions.models import Difficulty, Question, Option, Attachment


class OptionInline(admin.TabularInline):

    model = Option


class AttachmentInline(admin.StackedInline):

    model = Attachment
    extra = 0


class QuestionAdmin(admin.ModelAdmin):

    inlines = (OptionInline, AttachmentInline, )


admin.site.register(Difficulty)
admin.site.register(Question, QuestionAdmin)
