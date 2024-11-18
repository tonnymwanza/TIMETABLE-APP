from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class TimeTable(models.Model):
    day_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    )
    day = models.CharField(max_length=10, choices=day_choices)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day}: {self.subject.name} by {self.teacher.name}"