#!/usr/bin/env python
# File Name: users/urls.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月29日 星期一 10时40分31秒
#########################################################################

from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
        url(r'register/', views.register, name='register'),
        url(r'index/', views.index, name='user_index'),
        ]
