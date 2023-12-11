from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm
from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


def chart_list(request):
    """ 数据统计页面 """
    return render(request, 'chart_list.html')

#这是文章和专利的有关teng的数量图
def chart_line(request):
    result = {
        "status": True
        # "data": {
        #     'data0': data0,
        #     'data1': data1,

        # }
    }
    return JsonResponse(result)

def chart_level(request):
    legend = ["TENG*", "TENG**","TENG***","TENG****","TENG*****"]

    a = models.Essay.objects.filter(Level=1) .values_list("Ref_Publication_date_digit","Level","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Level=2).values_list("Ref_Publication_date_digit", "Level","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Level=3).values_list("Ref_Publication_date_digit", "Level","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Level=4).values_list("Ref_Publication_date_digit", "Level","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Level=5).values_list("Ref_Publication_date_digit", "Level","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]



    series_list = [
        {
            "name": 'TENG*',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'TENG**',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'TENG***',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'TENG****',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'TENG*****',
            "type": 'scatter',

            "data": e1
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


#这是teng传感器电压图
def chart_sensorvoltage(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Sensor_field_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)


#这是teng发电机电压图

def chart_powervoltage(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Power_generation_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng发电机电流密度图
def chart_powercurrent(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Power_generation_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Power_generation_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng传感器电流密度图

def chart_sensorcurrent(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Sensor_field_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng传感器电流图

def chart_sensorcurrentreal(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Sensor_field_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Current_nA","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)
#这是teng发电机电荷
def chart_powercharge(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Power_generation_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Power_generation_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng传感器电荷密度图

def chart_sensorcharge(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Sensor_field_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng发电机功率
def chart_powerpower(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Power_generation_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Power_modified","TENG_Power_generation_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

#这是teng传感器功率

def chart_sensorpower(request):

    # a = models.Essay.objects.filter(Efficiency_Voltage__lt=5000) .values_list("Ref_Publication_date_digit","Efficiency_Voltage")
    c = models.Essay.objects.exclude(TENG_Sensor_field_application__in=["Nothing"]).values_list("Ref_Publication_date_digit","Efficiency_Power_modified","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    b=[list(x) for x in c]


    data=b

    result = {
        "data":data,
        "status": True,

    }
    return JsonResponse(result)

def chart_highcharts(request):

    return render(request,'chart_highcharts.html')