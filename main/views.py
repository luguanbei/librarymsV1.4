# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from models import *

# Create your views here.
def index_view(request):
    return render(request,'index.html')


def login_view(request):
    if request.method == 'GET':
        if request.COOKIES.has_key('loginUser'):
            loginUser = request.COOKIES.get('loginUser', '').split(',')
            name = loginUser[0]
            pwd = loginUser[1]

            return render(request, 'login.html', {'name': name, 'pwd': pwd})
        return render(request, 'login.html')
    else:
        name = request.POST.get('name', '')
        pwd = request.POST.get('pwd', '')
        flag = request.POST.get('flag', '')


        response = HttpResponse()
        if name == 'zhangsan' and pwd == '123':
            response.status_code = 302
            response.setdefault('Location', '/')
            if flag == '1':
                response.set_cookie('loginUser', name + ',' + pwd, max_age=3 * 24 * 60 * 60, path='/login/')

                return response
            else:
                response.delete_cookie('loginUser', path='/login/')
                return response
        else:
            response.delete_cookie('loginUser', path='/login/')
            response.status_code = 302
            response.setdefault('Location', '/login/')
            return response


def manager_view(request):
    return render(request,'manager.html')





def change_view(request):
    return render(request,'pwd_Modify.html')


def reader_view(request):
    return render(request,'reader.html')


def library_view(request):
    return render(request,'library_modify.html')


def readerType_view(request):
    return render(request,'readerType.html')


def parameter_view(request):
    return render(request,'parameter_modify.html')


def bremind_view(request):
    return render(request,'bremind.html')


def borrowQuery_view(request):
    return render(request,'borrowQuery.html')


def bookType_view(request):
    return render(request,'bookType.html')


def bookRenew_view(request):
    return render(request,'bookRenew.html')


def bookQuery_view(request):
    return render(request,'bookQuery.html')


def bookcase_view(request):
    return render(request,'bookcase.html')


def bookBorrow_view(request):
    return render(request,'bookBorrow.html')


def bookBack_view(request):
    return render(request,'bookBack.html')


def book_view(request):
    return render(request,'book.html')