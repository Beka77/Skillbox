from django.contrib import admin
from apps.settings.models import Setting, News, Contact
# Register your models here.
admin.site.register(Setting)
admin.site.register(News)
admin.site.register(Contact)
