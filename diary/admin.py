
from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_private', 'created_at')
    search_fields = ('title', 'body', 'tags')
    list_filter = ('is_private', 'created_at')
