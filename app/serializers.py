from rest_framework import serializers
from .models import Profile, Organization, Job, Candidate
from customers.models import Client

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 1

class CandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        depth = 2

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        depth = 2