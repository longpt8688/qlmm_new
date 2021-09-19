from django import forms
from QuyTrinhSanXuat.models import GanCongDoan

class GanCongDoanForm(forms.ModelForm):
    class Meta: #De Design lai model co san cuar django
        model = GanCongDoan
        fields = '__all__'

    