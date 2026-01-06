from string import digits

from django.db import models

# Create your models here.
class Classroom(models.Model):
    name=models.CharField(max_length=10)
    teacher=models.CharField(max_length=20)
    def __str__(self):
        return self.name
        
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)

    def __str__(self):
        return  self.name
class Guardian(models.Model):
    student=models.ForeignKey('Student',on_delete=models.CASCADE,related_name="guardians")
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    relation=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} ( {self.relation})"