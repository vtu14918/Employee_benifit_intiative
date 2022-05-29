from django.contrib import admin
from .models import upload
from import_export.admin import ImportExportModelAdmin

admin.site.register(upload)
# Register your models here.
