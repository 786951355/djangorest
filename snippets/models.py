from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [ item for item in get_all_lexers() if item[1]]

LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly',max_length=100)
    # 添加两个字段，一个字段用于表示创建代码片段的用户，其他字段将用于存储代码的突出显示的HTML表示形式
    # 这里关联到自己定义的用户模型
    owner = models.ForeignKey('users.User',related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
