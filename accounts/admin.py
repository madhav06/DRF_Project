from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Manager)
admin.site.register(Staff)
admin.site.register(Tag)
admin.site.register(utility)
