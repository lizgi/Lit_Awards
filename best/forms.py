from .models import Profile,Project
from django.forms import ModelForm
from django import forms


class showprojectform(ModelForm):
    class Meta:
        model=Project
        fields=('image',
                'title',
                'description',
                'category',
                'location',
                 'url',
               )

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','contact') 

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']    