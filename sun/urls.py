"""sun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from views import list_view, contact_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('pages.urls', namespace='pages')),
    url(r'^snap', include('snapchat.urls', namespace='snapchat')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', list_view, name="list_view"),
    # url(r'^contact/$', contact_view, name='contact'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
