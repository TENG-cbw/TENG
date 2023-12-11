from django.db import models

# Create your models here.

class Essay(models.Model):


    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date[year:mm:dd]")
    Ref_Publication_date_digit=models.DecimalField(verbose_name="Ref.Publication date(Digit)", max_digits=10, decimal_places=4, default=0)
    Ref_Article_title=models.CharField(verbose_name="Ref.Article title",max_length=255)
    Ref_Journal=models.CharField(verbose_name="Ref.Journal", max_length=64)
    Ref_First_author= models.CharField(verbose_name="Ref.First author", max_length=64)
    Ref_Corresponding_author=models.CharField(verbose_name="Ref.Corresponding author", max_length=64)
    Ref_DOI_number=models.CharField(verbose_name="Ref.DOI number", max_length=64)



    TENG_MFCFP = models.CharField(verbose_name="TENG.MFCFP", max_length=255)

    TENG_structure_choices = (
        (1, "Basic"),
        (2, "Machine"),
        (3, "IMTRM"),
        (4, "Nothing"),
    )
    TENG_structure = models.SmallIntegerField(verbose_name="TENG.structure", choices=TENG_structure_choices,default=1)

    Structure_choices = (
        (1, "Spring"),
        (2, "Sandwich"),
        (3, "Roll"),
        (4, "Rotation"),
        (5, "Line"),
        (6, "Gear"),
        (7, "Ratchet"),
        (8, "Rod"),
        (9, "Bearing"),
        (10, "Beam"),
        (11, "Folding"),
        (12, "Wind"),
        (13, "Origami"),
        (14, "Softness"),
        (15, "Textile"),
        (16, "Water droplet"),
        (17, "Nothing"),
    )
    Structure = models.SmallIntegerField(verbose_name="Specific structure", choices=Structure_choices,default=1)

    TENG_Mode_choices = (
        (1, "TM"),
        (2, "DC"),
        (3, "SL"),
    )
    TENG_Mode = models.SmallIntegerField(verbose_name="TENG.Mode", choices=TENG_Mode_choices,default=1)
    Mode_choices = (
        (1, "Contact separation"),
        (2, "Horizontal slide"),
        (3, "Single electrode"),
        (4, "Independent layer"),
        (5, "Phase coupling"),
        (6, "Dielectric breakdown"),
        (7, "Electric brush"),
        (8, "Ternary Dielectric Triboelectrification Effect"),
        (9, "Semiconductor"),
        (10, "Single"),
        (11, "Contact"),
        (12, "Non-Contact"),
        (13, "Semiconductor-Metal"),
    )
    Mode = models.SmallIntegerField(verbose_name="Specific mode", choices=Mode_choices,default=1)


    Mode_Loss_electrons_Electrode_layer=models.CharField(verbose_name="Mode.Loss electrons.Electrode layer", max_length=255)
    Mode_Loss_electrons_layer=models.CharField(verbose_name="Mode.Loss electrons layer", max_length=255)
    Mode_Get_electrons_layer=models.CharField(verbose_name="Mode.Get electrons layer", max_length=255)
    Mode_Get_electrons_layer_Electrode_layer=models.CharField(verbose_name="Mode.Get electrons layer.Electrode layer", max_length=255)


    TENG_Power_generation_application=models.CharField(verbose_name="TENG.Power generation.application", max_length=255)
    TENG_Sensor_field_application=models.CharField(verbose_name="TENG.Sensor field.application", max_length=255)


    Efficiency_Voltage=models.DecimalField(verbose_name="Efficiency.Voltage(V)", max_digits=10, decimal_places=4, default=0)

    Efficiency_Current=models.CharField(verbose_name="Efficiency.Current(Input)", max_length=64)
    Efficiency_Current_nA=models.DecimalField(verbose_name="Efficiency.Current modified(nA)", max_digits=10, decimal_places=4, default=0)
    Efficiency_Current_modified=models.DecimalField(verbose_name="Efficiency.Current modified(μA/cm2)", max_digits=10, decimal_places=4, default=0)

    Efficiency_Charge=models.CharField(verbose_name="Efficiency.Charge(Input)", max_length=64)
    Efficiency_Charge_nC=models.DecimalField(verbose_name="Efficiency.Charge(nC)", max_digits=10, decimal_places=4, default=0)
    Efficiency_Charge_modified=models.DecimalField(verbose_name="Efficiency.Charge modified(μC/m2)", max_digits=10, decimal_places=4, default=0)

    Efficiency_Power=models.CharField(verbose_name="Efficiency.Power(Input)", max_length=64)
    Efficiency_Power_modified=models.DecimalField(verbose_name="Efficiency.Power modified(W/m2)", max_digits=10, decimal_places=4, default=0)
    Efficiency_Resistance=models.DecimalField(verbose_name="Efficiency.Resistance(MΩ)", max_digits=10, decimal_places=4, default=0)
    Efficiency_Area=models.DecimalField(verbose_name="Efficiency.Area(cm2)", max_digits=10, decimal_places=4, default=0)
    Level_choices = (
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****"),
    )
    Level = models.SmallIntegerField(verbose_name="Level", choices=Level_choices)





class Main(models.Model):
    """ Main """
    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date")
    DOI = models.CharField(verbose_name="DOI", max_length=64)
    Application= models.CharField(verbose_name="Application", max_length=64)


    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Image", max_length=128, upload_to='main/')


class SL(models.Model):
    """ 固液 """
    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date")
    DOI = models.CharField(verbose_name="DOI", max_length=64)


    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Image", max_length=128, upload_to='sl/')


class DC(models.Model):
    """ 直流 """
    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date")
    DOI = models.CharField(verbose_name="DOI", max_length=64)


    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Image", max_length=128, upload_to='dc/')

class MFCFP(models.Model):
    """ 改变摩擦性质的方法 """
    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date")
    DOI = models.CharField(verbose_name="DOI", max_length=64)


    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Image", max_length=128, upload_to='mfcfp/')


class Structure(models.Model):
    """ 结构 """
    Ref_Publication_date = models.DateField(verbose_name="Ref.Publication date")
    DOI = models.CharField(verbose_name="DOI", max_length=64)


    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Image", max_length=128, upload_to='structure/')