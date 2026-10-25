"""vuedj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import re_path as url
from django.contrib import admin
from app.views import index, ProfileList, Organization, Job, Candidate
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^jobs/$', index, name='home'),
    url(r'^api/profiles/$', ProfileList.as_view()),
    url(r'^api/organization/$', Organization.as_view()),
    url(r'^api/jobs/$', Job.as_view()),
    url(r'^api/candidates/$', Candidate.as_view()),
    url(r'^api/clients/$', Candidate.as_view()),
    url(r'^api/schema/$', SpectacularAPIView.as_view(), name='schema'),
    url(r'^docs/$', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)

admin.site.site_header = 'Employee Manager & Job Application Portal'