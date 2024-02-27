from django.utils.deprecation import MiddlewareMixin    
from django.shortcuts import HttpResponse, redirect
   
   
class AuthMiddleware(MiddlewareMixin):
   
    def process_request(self, request):
          # 0.排除那些不需要登录就能访问的页面
          urls = [
            '/my/login/',
            '/my/register/',
            '/save/code/'
          ]
          if request.path_info in urls:
              return
   
          # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
          info_dict = request.session.get("info")
          
          if info_dict:
              return
   
          # 2.没有登录过，重新回到登录页面
          return redirect('/my/login/')


    def process_response(self,request, response): #基于请求响应
        return response