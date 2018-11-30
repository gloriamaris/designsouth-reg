# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
from django.http import HttpResponse
from django.contrib import admin

# Register your models here.
from .models import User

# Export as csv mixin
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Export Selected'

class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'email', 'school', 'created_at')
    list_filter = ('name', 'email', 'school')
    actions = ['export_as_csv']

admin.site.register(User, UserAdmin)
