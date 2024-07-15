from django.contrib import admin

from loginapp.models import Message, ChatRoom

# Register your models here.

admin.site.register(Message)
admin.site.register(ChatRoom)