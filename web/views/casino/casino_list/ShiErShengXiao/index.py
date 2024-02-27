
import json

from django.shortcuts import render,HttpResponse,redirect

from django.http import JsonResponse

from web.models import temporary_order,user,open_shengxiao,user_bet

# 用于筛选出当前的奖期数
from django.db.models import Max

from django import forms

from datetime import datetime

from decimal import Decimal

class orderModelsForm(forms.ModelForm):
        class Meta:
            model = temporary_order  #对应的Model中的类
            fields = ['user_id','user_buy_goods','stay_pay_money','current_phase']

def index(request):

    if request.method == 'GET':
        return render(request=request,template_name='casino/赌场列表/十二生肖/index.html')
    

    elif request.method == 'POST':
        """
        错误码：
            - 400   已下注
            - 401   已到开奖时间
        """
        # 获取用户 ID
        user_id = request.session.get("info")['user_id']
        # 获取当前期数并判断用户是否在历史表中是否有数据
        DQQS = open_shengxiao.objects.all().aggregate(Max('current_phase'))['current_phase__max']
        if user_bet.objects.filter(user_id=request.session['info']['user_id'],current_phase_id=DQQS).first() is not None:
             return HttpResponse("你已在本期中下注，请勿重复下注！",status=401)

        # 判断订单表中的期数是否等于最新期数，如果不是需要删除掉
        # 代码执行到这里需要判断一次订单表中是否还有该用户的残留，如果有需要删除
        a = temporary_order.objects.filter(user_id=user_id).first()
        # 如果 a 为空，说明用户在订单表中没有数据，可以创建表
        if a is not None:
            if a.current_phase != DQQS:
                a.delete()
        # 保证在订单表中，该用户不能存在，如果存在说明用户已经有一笔订单了，需要先支付订单在购买新的订单
        if temporary_order.objects.filter(user_id=user_id).first() is not None:
             return HttpResponse("你已下注，请等待开奖结果！",status=400)

        # 如果当前的开奖时间已经到了，那么就返回不允许用户下注了
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d")
        # 判断当前时间是否等于开奖的时间
        if open_shengxiao.objects.filter(current_phase=DQQS).first().open_time.strftime("%Y-%m-%d") == formatted_now:
             return HttpResponse("当前已到开奖时间，请等待下一期再来吧!~",status=401)
        # 将 QueryDict 变为可修改对象
        post_data = request.POST.dict()

        # 修改字典
        post_data['user_id'] = user_id
        # 获取开奖数据库中最大的一期，也就是当前期数
        post_data['current_phase'] = DQQS
        
        form = orderModelsForm(data=post_data)
        
        if form.is_valid():
            form.save()
            # 验证成功
            # 制作返回数据，让前端跳转到支付页面
            content = {
                 "resuil":"订单创建成功，正在跳转支付页面...",
                 "url":"/pay/"
            }
            return JsonResponse(content,status=200,content_type='application/json')
        
        MsgError = form.errors.as_text()
        return HttpResponse(MsgError)
    




# 编写一个函数，用来检测如果判断出是Decimal类型就自动转换成str并返回
def DefaultDecimal(obj):
     
     if isinstance(obj,Decimal):
          obj = str(obj)
    
     return json.dumps(obj)



# 支付页面
def pay(request):
    """
        错误码：
            - 400 余额不足，因为浏览器提交上来的不是 1 
            - 401 余额不足，因为用户浏览器提交上来的金额与数据库中用户的资金相减后得到的数小于0
            - 402 帐户余额更新失败，可能不是用户的错。管理员应检查控制台是否存在此错误。
    """
    # 通过用户的ID获取用户的订单
    user_id = request.session.get("info")['user_id']

    # 测试代码，一会删除：用户订单永远不能支付成功
    # temporary_order.objects.filter(user_id=user_id).update(is_pay=False)
    # user.objects.filter(id=user_id).update(money=1000000)
    # 测试代码，一会删除：用户订单永远不能支付成功

    if request.method == 'GET':
        # 在订单表中查询判断有没有数据
        query = temporary_order.objects.filter(user_id=user_id).first()
        if query is None:
            # 如果在订单表中没有数据，则重定向到赌场首页
            return redirect("/casino/shiershengxiao/index/")
        
        # 获取生肖并转换为list
        shengxiao = json.loads(query.user_buy_goods) # [{"duju":"兔","money":100}]

        # 向用户的数据库中查询用户目前有多少钱，然后通过session的形式返回给前端，由前端自行校验
        request.session['user_money'] = float(user.objects.filter(id=user_id).first().money)

        content = {
            "user_shengxiao":shengxiao,
            "pay_money":query.stay_pay_money,
        }
        return render(request,'casino/赌场列表/十二生肖/pay.html',content)
    
    # 获取浏览器提交上来的资金，以便在用户表中扣除
    if int(request.POST.get('code')) != 1:
         return HttpResponse("余额不足！",status=400)
    

    # 向用户资金中扣除浏览器提交上来的资金
    # 用户的账户资金
    user_money = user.objects.filter(id=user_id).first().money
    # 浏览器提交上来的资金
    Bro_money = int(request.POST.get("AccountMoney"))
    count = user_money - Bro_money
    # 判断能不能相减，如果不可以就返回
    if count < 0:
         return HttpResponse("余额不足",status=401)
    
    if user.objects.filter(id=user_id).update(money=count) != 1:
        # 说明账户资金更改失败，但是应该不是用户的错，如果出现此错误需要管理员前往控制台查看
        print("账户资金更改失败",user.objects.filter(id=user_id).update(money=count))
        return HttpResponse("Account balance update failed, possibly not user's fault. Admin should check the console for this error.",status=402)

    # 当支付成功后需要将用户在订单表中的 “是否已支付” 字段改为真
    temporary_order.objects.filter(user_id=user_id).update(is_pay=True)

    # 代码执行到此处说明一切支付流程都完毕了，现在制作返回字典通知浏览器跳转到指定页面
    content = {
         "result":"Success",
         "text":"支付成功，正在跳转...",
         "url":"/my/order/goods/index/"
    }
    return JsonResponse(content,status=200)

