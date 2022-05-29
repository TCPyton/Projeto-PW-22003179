from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Blog)
admin.site.register(QuizzScore)
admin.site.register(Picture)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(ProgrammingLanguages)
admin.site.register(Subject)