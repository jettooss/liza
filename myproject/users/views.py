from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import ClientSerializer ,PersonalDataSerializer,DoctorSerializer



# class ClientList(generics.ListCreateAPIView):
#     queryset = Clients.objects.all()
#     serializer_class = ClientSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Clients.objects.all()
#     serializer_class = ClientSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class DoctorList(generics.ListCreateAPIView):
#     queryset = Doctors.objects.all()
#     serializer_class = DoctorSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except:
#                 return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Doctors.objects.all()
#     serializer_class = DoctorSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# class PersonalDataList(generics.ListCreateAPIView):
#     queryset = Personal_data.objects.all()
#     serializer_class = PersonalDataSerializer

# class PersonalDataDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Personal_data.objects.all()
#     serializer_class = PersonalDataSerializer


from rest_framework import generics, permissions

from rest_framework import generics
from .models import Personal_data, Clients, Doctors
from .serializers import PersonalDataSerializer, ClientSerializer, DoctorSerializer

class PersonalDataList(generics.ListCreateAPIView):
    queryset = Personal_data.objects.all()
    serializer_class = PersonalDataSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


class PersonalDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personal_data.objects.all()
    serializer_class = PersonalDataSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


class ClientList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация


from rest_framework import generics, permissions

class ClientList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication for access

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication for access
    
    def get_object(self):
        """Ensures the user can only access their own client data."""
        obj = super().get_object()
        if obj.personal_data.user != self.request.user:
            raise PermissionDenied("You are not allowed to view this client's data.")
        return obj

 