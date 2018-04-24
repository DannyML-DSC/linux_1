from django.contrib import admin

# Register your models here.

from .models import ScrummyGoals, Scrumystatus, Scrumyuser, GoalStatus

admin.site.register(Scrumyuser)
admin.site.register(Scrumystatus)
admin.site.register(ScrummyGoals)
admin.site.register(GoalStatus)
