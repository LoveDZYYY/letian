# 我的账户余额


from django.shortcuts import render,HttpResponse,redirect

from web.models import user
def index(request):
    # 获取用户的数据
    user_info = user.objects.filter(id=request.session.get('info')['user_id']).first()
    # 返回用户数据
    response = {
        "user_data":user_info
    }
    return render(request,'my/我的余额/index.html',response)