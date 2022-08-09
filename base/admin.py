from django.contrib import admin
from . models import Blog, Comment, Contact, Category, Event

# Register your models here.

# admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
# admin.site.register(Room)
admin.site.register(Contact)
admin.site.register(Event)