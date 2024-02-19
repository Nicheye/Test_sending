from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Operators)
admin.site.register(Tags)
admin.site.register(Send_Status)
admin.site.register(Sender)
admin.site.register(Client)
admin.site.register(Message)