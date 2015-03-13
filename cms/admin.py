from django.contrib import admin
from cms.models import Intruder

# Register your models here.
class IntruderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timeStamp',)
    list_display_links = ('id', 'name',)
admin.site.register(Intruder, IntruderAdmin)