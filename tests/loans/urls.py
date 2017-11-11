# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views

urlpatterns = (

    # PartnerAPI
    url(r'^questionnaires/$',
        views.PartnerAPI.as_view()),

    url(r'^questionnaires/(?P<pk>\S+)/$',
        views.PartnerAPI.get_by_pk),

    url(r'^questionnaires/submission/$',
        views.PartnerAPI.submit),


    # BankAPI
    url(r'^submissions/$',
        views.BankAPI.get_submissions),

    url(r'^submissions/(?P<pk>\S+)/$',
        views.BankAPI.get_submission)
)
