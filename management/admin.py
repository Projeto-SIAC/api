from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from management.models import User, TeacherSubject


class SubjectInline(admin.TabularInline):

    model = TeacherSubject
    verbose_name = 'subject'
    verbose_name_plural = 'subjects'


class UserAdmin(BaseUserAdmin):

    inlines = (SubjectInline, )


admin.site.register(User, UserAdmin)
