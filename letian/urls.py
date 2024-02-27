"""
URL configuration for letian project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from web.views import layout
from web.views.index import index as home
from web.views.casino import index as CasinoHome
from web.views.casino.casino_list.ShiErShengXiao import index as ShierShengXiaoIndex    # 十二生肖首页
from web.views.my import index as MyIndex
from web.views.my.MyOrderGoods import index as my_order_goods   # 我的订单 - index文件
from web.views.my.MyAccount import index as Myaccount
urlpatterns = [
    path('layout/', layout.index),  # 模板文件
    




    # 首页
    path('index/', home.index), # 首页
    # 首页

    # 赌场
    path('casino/index/', CasinoHome.index), # 赌场-首页


    # 十二生肖
    path('casino/shiershengxiao/index/', ShierShengXiaoIndex.index),    # 首页
    path('pay/', ShierShengXiaoIndex.pay),  # 支付页面
    # 十二生肖


    # 赌场


    # 我的
    path('my/index/', MyIndex.index),   # 我的-首页
    path('sessino/clear/', MyIndex.clone_session),   # 我的-清除session
    path('my/login/', MyIndex.login),   # 我的-登录
    path('my/register/', MyIndex.register),   # 我的-注册
    path('save/code/', MyIndex.save_code),  # 验证码逻辑
    path('my/order/goods/index/', my_order_goods.index),  # 我的订单 - 首页
    path('my/account/index/', Myaccount.index),  # 我的余额 - 首页
    
    # 我的
]
