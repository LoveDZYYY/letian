from django.db import models

# Create your models here.

"""
数据库迁移命令：
    - python manage.py makemigrations
    - python manage.py migrate
"""

# 创建用户表
class user(models.Model):
    """
    用户表
        - id
        - 姓名
        - 账号  (唯一)
        - 密码
        - 手机号    (唯一)
        - 账户余额
    """
    name = models.CharField(verbose_name='用户姓名',max_length=20,null=True,blank=True,default='yy小迷弟')
    account = models.CharField(verbose_name='用户账号',max_length=16,unique=True)
    password = models.CharField(verbose_name='用户密码',max_length=32)
    mobile = models.CharField(verbose_name='用户手机号',max_length=32,unique=True)
    # 精确到前面30位数，后面两位数
    money = models.DecimalField(verbose_name='账户余额',default=0,decimal_places=2,max_digits=30)
   



# 创建订单表，用来存储用户选择的好订单数据

class temporary_order(models.Model):
    """
    订单表
        - id
        - 用户ID
        - 用户购买的赌具
        - 待支付余额
        - 订单创建时间
        - 用户是否已支付
        - 当前的期数
        - 用户赢的钱是否已打到用户账号上了
    """

    # 级联删除，当用户被删除时自动删除该用户下的全部表信息
    user_id = models.ForeignKey(to="user",to_field="id",on_delete=models.CASCADE)

    # 用户购买的赌具
    user_buy_goods = models.CharField(verbose_name="用户购买的赌具",max_length=200)

    # 待支付余额
    stay_pay_money = models.IntegerField(verbose_name='待支付余额')

    # 订单创建时间
    order_create_time = models.DateTimeField(verbose_name='订单创建时间',auto_now=True)
    
    # 是否已支付
    is_pay = models.BooleanField(verbose_name="是否已支付",default=False)

    # 用户的钱是否已经追加到其账户上
    userPrizeReceipt = models.BooleanField(verbose_name="用户奖品是否已接收",default=False)

    current_phase = models.IntegerField(verbose_name="当前期数")


# 开奖的时间表以及开奖的生肖

class open_shengxiao(models.Model):
    """
        开奖时间表
            - id
            - 开奖时间
            - 开奖的生肖
            - 目前是第几期
            - 是否已经人工修改过(bool)
    """
    open_time = models.DateTimeField(verbose_name='开奖时间',auto_now_add=True)

    open_shengxiao = models.CharField(verbose_name="开奖生肖",max_length=200)

    current_phase = models.IntegerField(verbose_name="目前阶段",unique=True)

    is_edit = models.BooleanField(verbose_name="是否已人工修改",default=False)

# 创建一张表，用来存储用户的投注记录
class user_bet(models.Model):
    """
    用户投注记录表
        - id
        - 用户ID
        - 投注的生肖
        - 当期开奖的生肖
        - 购买生肖时订单创建时间
        - 当前阶段的期数
        - 用户共赢了多少钱
        - 开奖的时间
        - 应付用户多少钱
        - 是否已支付钱给用户    0 是没有支付    1 是已支付
    """
    user = models.ForeignKey(to="user",to_field="id",verbose_name='用户id',on_delete=models.CASCADE)
    user_bet_shengxiao = models.CharField(verbose_name="用户购买的生肖",max_length=200)
    user_bet_money = models.DecimalField(verbose_name='用户共赢了多少钱',decimal_places=2,max_digits=30)
    user_bet_time = models.DateTimeField(verbose_name='用户购买生肖时的订单创建时间')
    open_shengxiao = models.CharField(verbose_name='当期开奖的生肖',max_length=200)
    current_phase = models.ForeignKey(verbose_name='当前期数',to='open_shengxiao',to_field='current_phase',on_delete=models.CASCADE)
    open_time = models.DateTimeField(verbose_name='开奖的时间',auto_now=True)
    pay_how_much = models.DecimalField(verbose_name="应付用户多少钱",decimal_places=2,max_digits=30,default=0)
    is_pay = models.BooleanField(verbose_name="系统是否已支付资金给用户",default=False)


