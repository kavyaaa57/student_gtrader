from django.contrib import admin
from .models import Student, Course, Enrollment, Pdftool, Lyra


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_birth')
    search_fields = ('name', 'email')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id', 'course_name', 'course_grade', 'student')
    search_fields = ('name', 'course_id', 'course_name', 'course_grade', 'student__name')


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    search_fields = ('student__name', 'course__name',  'course__course_id', 'course__course_id_name', 'course__course_grade')


class PdftoolAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    search_fields = ('author__username', 'title')



admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Pdftool, PdftoolAdmin)

import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib import admin
from django.contrib.admin.actions import action
from .models import Enrollment




class LyraModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'Name', 'RegNo', 'Department', 'Grade')
    search_fields = ('title', 'Name', 'RegNo', 'Department', 'Grade')
    

admin.site.register(Lyra, LyraModelAdmin)



