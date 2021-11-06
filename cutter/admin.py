from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'author', 'url', 'short_url')
    search_fields = ('url',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Link, LinkAdmin)
