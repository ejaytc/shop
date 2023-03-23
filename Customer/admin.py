from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['is_active', 'is_terminated']

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.added_by = request.user
            obj.updated_by = request.user
        elif change and obj.id:
            obj.updated_by = request.user
        obj.save()
