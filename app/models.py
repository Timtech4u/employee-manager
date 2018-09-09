from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Organization(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Document(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Profile(models.Model):
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    pass

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
