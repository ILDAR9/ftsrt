# -*- coding: utf-8 -*-
from django.contrib import admin
from administration.models import Club, Coach, Pair, Student, Administration, Tournament, Document

class CoachAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ФИО и аватар', {'fields': ['fio', 'avatar']}),
        ('Контактные данные', {'fields': ['telephone', 'email']}),
        ('Должность', {'fields': ['position']}),
    ]

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Уникальный номер', {'fields': ['stsr_id']}),
        ('Личныые данные', {'fields': ['fio', 'gender', 'datebirth']}),
        ('Танцевальный клуб',{'fields':['club']}),
        ('Разряд', {'fields': ['standart_level', 'latin_level', 'category']}),
    ]
    list_filter = ('gender', 'standart_level', 'latin_level', 'category')
    search_fields = [('fio')]

class ClubAdmin(admin.ModelAdmin):
    filter_horizontal = ('coaches',)
    list_filter = [('city')]

admin.site.register(Student, StudentAdmin)
admin.site.register(Pair)
admin.site.register(Club, ClubAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Administration)
admin.site.register(Tournament)
admin.site.register(Document)