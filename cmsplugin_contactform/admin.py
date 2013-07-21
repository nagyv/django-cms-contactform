from django.contrib import admin
from .models import Message, Group

class MessageAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    list_display = ('name', 'email', 'subject', 'created', 'group')

admin.site.register(Group)
admin.site.register(Message, MessageAdmin)