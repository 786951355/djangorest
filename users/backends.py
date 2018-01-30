#!/usr/bin/env python
# File Name: users/backends.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月29日 星期一 15时11分44秒
#########################################################################

from .models import User

class EmailBackend(object):
    def authenticate(self, **credentials):
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials['password']):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
