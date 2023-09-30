from django.contrib import admin

from . import models

# admin.site.register(models.Pessoa)

@admin.register(models.Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display=('nome', 'idade', 'email', 'telefone')
    list_filter=('nome',)
    search_fields = ('cidade','idade')
    list_per_page = 5
    # list_editable = ('cidade', 'idade',)

# Register your models here.
