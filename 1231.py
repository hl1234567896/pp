from django.http import  HttpResponse



def index(requests):
    print('卢本伟牛逼')
    return HttpResponse('我卢本伟,没有开挂')