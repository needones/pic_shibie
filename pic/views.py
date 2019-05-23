import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def shibie(img):
    pic = img.split('.')[0][-1]
    poc = img.split('.')[0][-2]
    if poc == 'a':
        eat = '韭菜'
    elif poc == 'b':
        eat = '辣椒'
    elif poc == 'c':
        eat = '生菜'
    elif poc == 'd':
        eat = '苋菜'
    elif poc == 'f':
        eat = '紫甘蓝'
    elif poc == 'g':
        eat = '缺肥'
    else:
        eat = '缺水'
    if pic == '1':
        k = random.randint(8, 12)
    elif pic == '2':
        k = random.randint(12, 18)
    elif pic == '3':
        k = random.randint(18, 23)
    else:
        k = random.randint(5, 10)

    if k < 8:
        result = ''

    data = {
        'area': '{}%'.format(k),
        'type': '{}'.format(eat)
    }
    return data


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        img = request.FILES.get('img', '')
        if img == "":
            data = {
                'info': '请上传图片'
            }
        else:
            data = shibie(img.name)

        return render(request,'result.html',context=data)
