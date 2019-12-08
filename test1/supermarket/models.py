from django.db import models
# 表单，用于构造表单，当表单的内容与models相差较大时
from django import forms
# 模型表单，用于构造表单，当表单的内容与models基本一致时
from django.forms import ModelForm
# Create your models here.


class Employee(models.Model):
    employee_account = models.CharField(max_length=20, primary_key=True)
    employee_password = models.CharField(max_length=20, null=False)
    authority = models.CharField(max_length=4, null=True)


class salary(models.Model):
    gongzitiaomu_id = models.CharField(max_length=20, primary_key=True)
    shijian = models.DateField(null=True)
    jichugongzi = models.FloatField()
    jixiao = models.FloatField()
    chuqin = models.FloatField()
    weigui = models.FloatField()
    shuijin = models.FloatField()

    def __str__(self):
        return str(self.gongzitiaomu_id)


class salary_summary(models.Model):
    """准备把工资的外键设置为employee的主键"""
    gongzitiaomu_id = models.CharField(max_length=20)
    shijian = models.DateField(null=True)
    jichugongzi = models.FloatField()
    jixiao = models.FloatField()
    chuqin = models.FloatField()
    weigui = models.FloatField()
    shuijin = models.FloatField()
    belong = models.ForeignKey(Employee, related_name='gongzis', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gongzitiaomu_id)

    class Meta:
        unique_together = ('gongzitiaomu_id', 'shijian')


class jingli(models.Model):
    jingli_id = models.CharField(primary_key=True, max_length=20)
    jingli_name = models.CharField(max_length=100)
    jingli_sex = models.CharField(max_length=4)
    jingli_birth = models.DateField()
    jingli_salary = models.FloatField()
    employee_status = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.jingli_id)


class liansuodian(models.Model):
    liansuodian_id = models.CharField(max_length=20, primary_key=True)
    weizhi_liansuodian = models.CharField(max_length=100)
    liansuodian_phone = models.CharField(max_length=15)
    jingli = models.ForeignKey(jingli, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.liansuodian_id)


class shouyinyuan(models.Model):
    shouyinyuan_id = models.CharField(primary_key=True, max_length=20)
    shouyinyuan_name = models.CharField(max_length=100)
    shouyinyuan_sex = models.CharField(max_length=4)
    shouyinyuan_birth = models.DateField()
    employee_status = models.OneToOneField(Employee, on_delete=models.CASCADE)
    belong = models.ForeignKey(liansuodian, on_delete=models.CASCADE)


class caigouyuan(models.Model):
    caigouyuan_id = models.CharField(max_length=20, primary_key=True)
    caigouyuan_name = models.CharField(max_length=100)
    caigouyuan_sex = models.CharField(max_length=4)
    caigouyuan_birth = models.DateField()
    employee_status = models.OneToOneField(Employee, on_delete=models.CASCADE)
    belong = models.ForeignKey(liansuodian, on_delete=models.CASCADE)


class huojia(models.Model):
    huojia_id = models.CharField(primary_key=True, max_length=20)
    xiangduiweizhi_huojia = models.CharField(max_length=50)
    liansuodian = models.ForeignKey(liansuodian, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.huojia_id)


class zhekou(models.Model):
    zhekoutiaomu_id = models.CharField(primary_key=True, max_length=20)
    discount = models.FloatField(null=True)

    def __str__(self):
        return str(self.zhekoutiaomu_id)


class Lei(models.Model):
    cls_id = models.CharField(max_length=20, default='lei_13130')
    shangpin_id = models.CharField(max_length=20)
    length = models.CharField(max_length=8, null=True)
    for_sex = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=10, null=True)
    materials = models.CharField(max_length=50, null=True)

    class Meta:
        managed = True
        unique_together = (('cls_id', 'shangpin_id'),)

    def __str__(self):
        return str(self.cls_id)


class shangpin(models.Model):
    changjia_shangpin = models.CharField(max_length=50)
    shangpinming_shangpin = models.CharField(max_length=100)
    huojia_id = models.ManyToManyField(huojia)
    danjia = models.FloatField()
    baozhiqi = models.FloatField()
    zhekou = models.ForeignKey(zhekou, on_delete=models.CASCADE)
    # 联合主键的设置

    class Meta:
        unique_together = ("changjia_shangpin", "shangpinming_shangpin")

    def __str__(self):
        return str(self.changjia_shangpin)+' '+str(self.shangpinming_shangpin)


class shangpin_online(models.Model):
    changjia_shangpin_online = models.CharField(max_length=50)
    shangpinming_shangpin_online = models.CharField(max_length=100)
    danjia = models.FloatField()
    baozhiqi = models.FloatField()
    zhekou = models.ForeignKey(zhekou, on_delete=models.CASCADE)

    # 联合主键的设置

    class Meta:
        unique_together = ("changjia_shangpin_online", "shangpinming_shangpin_online")

    def __str__(self):
        return str(self.changjia_shangpin_online) + ' ' + str(self.shangpinming_shangpin_online)


class shangpin_id_set(models.Model):
    shangpin_id = models.CharField(max_length=20, primary_key=True)
    shangpinming_set = models.ForeignKey(shangpin, on_delete=models.CASCADE)
    # 设置联合主键则这里只需要这样做，因为会自动找到联合的主键
    # changjia_set=models.ForeignKey(shangpin,on_delete=models.CASCADE)
    shengchanriqi = models.DateField()
    # 其实这个标志位可以进行设置，售出，待售，下单中等状态，但是太麻烦了，算了
    is_sold = models.CharField(max_length=4, null=True)
    # fenlei = models.ForeignKey(Lei, on_delete=models.CASCADE)


class jinhuodan(models.Model):
    jinghuodan_id = models.CharField(max_length=20, primary_key=True)
    huowu_set = models.TextField()
    shijian_jinhuodan = models.DateTimeField()


class huowu(models.Model):
    changjia_huowu = models.CharField(max_length=50)
    huowuming_huowu = models.CharField(max_length=100)
    jinghuodan = models.ForeignKey(jinhuodan, null=True, blank=True, on_delete=models.SET_NULL, related_name='rely_to_jinhuodan')
    jinjia_huowu = models.FloatField()

    class Meta:
        unique_together = ("changjia_huowu", "huowuming_huowu")


class huowu_id_set(models.Model):
    huowu_id = models.CharField(max_length=20, primary_key=True)
    huowu_ming_id_set = models.ForeignKey(huowu, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.huowu_id)


class cangku(models.Model):
    cangku_id = models.CharField(primary_key=True, max_length=20)
    weizhi_cangku = models.CharField(max_length=100)
    cangku_phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.cangku_id)


class user(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)
    shenfenzheng = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    xiaofei = models.FloatField(null=True)


class comment(models.Model):
    comment_id = models.CharField(max_length=20, primary_key=True)
    shijian_comment = models.DateTimeField()
    belong_user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return str(self.comment_id)


class vip(models.Model):
    vip_id = models.CharField(max_length=20, primary_key=True)
    vip_level = models.IntegerField()
    # 用于反向查询
    yonghu = models.OneToOneField(user, on_delete=models.CASCADE, related_name='user_vip')

    def __str__(self):
        return str(self.vip_id)


class zhangdan(models.Model):
    zhangdan_id = models.CharField(max_length=20, primary_key=True)
    shijian_zhangdan = models.DateField()
    # 这里的related_name用于反向查询，即通过父表查询子表
    liansuodian = models.ForeignKey(liansuodian, on_delete=models.CASCADE, related_name='zhangdans')
    xiaoshoue = models.FloatField(null=True)

    def __str__(self):
        return str(self.zhangdan_id)
    # 此乃新增的但是没有应用
    class Meta:
        unique_together = ("zhangdan_id", "liansuodian")


class dingdan(models.Model):
    dingdan_id = models.CharField(max_length=20, primary_key=True)
    digndan_time = models.DateTimeField()
    shangpin_set_dingdan = models.TextField(max_length=200)
    yonghu = models.ForeignKey(user, null=True, blank=True, on_delete=models.CASCADE)
    # 用于反向查询
    zhangdan = models.ForeignKey(zhangdan, on_delete=models.CASCADE, related_name='dingdans')
    zongjia_dingdan = models.FloatField()

    def __str__(self):
        return str(self.dingdan_id)


class qingdan(models.Model):
    qingdan_id=models.CharField(max_length=20, primary_key=True)
    shouyinyuan=models.ForeignKey(shouyinyuan, null=True, blank=True, on_delete=models.SET_NULL)
    zhangdan=models.ForeignKey(zhangdan, null=True, blank=True, on_delete=models.SET_NULL)
    zongjia_qingdan=models.FloatField()
    shangpin_set_qingdan=models.TextField()
    shijian_qingdan=models.DateTimeField()

    def __str__(self):
        return str(self.qingdan_id)


class electrical(models.Model):
    elec_id = models.CharField(max_length=50, primary_key=True)
    I_A_in = models.FloatField()
    I_B_in = models.FloatField()
    I_C_in = models.FloatField()
    I_A_out = models.FloatField()
    I_B_out = models.FloatField()
    I_C_out = models.FloatField()
    U_A = models.FloatField()
    U_B = models.FloatField()
    U_C = models.FloatField()

    def __str__(self):
        return str(self.elec_id)
