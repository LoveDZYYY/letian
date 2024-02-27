
import json
from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Max    
from web.models import user,temporary_order,open_shengxiao,user_bet
from django.utils.safestring import mark_safe
from django.db.models import QuerySet
# 需要编写一个函数用来计算用户购买的生肖与开奖的生肖
# 这个函数的作用是根据传进来的生肖名字（DujuName）获取用户在购买该生肖时所花的金额并 乘 1倍返回
def ADDMONEY(QueryDict,DujuName):
    
    """
        QueryDict: 用户订单数据
        DujuName: 生肖名称
    
    """
    DujuName = str(DujuName)
    MO = 0
    
    if isinstance(QueryDict,str):
        QueryDict = eval(QueryDict)

    for obj in QueryDict:
        if obj['duju'] == DujuName:
            MO = obj['money'] * 2

    return MO


# 编写一个函数返回用户的全部购买信息
def __USERBETDATAALL(user_data_all=None,is_res_order=[]) -> list:
        """
            user_data_all: 返回用户记录表中的全部历史记录
            is_res_order: 返回本期数据，如果开了新的一期但是当前没有到开奖的时间，那么就返回本期数据,数据格式：[临时表，开奖表]
        """
        # 返回用户的购买记录
        USERBETDATA = []
        if is_res_order != []:
            # 定义一个变量用来存储用户赢了多少钱
            good_money = 0
            # 制作开奖HTML文本
            OPENHTML = ''
            # 取出用户的购买生肖[{"duju":"龙","money":10}]
            user_bet_shengxiao =is_res_order[0].user_buy_goods
            # 取出当期开奖的生肖
            this_open_shengxiao = is_res_order[1].open_shengxiao
            # 获取用户共赢了多少钱
            for i in eval(this_open_shengxiao):
                # i 代表着开奖的一个生肖
                good_money += ADDMONEY(QueryDict=json.loads(json.dumps(user_bet_shengxiao)),DujuName=i)
                NEWOPENHTML = f"""
                                        <h1>未到开奖时间</h1>
                                """
                OPENHTML = OPENHTML + NEWOPENHTML
                break
                
            # 获取当前的期数
            current_phase = is_res_order[0].current_phase

            # 制作成字典
            UUUUDICT = {
                "good_money":good_money,# 用户赢了多少钱
                "user_bet_shengxiao":eval(user_bet_shengxiao),# 用户购买的生肖
                "OPENHTML":mark_safe(OPENHTML),# 返回HTML文本
                "user_bet_time":is_res_order[0].order_create_time,# 用户下注时间
                "open_time":is_res_order[1].open_time, # 开奖时间
                "user_bet_shengxiao_length":len(eval(user_bet_shengxiao)),    # 用户购买了多少个生肖
                "user_bet_money":is_res_order[0].stay_pay_money,    # 用户支付了多少钱
                "is_res_order":1,
                "current_phase":current_phase,  # 当期期数
                "is_pay":is_res_order[0].is_pay,    # 用户是否在本期中已支付
                "open_current_phase":is_res_order[1].current_phase,  # 当前开奖是第几期
            }
            # print(eval(json.loads(json.dumps(this_open_shengxiao))),type(eval(json.loads(json.dumps(this_open_shengxiao)))))
            USERBETDATA.append(UUUUDICT)
        if user_data_all is not None:
            for obj in user_data_all:
                # 定义一个变量用来存储用户赢了多少钱
                good_money = 0
                # 制作开奖HTML文本
                OPENHTML = ''
                # 取出用户的购买生肖[{"duju":"龙","money":10}]
                user_bet_shengxiao =obj.user_bet_shengxiao
                # 取出当期开奖的生肖
                this_open_shengxiao = obj.open_shengxiao
                # 获取用户共赢了多少钱
                for i in eval(this_open_shengxiao):
                    # i 代表着开奖的一个生肖
                    good_money += ADDMONEY(QueryDict=json.loads(json.dumps(user_bet_shengxiao)),DujuName=i)
                    NEWOPENHTML = f"""
                                            <tr>
                                                <td>
                                                    <div class="duju_box" style="background-color: rgb(255, 149, 0);">{i}</div>
                                                </td>
                                                <td>$ <span>{ADDMONEY(QueryDict=json.loads(user_bet_shengxiao),DujuName=i)}</span> 元</td>
                                            </tr>
                                    """
                    OPENHTML = OPENHTML + NEWOPENHTML
                # 获取期数
                current_phase = obj.current_phase_id
                # 制作成字典
                UUUUDICT = {
                    "good_money":good_money,# 用户赢了多少钱
                    "user_bet_shengxiao":eval(user_bet_shengxiao),# 用户购买的生肖
                    "OPENHTML":mark_safe(OPENHTML),# 返回HTML文本
                    "user_bet_time":obj.user_bet_time,# 用户下注时间
                    "open_time":obj.open_time, # 开奖时间
                    "user_bet_shengxiao_length":len(eval(user_bet_shengxiao)),    # 用户购买了多少个生肖
                    "user_bet_money":obj.user_bet_money,    # 用户支付了多少钱
                    "is_res_order":0,   # 当前是否已经是开奖的时间了
                    "current_phase":current_phase,  # 当期期数
                    "is_pay":obj.is_pay,    # 用户是否在本期中已支付
                    "open_current_phase":obj.current_phase_id,  # 当前开奖是第几期
                }
                # print(eval(json.loads(json.dumps(this_open_shengxiao))),type(eval(json.loads(json.dumps(this_open_shengxiao)))))
                USERBETDATA.append(UUUUDICT)
        
        

        return USERBETDATA

# 编写函数可以自动识别当期期数并自动把钱添加进账号
def __AI_ADDMONEY(userID,OrderGoods=None):
    """
    
        获取用户的id并拿着id去历史记录表中获取当前期数，并判断是否已支付给用户金钱
        OrderGoods: 用户临时订单的数据
    """
    # 用户在当前期的数据
    userdata =  user_bet.objects.filter(current_phase_id=user_bet.objects.filter(user_id=userID).aggregate(Max('current_phase_id'))['current_phase_id__max']).first()

    # 如果 userdata 为 None 代表用户一次也没有购买过订单，直接返回即可
    if userdata is None:return
    if OrderGoods is None:return

    # 在此处判断用户在临时表中是否已经完成了支付
    
    if OrderGoods.is_pay is False:return 

    # 获取是否已支付字段
    B = 0   # 表示需要发给用户多少钱
    if userdata.is_pay is False:
        # 没有支付给用户
        # 获取开奖的数据与用户数据进行比较判断
        # 获取用户的生肖数据
        user_shengxiao_data = eval(userdata.user_bet_shengxiao)
        # 定义变量代表总钱，如果当前金钱还是0说明用户在本期中没有中奖
        a = 0
        for obj in json.loads(json.dumps((userdata.open_shengxiao))):
            # obj是开奖的每一个生肖
            money = ADDMONEY(user_shengxiao_data,obj)
            a += money

        if a != 0:
            b = user.objects.filter(id=userID).first().money
            B = b + a

            user.objects.filter(id=userID).update(money=B)
        # 修改支付字段
        user_bet.objects.filter(current_phase_id=user_bet.objects.filter(user_id=userID).aggregate(Max('current_phase_id'))['current_phase_id__max']).update(is_pay=True)
        user_bet.objects.filter(current_phase_id=user_bet.objects.filter(user_id=userID).aggregate(Max('current_phase_id'))['current_phase_id__max']).update(pay_how_much=B)

    return


def index(request):
    """
        请按照下面代码让前端显示不同数据
            - yy:0 没有查询到用户的信息
            - yy:1 赌场未开放
            - yy:2 未到开奖时间
            - yy:3 还原全部的历史记录
    """
    # 获取用户的session
    USERSESSION = request.session.get('info')
    # 获取开奖信息
    # 从 open_shengxiao 数据库中获取字段名为： “current_phase” 中的最大一个数
    OPENDATA = open_shengxiao.objects.filter(current_phase=open_shengxiao.objects.all().aggregate(Max('current_phase'))['current_phase__max'])[0]
    # 获取用户在订单中的数据
    user_order_data = temporary_order.objects.filter(user_id=USERSESSION['user_id']).first()
    
    if user_order_data is None:
        # 没有查询到用户信息    0
        # 拿着用户的id到历史记录单表找找，如果那里也没有就返回0
        if user_bet.objects.filter(user_id=USERSESSION['user_id']).first() is None:
            return render(request,'my/我的订单/index.html',{"yy":0})
        
        # 返回历史的记录
        a = __USERBETDATAALL(user_data_all=user_bet.objects.filter(user_id=USERSESSION['user_id']))
        content = {
        "yy":3,
        "USERBETDATA":a
        }
        return render(request,'my/我的订单/index.html',content)
    
    # 获取用户的生肖数据
    UserShengXiaoData = json.loads(user_order_data.user_buy_goods)
    # 获取用户购买生肖的数量
    ShengXiaoNumber = len(UserShengXiaoData)

    
    # 判断是否有期数数据
    if OPENDATA is None:
        # 说明当前赌场一次都没有开过，相当于没有开店
        return render(request,'my/我的订单/index.html',{"yy":1})
    

    # 判断当前时间是否没有到达指定的开奖时间
    KJSJ = OPENDATA.open_time.strftime("%Y-%m-%d")  # 开奖时间

    YHSJ = user_order_data.order_create_time.strftime("%Y-%m-%d")
    
    if YHSJ != KJSJ:
        """
        未到开奖时间：
            可返回用户上几期的开奖数据(yes)
            
            返回用户这期的开奖数据
        """
        # 制作返回字典
        content = {
            "yy":2,
            "USERBETDATA":__USERBETDATAALL(user_data_all=user_bet.objects.filter(user_id=USERSESSION['user_id']),is_res_order=[user_order_data,OPENDATA])
        }
        
        return render(request,'my/我的订单/index.html',content)
    # 判断当前的开奖记录是否已经更新到用户的投注记录中
    # 如果当前已经到了开奖时间而且用户的购买期数与数据库的开奖期数相同就添加入库
    """
        判断方法
            - 获取当前开奖期数
            - 在用户记录表中是否有该期数
            - 如果有则不执行创建代码
            - 如果没有则更新到数据库中

        为什么这样做？
            下面是已知的用法
                - 方便返回用户前几期购买的数据
    """
    # 获取开奖的时间(KJSJ)
    if len(user_bet.objects.filter(user_id=USERSESSION['user_id'],current_phase_id=OPENDATA.current_phase)) <= 0:
        # 用户在本期购买的数据没有添加进数据库
        # 添加入库
        user_order = temporary_order.objects.filter(user_id=USERSESSION['user_id']).first()
        user_bet.objects.create(
            user_bet_shengxiao = user_order.user_buy_goods, # 用户下注的生肖
            user_bet_money = user_order.stay_pay_money, # 用户下注时花的钱
            user_bet_time = user_order.order_create_time,   # 用户的下单时间
            open_shengxiao = OPENDATA.open_shengxiao,   # 当期中开奖的生肖
            current_phase_id = OPENDATA.current_phase,  # 当期期数
            user_id = USERSESSION['user_id'],    # 购买用户的ID
            open_time = OPENDATA.open_time, # 开奖的时间
        )

    # 显示完用户的全部数据
    # 制作返回字典
    # 系统是否已支付金钱给用户(消耗代码)
    __AI_ADDMONEY(USERSESSION['user_id'],temporary_order.objects.filter(user_id=USERSESSION['user_id']).first())

    
    a = __USERBETDATAALL(user_data_all=user_bet.objects.filter(user_id=USERSESSION['user_id']))
    
    content = {
        "yy":3,
        "USERBETDATA":a
    }
    return render(request,'my/我的订单/index.html',content)