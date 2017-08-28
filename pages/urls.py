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
from django.conf.urls import url
import views as page_views


app_name = 'pages'
urlpatterns = [
    url(r'^page/(?P<slug>[a-zA-Z0-9_-]+)/$', page_views.detail_view, name="page_detail"),
    # url(r'^(?P<page>[0-9]+)/$', page_views.list_view, name="page_list"),
    url(r'^page_(?P<page>[0-9]+)/(?P<article_genre>[a-zA-Z_-]+)/(?P<article_filter>[a-zA-Z_-]+)/$',
        page_views.list_view, name="page_list"),
]

# (?P<article_filter>[a-zA-Z]+)/