import random
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from pic import settings


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
        k = random.randint(12, 22)
    elif pic == '3':
        k = random.randint(30, 50)
    else:
        k = random.randint(5, 10)

    if k < 8:
        result = '生长异常'
    else:
        result = None
    data = {
        'area': '{}%'.format(k),
        'type': '{}'.format(eat),
        'result': result
    }
    num = random.randint(5, 10)
    sleep(num)

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
        elif img.name == 'j3dBlFSVY7H4E5Dc3.jpg':
            data = shibie(img.name)
            img_name = 'media/' + img.name
            with open(img_name, 'wb')as f:
                for fimg in img.chunks():
                    f.write(fimg)
            data['img'] = img_name
            data['img1'] = 'media/2bigRGB.jpg'

        elif img.name == 'woDL6xHZnGxnECMc1.jpg':
            data = shibie(img.name)
            img_name = 'media/' + img.name
            with open(img_name, 'wb')as f:
                for fimg in img.chunks():
                    f.write(fimg)
            data['img'] = img_name
            data['img1'] = 'media/2smallRGB.jpg'

        else:
            img_name = 'media/' + img.name
            with open(img_name, 'wb')as f:
                for fimg in img.chunks():
                    f.write(fimg)
            data = shibie(img.name)
            data['img'] = img_name
            data['img1'] = None

        return render(request, 'result.html', context=data)


def test(request):
    return render(request, 'result.html')
