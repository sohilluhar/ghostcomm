from django.contrib import admin

# Register your models here.
# core/admin.py

# core/admin.py

from django.contrib import admin
from .models import Group, Message

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'topic', 'created_at')  # Ensure 'created_at' is a valid field
    search_fields = ('group_id', 'topic')
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'anon_name', 'created_at')  # Ensure 'username' and 'timestamp' are valid fields
    search_fields = ('anon_name', 'group__group_id')
    ordering = ('-created_at',)
