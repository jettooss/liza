
from django.urls import path
from .views import ClientList, ClientDetail, DoctorList, DoctorDetail
from .views import PersonalDataList, PersonalDataDetail
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)
urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('personal-data/', PersonalDataList.as_view(), name='personal-data-list'),
    path('personal-data/<int:pk>/', PersonalDataDetail.as_view(), name='personal-data-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
  
