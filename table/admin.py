from django.contrib import admin
from .models import FilePath, Columns


# Register your models here.


@admin.register(FilePath)
class FilePathAdmin(admin.ModelAdmin):
    pass


@admin.register(Columns)
class ColumnsAdmin(admin.ModelAdmin):
    pass
