from django import forms
from django.db import models

class CommentForm(forms.Form):
    '''
    评论表单
    '''

    # 定义三个字段：称呼、邮箱和评论内容
    name = forms.CharField(label='称呼', max_length=16, error_messages={
            'required': '请填写您的称呼',
            'max_length': '称呼太长'
        })
    email = forms.EmailField(label='邮箱', error_messages={
            'required': '请填写您的邮箱',
            'invalid': '邮箱格式不正确'
        })
    content = forms.CharField(label='评论内容', error_messages={
            'required': '请填写您的评论内容',
            'max_length': '评论内容太长'
        })












