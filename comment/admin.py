from django.contrib import admin
# 同一个目录导入用.model
from .models import Comment

# Register your models here.
# 注册模型
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'comment_time', 'user', 'root', 'parent')