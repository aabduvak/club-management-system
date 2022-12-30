from django.contrib import admin
from .models import User, Role, Event, Club

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Event)
admin.site.register(Club)
