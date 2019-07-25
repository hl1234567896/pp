from django.http import  HttpResponse



def index(requests):
    print('卢本伟牛逼')
    return HttpResponse('我卢本伟,没有开挂')


def log(request):
    print('这是登录视图')

    return HttpResponse()