from django.contrib import admin

from . import models as test_models
# Register your models here.


admin.site.register(test_models.caigouyuan)
admin.site.register(test_models.cangku)
admin.site.register(test_models.dingdan)
admin.site.register(test_models.huojia)
admin.site.register(test_models.huowu)
admin.site.register(test_models.jingli)
admin.site.register(test_models.jinhuodan)
admin.site.register(test_models.liansuodian)

admin.site.register(test_models.qingdan)
admin.site.register(test_models.salary)
admin.site.register(test_models.shangpin)
admin.site.register(test_models.shangpin_id_set)
admin.site.register(test_models.shouyinyuan)
admin.site.register(test_models.user)
admin.site.register(test_models.vip)
admin.site.register(test_models.zhekou)
admin.site.register(test_models.zhangdan)
