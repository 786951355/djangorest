#!/usr/bin/env python
# File Name: users/forms.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月29日 星期一 10时32分16秒
#########################################################################
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", 'email')
