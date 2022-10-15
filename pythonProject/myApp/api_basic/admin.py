from django.contrib import admin
from .models import Asset
from .models import Report


# Register your models here.


admin.site.register(Asset)
admin.site.register(Report)