from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm

import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


#上传区域


def summary_chart(request):
    """ 数据统计页面 """
    return render(request, 'structure_chart.html')


def summary_voltage(request):
    legend = ["TM", "DC","SL"]

    a = models.Essay.objects.filter(TENG_Mode=1) .values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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


def summary_current(request):



    legend = ["TM", "DC","SL"]

    a = models.Essay.objects.filter(TENG_Mode=1) .values_list("Ref_Publication_date_digit","Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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

def summary_currentdensity(request):


    legend = ["TM", "DC","SL"]

    a = models.Essay.objects.filter(TENG_Mode=1) .values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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


def summary_charge(request):



    legend = ["TM", "DC","SL"]

    a = models.Essay.objects.filter(TENG_Mode=1) .values_list("Ref_Publication_date_digit","Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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

def summary_chargedensity(request):



    legend = ["TM", "DC","SL"]

    a = models.Essay.objects.filter(TENG_Mode=1) .values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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

def summary_power(request):



    legend = ["TM", "DC", "SL"]

    a = models.Essay.objects.filter(TENG_Mode=1).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
                                                             "TENG_Power_generation_application",
                                                             "TENG_Sensor_field_application", "Ref_DOI_number",
                                                             "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_Mode=2).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
                                                             "TENG_Power_generation_application",
                                                             "TENG_Sensor_field_application", "Ref_DOI_number",
                                                             "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_Mode=3).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
                                                             "TENG_Power_generation_application",
                                                             "TENG_Sensor_field_application", "Ref_DOI_number",
                                                             "Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1 = [list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]

    series_list = [
        {
            "name": 'TM',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'DC',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'SL',
            "type": 'scatter',

            "data": c1
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