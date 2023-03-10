from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from home.models import Emp
from home.Empserializer import EmpSerializer
from home.Empviewset import EmpViewset
router = routers.DefaultRouter()
router.register(r'emps', EmpViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
