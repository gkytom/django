from django.shortcuts import render
from django.views.decorators import csrf
from excel_show.Functions.handle_execl import *
from django.http import HttpResponse
from xlrd import *
import shutil


# handle_excle_rs = gain_data(request.POST['q'], 'ZCFES')
# 接收POST请求数据

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt1'] =request.POST['q']
        # shutil.move(request.POST['q'], 'D:\workspace\django_excel\\')
        # shutil.copy('D:\workspace\python_excel\\' + request.POST['q'], 'D:\workspace\django_excel')
        shutil.copy(request.POST['q'], 'D:\workspace\django_excel')
        Excelfile = open_workbook(request.POST['q'])
        Sheet_name = Excelfile.sheet_names()[0]

        ctx['rlt2']=gain_data(request.POST['q'],Sheet_name)

    return render(request, "excel_show/index.html", ctx)
