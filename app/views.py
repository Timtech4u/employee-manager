from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer