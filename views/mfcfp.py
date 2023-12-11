from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm

import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models


#上传区域
def mfcfp_list(request):
    queryset = models.MFCFP.objects.all()
    return render(request, 'mfcfp_list.html', {'queryset': queryset})

class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.MFCFP
        fields = "__all__"

def mfcfp_upload(request):
    title = "Add MFCFP Image"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'mfcfp_upload.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/mfcfp/list/")
    return render(request, 'mfcfp_upload.html', {"form": form, 'title': title})

def mfcfp_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.MFCFP.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/mfcfp/list/")

#绘画区域

def mfcfp_chart(request):
    """ 数据统计页面 """
    return render(request, 'mfcfp_chart.html')


def mfcfp_voltage(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Voltage","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]


    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)


def mfcfp_current(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Current_nA","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]




    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def mfcfp_currentdensity(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Current_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)


def mfcfp_charge(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Charge_nC","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def mfcfp_chargedensity(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Charge_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)

def mfcfp_power(request):
    legend = ["ICP", "Light","Film coating","Textile fiber", "Chemical etch","Gel","Mosaic particle", "Electrospinning","3D printing",]

    a = models.Essay.objects.filter(TENG_MFCFP="ICP") .values_list("Ref_Publication_date_digit","Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    b = models.Essay.objects.filter(TENG_MFCFP="Light").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    c = models.Essay.objects.filter(TENG_MFCFP="Film coating").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    d = models.Essay.objects.filter(TENG_MFCFP="Textile fiber").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    e = models.Essay.objects.filter(TENG_MFCFP="Chemical etch").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    f = models.Essay.objects.filter(TENG_MFCFP="Gel").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    g = models.Essay.objects.filter(TENG_MFCFP="Mosaic particle").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    h = models.Essay.objects.filter(TENG_MFCFP="Electrospinning").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")
    i = models.Essay.objects.filter(TENG_MFCFP="3D printing").values_list("Ref_Publication_date_digit", "Efficiency_Power_modified","TENG_Power_generation_application","TENG_Sensor_field_application","Ref_DOI_number","Ref_Publication_date")

    # c = models.Essay.objects.filter(Efficiency_Voltage__gt=5000)

    # print(c)

    # for obj in c:
    #     print(obj.Ref_Publication_date.strftime('%Y-%m-%d'))

    a1=[list(x) for x in a]
    b1 = [list(x) for x in b]
    c1 = [list(x) for x in c]
    d1 = [list(x) for x in d]
    e1 = [list(x) for x in e]
    f1 = [list(x) for x in f]
    g1 = [list(x) for x in g]
    h1 = [list(x) for x in h]
    i1 = [list(x) for x in i]
    series_list = [
        {
            "name": 'ICP',
            "type": 'scatter',

            "data": a1
        },
        {
            "name": 'Light',
            "type": 'scatter',

            "data":  b1
        },
        {
            "name": 'Film coating',
            "type": 'scatter',

            "data": c1
        },
        {
            "name": 'Textile fiber',
            "type": 'scatter',

            "data": d1
        },
        {
            "name": 'Chemical etch',
            "type": 'scatter',

            "data": e1
        },
        {
            "name": 'Gel',
            "type": 'scatter',

            "data": f1
        },
        {
            "name": 'Mosaic particle',
            "type": 'scatter',

            "data": g1
        },
        {
            "name": 'Electrospinning',
            "type": 'scatter',

            "data": h1
        },
        {
            "name": '3D printing',
            "type": 'scatter',

            "data": i1
        },
    ]
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,

        }
    }
    return JsonResponse(result)



