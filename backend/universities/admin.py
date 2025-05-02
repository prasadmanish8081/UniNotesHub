from django.contrib import admin
from .models import University, Program, Branch, Course, ProgramStructure


class ProgramStructureInline(admin.TabularInline):
    model = ProgramStructure
    extra = 1
    fields = ('branch', 'course')


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image')
    search_fields = ('name',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'image')
    fields = ('name', 'university', 'image')
    list_filter = ('university',)
    inlines = [ProgramStructureInline]
    search_fields = ('name', 'university__name')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image')
    search_fields = ('name',)


@admin.register(ProgramStructure)
class ProgramStructureAdmin(admin.ModelAdmin):
    list_display = ('program', 'branch', 'course')
    list_filter = ('program__university', 'program', 'branch', 'course')
    search_fields = ('program__name', 'branch__name', 'course__name')
    fields = ('program', 'branch', 'course')