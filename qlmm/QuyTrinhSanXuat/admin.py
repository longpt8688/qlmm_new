from django.contrib import admin
from QuyTrinhSanXuat.models import GanCongDoan
from QuyTrinhSanXuat.forms import GanCongDoanForm
# Register your models here.


# @admin.register(GanCongDoan)
class GanCongDoanAdmin(admin.ModelAdmin):
    model = GanCongDoan

    def has_module_permission(self,request):
        return True

    def has_module_perms(self, user_obj, perm, obj=None):
        return True
    
# admin.site.unregister(GanCongDoan)
admin.site.register(GanCongDoan, GanCongDoanAdmin)