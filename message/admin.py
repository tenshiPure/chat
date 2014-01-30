from django.contrib import admin

from message.models import Message, Tag

admin.site.register(Message)
admin.site.register(Tag)
