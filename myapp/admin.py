from django.contrib import admin

from .models import Student
from .models import *
from .models import Games
# Register your models here.

admin.site.register(Student)
admin.site.register(Games)