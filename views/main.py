
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm

import os
from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from app_01 import models






def main_list(request):
    queryset = models.Main.objects.all()
    return render(request, 'main_list.html', {'queryset': queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.Main
        fields = "__all__"


def main_upload(request):
    title = "Add Main Image"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'main_upload.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        form.save()
        return redirect("/main/list/")
    return render(request, 'main_upload.html', {"form": form, 'title': title})

def main_delete(request):
    """ 删除部门 """
    # 获取ID http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')

    # 删除
    models.Main.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/main/list/")