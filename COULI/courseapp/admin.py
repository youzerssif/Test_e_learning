from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ('photo_profile','user', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('user')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Formateur')
    active.short_description = 'active Formateur'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Formateur')
    desactive.short_description = 'desactive Formateur'
    ordering = ('user',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('user',)
    
    
@admin.register(models.Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('formateur','titre', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('formateur')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Cours')
    active.short_description = 'active Cours'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Cours')
    desactive.short_description = 'desactive Cours'
    ordering = ('formateur','titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('formateur','titre',)
    
    
@admin.register(models.Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ('cours','titre', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('cours')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Chapitre')
    active.short_description = 'active Chapitre'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Chapitre')
    desactive.short_description = 'desactive Chapitre'
    ordering = ('cours','titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('cours','titre',)