# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ListModel3DView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.DetailModel3DView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/change/$',
        view=views.ChangeModel3DView.as_view(),
        name='change'
    )
]
