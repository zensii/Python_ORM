from django.contrib import admin

from main_app.models import Student, StudentEnrollment, Subject


# Register your models here.
@admin.register(Student)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass