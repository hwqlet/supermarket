"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from supermarket import views as sup_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', sup_views.home, name='home-site'),
    path('login/', sup_views.login, name='denglu'),
    path('login_submit/', sup_views.login_sub, name='login_submit'),
    path('register_new/', sup_views.register, name='register'),
    # path('register_new/result/', sup_views.register_result, name='reg_result'),
    # path('register_new/result', sup_views.register_result, name='register_result'),
    path('change_pass/', sup_views.change_pass, name='change_pass'),
    path('change_pass/result/', sup_views.change_pass_result, name='change_pass_result'),
    path('user_index/', sup_views.user_index, name='user_index'),
    path('user_info/', sup_views.user_info, name='user_info'),
    path('user_purchase/', sup_views.user_purchase, name='user_purchase'),
    path('change_info/', sup_views.change_info, name='change_info'),
    path('electricity/', sup_views.electricity_del, name='electricity'),
    path('test/', sup_views.test, name='test'),
    path('user_initial/', sup_views.user_initial, name='initial'),
    path('user_extra/', sup_views.user_extra, name='extra'),
    path('user_dingdan/', sup_views.user_dingdan, name='dingdan'),
    path('user_buy/', sup_views.user_buy, name='buy'),
    path('manager_login/', sup_views.manager_login, name='manager_login'),
    path('employee_index/', sup_views.employee_index, name='employee_index'),
    path('employee_index/search/', sup_views.search, name='search'),
    path('employee_index/gen_zhangdan/', sup_views.gen_zhangdan, name='gen_zhangdan'),
    path('employee_index/middle/', sup_views.middle_request, name='middle'),
    path('employee_index/salary/', sup_views.salary, name='salary'),

    # todo 怎么映射每个用户的界面？
]

