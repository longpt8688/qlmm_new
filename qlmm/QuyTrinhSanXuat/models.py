from django.db.models.deletion import CASCADE
from sanxuat.models import SanPham
from django.db import models
from sanxuat.models import *
from django.urls import reverse

class GanCongDoan(models.Model):
    TenSanPham = models.ForeignKey(SanPham, on_delete=CASCADE)
    CongDoan = models.ManyToManyField(CongDoan)

    def get_absolute_url(self):
        return reverse("quytrinhsanxuat:tao-san-pham")

    def __str__(self):
        return str(self.TenSanPham) + " " + str(self.CongDoan)
    
    
# Create your models here.

