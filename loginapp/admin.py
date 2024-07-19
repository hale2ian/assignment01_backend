from django.contrib import admin

from loginapp.models import Course, Program, UserRegister

# Register your models here.

admin.site.register(Course)
admin.site.register(Program)
admin.site.register(UserRegister)
