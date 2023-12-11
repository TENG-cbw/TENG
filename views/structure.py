from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm

import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


#上传区域
def structure_list(request):
    queryset = models.Structure.objects.all()
    return render(request, 'structure_list.html', {'queryset': queryset})

class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.Structure
        fields = "__all__"

def structure_upload(request):
    title = "Add Structure Image"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'structure_upload.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/structure/list/")
    return render(request, 'structure_upload.html', {"form": form, 'title': title})

def structure_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.Structure.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/structure/list/")

#绘画区域

def structure_chart(request):
    """ 数据统计页面 """
    return render(request, 'structure_chart.html')


def structure_voltage(request):
    legend = ["Basic", "Machine","IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1) .values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]




    series_list = [
        {
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'IMTRM',
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


def structure_current(request):
    legend = ["Basic", "Machine", "IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Current_nA",
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
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'IMTRM',
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

def structure_currentdensity(request):
    legend = ["Basic", "Machine", "IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Current_modified",
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
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'IMTRM',
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


def structure_charge(request):
    legend = ["Basic", "Machine", "IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC",
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
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'IMTRM',
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

def structure_chargedensity(request):
    legend = ["Basic", "Machine", "IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified",
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
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'IMTRM',
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

def structure_power(request):
    legend = ["Basic", "Machine", "IMTRM"]

    a = models.Essay.objects.filter(TENG_structure=1).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_structure=2).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
                                                                  "TENG_Power_generation_application",
                                                                  "TENG_Sensor_field_application", "Ref_DOI_number",
                                                                  "Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_structure=3).values_list("Ref_Publication_date_digit", "Efficiency_Power_modified",
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
            "name": 'Basic',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Machine',
            "type": 'scatter',

            "data": b1
        },
        {
            "name": 'IMTRM',
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