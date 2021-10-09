from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from student.models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
