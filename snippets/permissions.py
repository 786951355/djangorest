#!/usr/bin/env python
# File Name: snippets/permissions.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月30日 星期二 19时21分28秒
#########################################################################
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


