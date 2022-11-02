from django.contrib import admin
from iatf_db_demo2.processapp.models import Process


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('step_name', 'responsible', 'evidence')
