from main_app.models import Spec
from django.contrib import admin
from .models import Spec, Gear
# Register your models here.
admin.site.register(Spec)
admin.site.register(Gear)