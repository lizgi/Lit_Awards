from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('profile_pic','bio','contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ('image','title','description','category','location','url')