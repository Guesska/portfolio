from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AdminAboutMe(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'image')


class AdminSkills(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'get_image', 'updated_at', 'ordering')
    list_display_links = ('pk', 'title')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "There s no photo"


class AdminProjects(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'url')


admin.site.register(Skills, AdminSkills)
admin.site.register(Projects, AdminProjects)
admin.site.register(AboutMe, AdminAboutMe)
