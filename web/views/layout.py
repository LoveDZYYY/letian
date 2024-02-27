
import random

from django.shortcuts import render
from datetime import datetime
from web.models import open_shengxiao

def index(request):
    # 模板文件
    return render(request=request,template_name='layout.html')




# 开场
def OPEN(
        CURRENT_PHASE=1,
        target_date = None,
        OPENSHENGXIAO_LIST = None,
        is_edit = False
):
    """
        CURRENT_PHASE:当前第几阶段，默认1，后面开发后台后按照后台指示
        target_date: 开奖的时间，后面开发后台后按照后台指示
        OPENSHENGXIAO_LIST: 开奖的结果，后面开发后台后按照后台指示
        is_edit: 是否被人修改过，后面开发后台后按照后台指示
        设置开奖时间和开奖结果
    """

    
    # 首先判断开奖表没有当前期的数据
    if open_shengxiao.objects.filter(current_phase=CURRENT_PHASE).first() is not None:
        # 数据库中有当前期数，不必执行下面代码
        print("数据库中已设置，代码不再往下执行")
        return False
    
    # 定义开奖结果
    OPENSHENGXIAO = [
            '鼠',
            '牛',
            '虎',
            '兔',
            '龙',
            '蛇',
            '马',
            '羊',
            '猴',
            '鸡',
            '狗',
            '猪',
    ]
    if OPENSHENGXIAO_LIST is None:

        # 开奖结果
        OPENSHENGXIAO_LIST = random.sample(OPENSHENGXIAO,5)

    # 设置开奖的时间
    # 生成指定日期的时间数据
    if target_date is None:
        target_date = datetime.strptime('2024-02-25', r'%Y-%m-%d')
    

    
    # 制作数据方便上传到数据库
    data = {
        "is_edit":is_edit,
        "open_shengxiao":OPENSHENGXIAO_LIST,
        "open_time":target_date,
        "current_phase":CURRENT_PHASE
    }
    # 把数据上传到数据库
    open_shengxiao.objects.create(**data)
    
    
    return True

