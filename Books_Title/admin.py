from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Title)
admin.site.register(Books)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(ID)