from rest_framework import serializers
from .models import Personal_data, Clients, Doctors
from django.db import transaction








# class PersonalDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Personal_data
#         fields = '__all__'

# class ClientSerializer(serializers.ModelSerializer):
#     personal_data = PersonalDataSerializer()

#     class Meta:
#         model = Clients
#         fields = '__all__'

#     def create(self, validated_data):
#             personal_data_data = validated_data.pop('personal_data')
#             full_name = f"{personal_data_data.get('name')} {personal_data_data.get('surname')}"
            
#             with transaction.atomic():
#                 # Check if there is any Client with the same name and surname in Personal_data
#                 if Clients.objects.filter(personal_data__name=personal_data_data.get('name'), personal_data__surname=personal_data_data.get('surname')).exists():
#                     raise serializers.ValidationError('A Client with the same name and surname already exists.')
                
#                 personal_data = Personal_data.objects.create(**personal_data_data)
#                 return Clients.objects.create(personal_data=personal_data, **validated_data)


#     def update(self, instance, validated_data):
#         personal_data_data = validated_data.pop('personal_data')
#         personal_data = instance.personal_data

#         instance.save()

#         for attr, value in personal_data_data.items():
#             setattr(personal_data, attr, value)
#         personal_data.save()

#         return instance

# class DoctorSerializer(serializers.ModelSerializer):
#     personal_data = PersonalDataSerializer()

#     class Meta:
#         model = Doctors
#         fields = '__all__'

#     def create(self, validated_data):
#             personal_data_data = validated_data.pop('personal_data')
#             full_name = f"{personal_data_data.get('name')} {personal_data_data.get('surname')}"
            
#             with transaction.atomic():
#                 # Check if there is any Doctor with the same name and surname in Personal_data
#                 if Doctors.objects.filter(personal_data__name=personal_data_data.get('name'), personal_data__surname=personal_data_data.get('surname')).exists():
#                     raise serializers.ValidationError('A Doctor with the same name and surname already exists.')
                
#                 personal_data = Personal_data.objects.create(**personal_data_data)

#                 return Doctors.objects.create(personal_data=personal_data, **validated_data)
#     def update(self, instance, validated_data):
#         personal_data_data = validated_data.pop('personal_data')
#         personal_data = instance.personal_data

#         instance.save()

#         for attr, value in personal_data_data.items():
#             setattr(personal_data, attr, value)
#         personal_data.save()

#         return instance


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class PersonalDataSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Personal_data
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        personal_data = Personal_data.objects.create(user=user, **validated_data)
        return personal_data

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        user = instance.user

        if user_data is not None:
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class ClientSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer()

    class Meta:
        model = Clients
        fields = '__all__'

    def create(self, validated_data):
        personal_data_data = validated_data.pop('personal_data')
        personal_data = PersonalDataSerializer.create(PersonalDataSerializer(), validated_data=personal_data_data)
        return Clients.objects.create(personal_data=personal_data, **validated_data)

    # Update method remains similar, ensuring it uses the updated PersonalDataSerializer methods.

class DoctorSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer()

    class Meta:
        model = Doctors
        fields = '__all__'

    def create(self, validated_data):
        personal_data_data = validated_data.pop('personal_data')
        personal_data = PersonalDataSerializer.create(PersonalDataSerializer(), validated_data=personal_data_data)
        return Doctors.objects.create(personal_data=personal_data, **validated_data)

 