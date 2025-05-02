from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import University, Program, Branch, Course, ProgramStructure
from .serializers import (
    UniversitySerializer, ProgramSerializer, BranchSerializer,
    CourseSerializer, ProgramStructureSerializer
)


class UniversityListView(generics.ListAPIView):
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip()
        if query:
            return University.objects.filter(name__icontains=query)
        return University.objects.all()


class ProgramListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        university_id = self.request.query_params.get('university', None)
        queryset = Program.objects.select_related('university').order_by('name')
        if university_id:
            queryset = queryset.filter(university_id=university_id)
        return queryset


class BranchListCreateView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        program_id = self.request.query_params.get('program', None)
        queryset = Branch.objects.all().order_by('name')
        if program_id:
            queryset = queryset.filter(
                programstructure__program_id=program_id
            ).distinct()
        return queryset


class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        branch_id = self.request.query_params.get('branch', None)
        program_id = self.request.query_params.get('program', None)
        queryset = Course.objects.all().order_by('name')
        if branch_id:
            queryset = queryset.filter(
                programstructure__branch_id=branch_id
            ).distinct()
        if program_id:
            queryset = queryset.filter(
                programstructure__program_id=program_id
            ).distinct()
        return queryset


class ProgramStructureListCreateView(generics.ListCreateAPIView):
    serializer_class = ProgramStructureSerializer

    def get_queryset(self):
        queryset = ProgramStructure.objects.select_related(
            'program__university', 'branch', 'course'
        ).order_by('program__name')
        university_id = self.request.query_params.get('university', None)
        program_id = self.request.query_params.get('program', None)
        branch_id = self.request.query_params.get('branch', None)
        course_id = self.request.query_params.get('course', None)

        if university_id:
            queryset = queryset.filter(program__university_id=university_id)
        if program_id:
            queryset = queryset.filter(program_id=program_id)
        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        return queryset