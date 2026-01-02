from django.shortcuts import render, redirect
from django.http import HttpResponse


def disable_ann(request):
    referer = '/announcements/page1'

    try:
        referer = request.META['HTTP_REFERER']
    except:
        print("========= HELLO ========")


    response = redirect(referer)
    response.set_cookie('disable_announcements', True)

    return response

def pagen1(request):
    response = render(request, 'announcements/page1.html')

    return response

def pagen2(request):
    return render(request, 'announcements/page2.html')