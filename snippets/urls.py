#!/usr/bin/env python
# File Name: snippets/urls.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月30日 星期二 15时33分11秒
#########################################################################
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
