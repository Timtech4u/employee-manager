from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Organization(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    
    def save(self, *args, **kwargs):
        if Organization.objects.exists() and not self.pk:
            raise ValidationError("You can only have this organization")
        return super(Organization, self).save(*args, **kwargs)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    skillset = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class JobStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    required_skills = models.TextField(blank=True, null=True)
    designation = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    nummber_of_position = models.IntegerField(blank=True, null=True)
    required_qualification = models.TextField(blank=True, null=True)
    required_years_experience = models.IntegerField(blank=True, null=True)
    employment_status = models.ForeignKey(JobStatus, blank=True, null=True, on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
