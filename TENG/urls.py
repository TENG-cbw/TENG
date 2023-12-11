"""TENG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from app_01.views import essay,chart,main,sl,dc,mfcfp,structure,summary




urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),



    path('essay/list/', essay.essay_list),
    path('essay/add/', essay.essay_add),
    path('essay/delete/', essay.essay_delete),
    path('essay/<int:nid>/edit/', essay.essay_edit),
    path('essay/multi/', essay.essay_multi),

        # main数据统计
    path('chart/list/', chart.chart_list),
    path('chart/highcharts/', chart.chart_highcharts),

    path('chart/line/', chart.chart_line),
    path('chart/level/', chart.chart_level),
    path('chart/powervoltage/', chart.chart_powervoltage),
    path('chart/sensorvoltage/', chart.chart_sensorvoltage),

    path('chart/powercurrent/', chart.chart_powercurrent),
    path('chart/sensorcurrent/', chart.chart_sensorcurrent),
    path('chart/sensorcurrentreal/', chart.chart_sensorcurrentreal),

    path('chart/powercharge/', chart.chart_powercharge),
    path('chart/sensorcharge/', chart.chart_sensorcharge),

    path('chart/powerpower/', chart.chart_powerpower),
    path('chart/sensorpower/', chart.chart_sensorpower),

    path('main/list/', main.main_list),
    path('main/upload/', main.main_upload),
    path('main/delete/', main.main_delete),
    # Summary数据统计
    path('summary/chart/', summary.summary_chart),
    path('summary/voltage/', summary.summary_voltage),
    path('summary/current/', summary.summary_current),
    path('summary/currentdensity/', summary.summary_currentdensity),
    path('summary/charge/', summary.summary_charge),
    path('summary/chargedensity/', summary.summary_chargedensity),
    path('summary/power/', summary.summary_power),
        # S-L数据统计
    path('sl/chart/', sl.sl_chart),
    path('sl/voltage/', sl.sl_voltage),
    path('sl/current/', sl.sl_current),
    path('sl/currentdensity/', sl.sl_currentdensity),
    path('sl/charge/', sl.sl_charge),
    path('sl/chargedensity/', sl.sl_chargedensity),
    path('sl/power/', sl.sl_power),

    path('sl/list/', sl.sl_list),
    path('sl/upload/', sl.sl_upload),
    path('sl/delete/', sl.sl_delete),

    # D-C数据统计
    path('dc/chart/', dc.dc_chart),
    path('dc/voltage/', dc.dc_voltage),
    path('dc/current/', dc.dc_current),
    path('dc/currentdensity/', dc.dc_currentdensity),
    path('dc/charge/', dc.dc_charge),
    path('dc/chargedensity/', dc.dc_chargedensity),
    path('dc/power/', dc.dc_power),

    path('dc/list/', dc.dc_list),
    path('dc/upload/', dc.dc_upload),
    path('dc/delete/', dc.dc_delete),

    # MFCFP数据统计
    path('mfcfp/chart/', mfcfp.mfcfp_chart),
    path('mfcfp/voltage/', mfcfp.mfcfp_voltage),
    path('mfcfp/current/', mfcfp.mfcfp_current),
    path('mfcfp/currentdensity/', mfcfp.mfcfp_currentdensity),
    path('mfcfp/charge/', mfcfp.mfcfp_charge),
    path('mfcfp/chargedensity/', mfcfp.mfcfp_chargedensity),
    path('mfcfp/power/', mfcfp.mfcfp_power),

    path('mfcfp/list/', mfcfp.mfcfp_list),
    path('mfcfp/upload/', mfcfp.mfcfp_upload),
    path('mfcfp/delete/', mfcfp.mfcfp_delete),


    # Structure数据统计
    path('structure/chart/', structure.structure_chart),
    path('structure/voltage/', structure.structure_voltage),
    path('structure/current/', structure.structure_current),
    path('structure/currentdensity/', structure.structure_currentdensity),
    path('structure/charge/', structure.structure_charge),
    path('structure/chargedensity/', structure.structure_chargedensity),
    path('structure/power/', structure.structure_power),


    path('structure/list/', structure.structure_list),
    path('structure/upload/', structure.structure_upload),
    path('structure/delete/', structure.structure_delete),
]