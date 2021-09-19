from django.shortcuts import render
from django.views.generic import CreateView
from QuyTrinhSanXuat.models import GanCongDoan
from QuyTrinhSanXuat.forms import GanCongDoanForm
# Create your views here.from django import forms



class TaoSanPham(CreateView):
    model = GanCongDoan
    form_class = GanCongDoanForm
    template_name = 'admin/qlmm/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaoSanPham, self).get_context_data(*args, **kwargs)
        context['tatcasanpham'] = GanCongDoan.objects.all()
        return context

