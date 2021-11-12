from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(AlbumPattern)
class AlbumPatternAdmin(ImportExportModelAdmin):
    list_display = ('title', 'theme', 'photo')
    list_filter = ('theme',)
    search_fields = ('title__startswith',)
    pass


def in_progress(modeladmin, request, queryset):
    queryset.update(status='in_progress')


in_progress.short_description = "Изменить статус заказа 'В процессе'"


def completed(modeladmin, request, queryset):
    queryset.update(status='completed')


completed.short_description = "Изменить статус заказа 'Выполнен'"


def canceled(modeladmin, request, queryset):
    queryset.update(status='canceled')


canceled.short_description = "Изменить статус заказа 'Отменен'"


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'albumPattern', 'albumLayout', 'pagesCount', 'date', 'status')
    list_filter = ('albumPattern', 'albumLayout', 'status')
    search_fields = ('name__startswith','email__startswith')
    actions = [in_progress, completed, canceled]
    pass

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'rate', 'date', 'text')
    list_filter = ('rate',)
    search_fields = ('tel__startswith', 'email__startswith', 'name__startswith',)
    pass


admin.site.register(Theme)
admin.site.register(Size)
admin.site.register(AlbumLayout)
admin.site.register(AlbumType)
