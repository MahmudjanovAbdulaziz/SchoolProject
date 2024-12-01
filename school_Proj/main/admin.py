from django.contrib import admin, messages
from django.utils.html import format_html

from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = ("text", "date", "image_preview")
    search_fields = ('text',)     
    list_filter = ('date',)       

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.img.url)
        return 'Нет изображения'


class SchoolCherectersCountAdmin(admin.ModelAdmin):
    # def has_add_permissions(self, request):
    #     if School_cherecters_count.objects.exists():
    #         self.message_user(
    #             request,
    #             "[Ошибка 4001] Запись уже существует. Разрешена только одна запись для этой таблицы.",
    #             level=messages.ERROR
    #         )
    #         return False
    #     return super().has_add_permissions(request)

    list_display = ('text','colvo_student', 'colvo_teacher', 'colvo_classes', 'colvo_offices')
    list_display_links = ('text',)  
    list_editable = ("colvo_student","colvo_teacher", "colvo_classes", "colvo_offices")


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'job_title', "image_preview")  
    search_fields = ('name', 'surname', 'job_title')  
    list_filter = ("job_title", "surname", "name")

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.img.url)
        return 'Нет изображения'


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    list_display_links = ('id',) 

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.img.url)
        return 'Нет изображения'


class OurGraduatesAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "image_preview")
    search_fields = ('name', 'surname')

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.img.url)
        return 'Нет изображения'


admin.site.register(Events, EventsAdmin)
admin.site.register(School_cherecters_count, SchoolCherectersCountAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Our_graduates, OurGraduatesAdmin)
