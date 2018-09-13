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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from app.views import index, ProfileList, Organization, Job, Candidate
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^jobs/$', index, name='home'),
    url(r'^api/profiles/$', ProfileList.as_view()),
    url(r'^api/organization/$', Organization.as_view()),
    url(r'^api/jobs/$', Job.as_view()),
    url(r'^api/candidates/$', Candidate.as_view()),
    url(r'^api/clients/$', Candidate.as_view()),
    url(r'^docs/', include_docs_urls(title='API docs'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

admin.site.site_header = 'Employee Manager & Job Application Portal'