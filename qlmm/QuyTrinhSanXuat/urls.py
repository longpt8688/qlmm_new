from django.urls import path
from . import views

app_name = 'quytrinhsanxuat'

urlpatterns = [
    path('tao/', views.TaoSanPham.as_view(), name='tao-san-pham'),
]