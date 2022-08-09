from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('community/', views.community, name='community'),
    path('forum/', views.forum, name='forum'),
    path('event/', views.event, name='event'),
    path('eventSingle/<int:pk>/', views.eventSingle, name='eventSingle'),
    path('blog/', views.blog, name='blog'),
    path('blogSingle/<int:pk>/', views.blogSingle, name='blogSingle'),
    path('contact/', views.contact, name='contact'),
]
