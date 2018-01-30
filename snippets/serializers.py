#!/usr/bin/env python
# File Name: snippets/serializers.py
# Author: test
# mail: test@163.com
# Created Time: 2018年01月30日 星期二 10时59分26秒
#########################################################################

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
