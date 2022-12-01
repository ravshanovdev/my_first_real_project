from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import TeacherForm
from .models import Group, ClassRoom, Attendance, User, Payments, Teacher, Student
from django.db import models


# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     add_form = TeacherForm
#     list_display = ['student', 'data', 'amount', 'amount_type']
#     fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('student', 'data', 'amount', 'amount_type')}),)
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('student', 'data', 'amount', 'amount_type')}),)


# admin.site.register(CustomUserAdmin)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Payments)
admin.site.register(ClassRoom)
admin.site.register(Attendance)
