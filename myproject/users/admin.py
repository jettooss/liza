from django.contrib import admin
from .models import Clients, Doctors,Personal_data
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError


class ClientsAdminForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

    def clean_personal_data(self):
        personal_data = self.cleaned_data['personal_data']
        if Doctors.objects.filter(personal_data=personal_data).exists():
            raise ValidationError("This Personal_data instance is already linked to a Doctor.")
        return personal_data

class DoctorsAdminForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'

    def clean_personal_data(self):
        personal_data = self.cleaned_data['personal_data']
        if Clients.objects.filter(personal_data=personal_data).exists():
            raise ValidationError("This Personal_data instance is already linked to a Client.")
        return personal_data
    

@admin.register(Personal_data)
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date_of_birth', 'number_phone','pk')
 
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    form = ClientsAdminForm
    list_display = ('get_name','get_number','pk')

    def get_name(self, obj):
        return obj.personal_data.name
    get_name.short_description = 'Name'

    def get_number(self, obj):
        return obj.personal_data.number_phone
    get_number.short_description = 'Number phone'

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    form = DoctorsAdminForm
    list_display = ('get_name',"pk")

    def get_name(self, obj):
        return obj.personal_data.name
    get_name.short_description = 'Name'