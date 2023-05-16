from django.contrib import admin
from .models import Result


class ResultAdmin(admin.ModelAdmin):
    list_display = ('proceedings', 'auditable_unit', 'url_auditable_unit', 'name_social_reason', 'category', 'region', 'status', 'detail')

    
admin.site.register(Result, ResultAdmin)