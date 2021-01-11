from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .permissions import PermissionsClass
from .serializer import HealthSerializer
from .models import Health

# Create your views here.


class HealthListView(ListAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes=(PermissionsClass,)


class HealthDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes=(PermissionsClass,)
