from django.urls import path
from .views import (
    UniversityListView, ProgramListCreateView, BranchListCreateView,
    CourseListCreateView, ProgramStructureListCreateView
)


urlpatterns = [
    path('universities/', UniversityListView.as_view(), name='university-list'),
    path('programs/', ProgramListCreateView.as_view(), name='program-list'),
    path('branches/', BranchListCreateView.as_view(), name='branch-list'),
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('program-structures/', ProgramStructureListCreateView.as_view(), name='program-structure-list'),
]