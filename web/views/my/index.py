


import random   # 随机数，一般用于验证码



from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.http import JsonResponse
# 导入用户数据库
from web.models import user


def index(request):

    # 模板文件
    return render(request=request,template_name='my/index.html')



# 登录
def login(request):
    """
        错误码：
            - 401 手机号或密码错误
    """

    # 如果是GET请求就返回页面给用户
    if request.method == 'GET':
        return render(request,'登录与注册/登录.html')
    


    res = user.objects.filter(
        password=request.POST.get("password"),
        mobile = request.POST.get("mobile"),
    ).first()
    
    # 如果为空则代表账号或者密码错误
    if res is None:
        return HttpResponse("手机号或密码错误",status=401)
    

    print("当前用户的ID：",res.id)

    # 将一些数据存储在用户的浏览器
    request.session['info'] = {
        "user_id":res.id,
        "user_name":res.name,
        "account":res.account,
        "mobile":res.mobile
    }
    
    # 制作登录成功的信息
    content = {
        "result":"Success",
        "test":"登录完成，正在跳转",
        "url":"/my/index/"
    }
    
    return JsonResponse(content,status=200)







# 生成随机的唯一11位账号

def get_random_accountNumber():
    global AccountNumber
    while True:
        AccountNumber = random.randint(10000000000,99999999999) # 生成11位随机数账号

        # 判断在数据库中是否存在该账号，如果存在就重新生成，如果不存在就结束循环并返回账号
        res = user.objects.filter(account=AccountNumber).first()

        if res is None:
            # 当前数据库中没有该账号，可以结束循环并返回账号
            break
        else:
            # 数据库中存在该账号，需要重新循环生成
            continue
    # 返回账号
    return AccountNumber




def __is_mobile(USERMOBILE) -> bool:
    """
        返回真代表当前数据库已存在手机号
    """
    # 当前手机号已存在，请使用手机号登录
        # 判断用户的手机号是唯一的
    if  user.objects.filter(mobile=USERMOBILE).first() is not None:
        # 当前数据库已存在手机号
        return True
    
    return False

# 注册
def register(request):
    """
        失败码及注解：
            - 401 验证码错误
            - 402 已存在手机号
            - 403 验证码错误
    """

    # 如果是GET请求就返回HTML文件
    if request.method == 'GET':
        return render(request,'登录与注册/注册.html')
    

    # 如果是POST请求当做是注册的数据


    # 判断验证码是否一样，如果一样就删除掉用户端的session
    try:
        if int(request.POST.get("code")) == int(request.session.get("code")):
            # 确实一模一样，需要删除客户端的session
            del request.session['code']
        else:
            # 不一样
            return HttpResponse("验证码核对失败",status=401)
    except TypeError as e:
        # 存储在用户端的session失效，可能是用户乱填验证码框
        return HttpResponse("验证码错误",status=403)


    # 判断当前用户的手机号在数据库中是否存在，如果存在则返回
    if __is_mobile(USERMOBILE=request.POST.get("mobile")):
        return HttpResponse("当前手机号已存在，请使用手机号登录",status=402)
    

    """
    接下来就获取用户的姓名、手机号、密码，然后在服务器端生成唯一的账号并存储到数据库中
    """
    data = {
        "name":request.POST.get("name"),
        "mobile":request.POST.get("mobile"),
        "password":request.POST.get("password"),
        "account":get_random_accountNumber()
    }

    # 将数据存储进数据库中
    user.objects.create(**data)
    
    # 制作注册成功后的字典返回给前端
    successDict = {
        "result":"Success",
        "redirect":"/my/login/",
        "test":"注册成功"
    }
    return JsonResponse(successDict,status=200)




# 清除session
def clone_session(request):
    request.session.clear()
    return redirect('/my/login/')




# 验证码
def save_code(request):
    """
        发送验证码
    """

    if __is_mobile(USERMOBILE=request.GET.get("mobile")):
        return HttpResponse("当前手机号已存在，请使用手机号登录",status=402)
    # 生成验证码后把验证码以session的形式返回给前端，由前端自行取验证码验证

    random_code = random.randint(1000,9999) # 验证码

    # 已session的形式返回给前端
    request.session['code'] = random_code

    content = f"[乐天]：尊敬的用户，欢迎你注册乐天赌场，本次你的注册验证码是：{random_code}，请尽早使用，谢谢！"
    return HttpResponse(content,status=200)
