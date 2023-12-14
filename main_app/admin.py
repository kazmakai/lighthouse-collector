from django.contrib import admin

# Import your models here
from .models import Lighthouse, Visitor

# Register your models here
admin.site.register(Lighthouse)
admin.site.register(Visitor)