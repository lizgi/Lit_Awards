from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('post/profile/', views.profile,name='profile'),
    path('post/project/', views.showProject,name='project'),
    path('update_profile/<int:id>',update_profile, name='update_profile'),
]
