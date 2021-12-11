from .models import Profile,Project
from django.forms import ModelForm
from django import forms


class showprojectform(ModelForm):
    class Meta:
        model=Project
        fields=('image',
                'title',
                'description',
                'location',
                 'url',
               )

# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio', 'profile_picture') 

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']    