from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm

import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


#上传区域
def dc_list(request):
    queryset = models.DC.objects.all()
    return render(request, 'dc_list.html', {'queryset': queryset})

class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.DC
        fields = "__all__"

def dc_upload(request):
    title = "Add D-C Image"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'dc_upload.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/dc/list/")
    return render(request, 'dc_upload.html', {"form": form, 'title': title})

def dc_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.DC.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/dc/list/")

#绘画区域

def dc_chart(request):
    """ 数据统计页面 """
    return render(request, 'dc_chart.html')


def dc_voltage(request):
    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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


def dc_current(request):


    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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

def dc_currentdensity(request):

    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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


def dc_charge(request):

    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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

def dc_chargedensity(request):


    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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

def dc_power(request):

    legend = ["Phase coupling", "Dielectric breakdown","Electric brush","Ternary Dielectric Triboelectrification Effect","Semiconductor"]

    a = models.Essay.objects.filter(Mode=5) .values_list("Ref_Publication_date_digit","Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(Mode=6).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(Mode=7).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(Mode=8).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(Mode=9).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

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
            "name": 'Phase coupling',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Dielectric breakdown',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Electric brush',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Ternary Dielectric Triboelectrification Effect',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Semiconductor',
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