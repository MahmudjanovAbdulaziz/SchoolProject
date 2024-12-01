from django.shortcuts import render
from rest_framework import generics


from .serializer import *
from .models import *
from django.http import HttpResponse


class EventsViews(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class School_charecters_countViews(generics.ListAPIView):
    queryset = School_cherecters_count.objects.all()
    serializer_class = School_cherecters_countSerializer


class TeachersViews(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


class GalleryViews(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class Our_graduatesViews(generics.ListAPIView):
    queryset = Our_graduates.objects.all()
    serializer_class = Our_graduatesSerializer
