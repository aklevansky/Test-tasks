# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^loans/', include('loans.urls')),
    url(r'^testing/', include('testing.urls')),
    url(r'^menu_tag/', include('menu_tag.urls')),

    url(r'^admin/', admin.site.urls)
]