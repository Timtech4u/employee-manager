from django.contrib import admin
from .models import Employee, Profile, Document, Organization, Department, Designation, JobType, Job, Candidate
from customers.models import Client
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    search_fields = ['employee_id', 'profile__user__first_name', 'profile__user__last_name', 'work_email', 'profile__user__email' ]
    list_display = ('employee_id', 'profile__user__first_name', 'profile__user__last_name')
    list_filter = ('department', 'designation', 'employment_type')

# Allowing Us to Edit User Profile
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

admin.site.register(Document)
admin.site.register(Client)

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(JobType)
admin.site.register(Job)
admin.site.register(Candidate)