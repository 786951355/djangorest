#!/usr/bin/env python
# File Name: snippets/urls.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月30日 星期二 15时33分11秒
#########################################################################
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
        url(r'^snippets/$', views.SnippetList.as_view()),
        url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
