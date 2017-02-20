# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.views import (
    logout_then_login, login,
    password_change
)
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=generic.RedirectView.as_view(
            url=reverse_lazy('user:redirect')
        ),
        name='index'
    ),
    url(
        regex='^login/$',
        view=login,
        kwargs={'template_name': 'login.html'},
        name='login'
    ),
    url(
        regex=r'^change-password/$',
        view=password_change,
        kwargs={
            'post_change_redirect': reverse_lazy('user:logout'),
            'template_name': 'password_change_form.html'
        },
        name='change-password'
    ),
    url(
        regex=r'^add/$',
        view=views.UserDesignerCreateAccount.as_view(),
        name='create'
    ),
    url(
        regex=r'^redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/change/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex='^model-list/$',
        view=views.DesignerListModelView.as_view(),
        name='model-list'
    ),
    url(
        regex='^model-list/add/$',
        view=views.DesignerAddModelView.as_view(),
        name='add-model'
    ),
    url(
        regex='^model-list/(?P<uid>[a-f,0-9]+)/$',
        view=views.DesignerModelDetailView.as_view(),
        name='model-detail'
    ),
    url(
        regex='^model-list/(?P<uid>[a-f,0-9]+)/change/$',
        view=views.DesignerChangeModelView.as_view(),
        name='model-change'
    ),
    url(
        regex='^logout/$',
        view=logout_then_login,
        name='logout'
    ),
]
