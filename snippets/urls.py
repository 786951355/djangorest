#!/usr/bin/env python
# File Name: snippets/urls.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月30日 星期二 15时33分11秒
#########################################################################
from django.conf.urls import url
from snippets import views

urlpatterns = [
        url(r'^snippets/$', views.snippet_list),
        url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
        ]
