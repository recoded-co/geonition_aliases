from django.contrib import admin
from geonition_aliases.models import Alias


class AliasAdmin(admin.ModelAdmin):
    fields = ('shortcut', 'dst')

admin.site.register(Alias, AliasAdmin)
