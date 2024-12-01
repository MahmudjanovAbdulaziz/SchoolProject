from django.urls import path

from .views import *


urlpatterns = [
    path("api/v1/EventsList", EventsViews.as_view()),
    path("api/v1/SchoolCharectersCountList", School_charecters_countViews.as_view()),
    path("api/v1/TeachersList", TeachersViews.as_view()),
    path("api/v1/GalleryList", GalleryViews.as_view()),
    path("api/v1/OurGraduatesList", Our_graduatesViews.as_view()),
]
