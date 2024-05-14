from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Personal_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="Phone number must be entered in the format: '99999999999'. Up to 11 digits allowed.")
    number_phone = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.surname}"


class Clients(models.Model):
    personal_data = models.OneToOneField(Personal_data, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.personal_data.name

    def save(self, *args, **kwargs):
        if Doctors.objects.filter(personal_data=self.personal_data).exists():
            raise ValidationError("This Personal_data instance is already linked to a Doctor.")
        super().save(*args, **kwargs)


class Doctors(models.Model):
    personal_data = models.OneToOneField(Personal_data, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='doctors_avatars/', null=True, blank=True)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.personal_data.name

    def save(self, *args, **kwargs):
        if Clients.objects.filter(personal_data=self.personal_data).exists():
            raise ValidationError("This Personal_data instance is already linked to a Client.")
        super(Doctors, self).save(*args, **kwargs)