from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm
from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


#上传区域
def sl_list(request):
    queryset = models.SL.objects.all()

    return render(request, 'sl_list.html', {'queryset': queryset})

class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.SL
        fields = "__all__"

def sl_upload(request):
    title = "Add S-L Image"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'sl_upload.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/sl/list/")
    return render(request, 'sl_upload.html', {"form": form, 'title': title})
def sl_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.SL.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/sl/list/")

#绘画区域

def sl_chart(request):
    """ 数据统计页面 """
    return render(request, 'sl_chart.html')


def sl_voltage(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)


def sl_current(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def sl_currentdensity(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)


def sl_charge(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def sl_chargedensity(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def sl_power(request):
    legend = ["Single", "Contact","Non-Contact","Semiconductor-Metal"]

    a = models.Essay.objects.filter(Mode=10) .values_list("Ref_Publication_date_digit","Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=11).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=12).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=13).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]



    series_list = [
        {
            "name": 'Single',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Contact',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Non-Contact',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Semiconductor-Metal',
            "type": 'scatter',

            "data": d1
        }
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)