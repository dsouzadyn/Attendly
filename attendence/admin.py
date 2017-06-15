from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(SubjectHolder)
admin.site.register(Subject)
admin.site.register(Theory)
admin.site.register(Practical)