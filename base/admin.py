from django.contrib import admin
from . models import Blog, Comment, Contact, Category, Curriculum, Event, Forum, Profile, Message, School

# Register your models here.

admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Curriculum)
admin.site.register(Forum)
admin.site.register(School)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "school","created")
    list_filter = ("name", "school","created" )
    

