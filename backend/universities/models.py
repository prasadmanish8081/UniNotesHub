from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='universities/', null=True, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="programs")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='programs/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.university.name})"


class Branch(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='branches/', null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return self.name


class ProgramStructure(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('program', 'branch', 'course')

    def __str__(self):
        return f"{self.program} - {self.branch} - {self.course}"