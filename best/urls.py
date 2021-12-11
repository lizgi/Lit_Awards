from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('post/profile/', views.profile,name='profile'),
    path('post/project/', views.showProject,name='project'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    # path('accounts/register/', RegistrationView.as_view(success_url='/create_profile'),name='django_registration_register'),
    
]

