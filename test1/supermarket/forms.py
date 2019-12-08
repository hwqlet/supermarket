from .models import *
from django.forms import Form
from django.forms import widgets
from django.forms import Field
from django.core.validators import ValidationError
from django.core.validators import RegexValidator


class register_form(forms.Form):
    """注册表单，用于渲染模板"""
    username = forms.CharField(
        max_length=20,
        label='用户名',
        strip=True,
        required=True,
        error_messages={
            'required': '必填信息',
            'max_length': '长度不能超过20个字符',
            'invalid': '格式错误'
        }
    )
    password = forms.CharField(
        min_length=7,
        label='密码',
        required=True,
        widget=forms.widgets.PasswordInput(render_value=True),
        strip=True,
        error_messages={
            'min_length': '最小长度不能小于7',
            'required': '必填信息',
        }
    )
    shenfenzheng = forms.CharField(
        label='身份证号',
        required=True,
        validators=[RegexValidator(r'((\d+){18})|((\d+){17}X)', '请输入正确的身份证号')],
        error_messages={
            'required': '必填信息'
        }
    )
    user_phone = forms.CharField(
        label='手机号',
        max_length=11,
        required=True,
        error_messages={
            'required': '必填信息',
            'max_length': '长度不符合要求',
            'invalid': '格式错误'
        },
        validators=[RegexValidator(r'1[35789]\d{9}', '请输入正确的手机号')]
    )
