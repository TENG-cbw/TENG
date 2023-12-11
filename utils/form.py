from app_01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app_01.utils.bootstrap import BootStrapModelForm





class EssayModelForm(BootStrapModelForm):
    # 验证：方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    # )

    class Meta:
        model = models.Essay
        # fields = "__all__" 意思是所有的字段
        # exclude = ['level']排除level
        fields = ['Ref_Publication_date','Ref_Publication_date_digit','Ref_Article_title', 'Ref_Journal', 'Ref_First_author','Ref_Corresponding_author','Ref_DOI_number',
                  'TENG_MFCFP','TENG_structure','Structure','TENG_Mode','Mode',
                  'Mode_Loss_electrons_Electrode_layer', 'Mode_Loss_electrons_layer', 'Mode_Get_electrons_layer','Mode_Get_electrons_layer_Electrode_layer',
                  'TENG_Power_generation_application', 'TENG_Sensor_field_application',"Efficiency_Voltage",
                  'Efficiency_Current', 'Efficiency_Current_nA', 'Efficiency_Current_modified',
                  'Efficiency_Charge','Efficiency_Charge_nC','Efficiency_Charge_modified',
                  'Efficiency_Power', 'Efficiency_Power_modified',
                  'Efficiency_Resistance', 'Efficiency_Area','Level']

    # 验证：方式2
    def clean_mobile(self):
        txt_Ref_DOI_number = self.cleaned_data["Ref_DOI_number"]

        exists = models.Essay.objects.filter(Ref_DOI_number=txt_Ref_DOI_number).exists()
        if exists:
            raise ValidationError("已存在")

        # 验证通过，用户输入的值返回
        return txt_Ref_DOI_number


class EssayEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    # )

    class Meta:
        model = models.Essay
        fields = ['Ref_Publication_date','Ref_Publication_date_digit','Ref_Article_title', 'Ref_Journal', 'Ref_First_author','Ref_Corresponding_author','Ref_DOI_number',
                  'TENG_MFCFP','TENG_structure','Structure','TENG_Mode','Mode',
                  'Mode_Loss_electrons_Electrode_layer', 'Mode_Loss_electrons_layer', 'Mode_Get_electrons_layer','Mode_Get_electrons_layer_Electrode_layer',
                  'TENG_Power_generation_application', 'TENG_Sensor_field_application',"Efficiency_Voltage",
                  'Efficiency_Current', 'Efficiency_Current_nA', 'Efficiency_Current_modified',
                  'Efficiency_Charge','Efficiency_Charge_nC','Efficiency_Charge_modified',
                  'Efficiency_Power', 'Efficiency_Power_modified',
                  'Efficiency_Resistance', 'Efficiency_Area','Level']

    # 验证：方式2
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        # print(self.instance.pk)
        txt_Ref_DOI_number = self.cleaned_data["Ref_DOI_number"]
        exists = models.Essay.objects.exclude(id=self.instance.pk).filter(Ref_DOI_number=txt_Ref_DOI_number).exists()
        if exists:
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_Ref_DOI_number
