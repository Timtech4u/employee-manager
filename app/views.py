from django.shortcuts import render
from .models import Profile, Organization, Job, Candidate
from .serializers import ProfileSerializer, OrganizationSerializer, JobSerializers, CandidateSerializers
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class Organization(generics.ListAPIView):
    """
    Return the organization details.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class Job(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing jobs.

    post:
    Create a new job instance.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class Candidate(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing candidates that applied to jobs.

    post:
    Create a new candidate instance.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializers