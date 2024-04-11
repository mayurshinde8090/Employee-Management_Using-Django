from django.db import models
from django.contrib.auth.models import User


class EmployeeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employeecode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=10, null=True)
    joiningdate = models.DateField(null=True)
    salary = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=250,null=True)
    age = models.CharField(max_length=20,null=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(default='default.jpg',upload_to='empimg-')

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100, null=True)
    schoolclgpg = models.CharField(max_length=200, null=True)
    yearofpassingpg = models.CharField(max_length=10, null=True)
    percentagepg = models.CharField(max_length=30, null=True)

    coursegra = models.CharField(max_length=100, null=True)
    schoolclggra = models.CharField(max_length=200, null=True)
    yearofpassinggra = models.CharField(max_length=10, null=True)
    percentagegra = models.CharField(max_length=30, null=True)

    coursessc = models.CharField(max_length=100, null=True)
    schoolclgssc = models.CharField(max_length=200, null=True)
    yearofpassingssc = models.CharField(max_length=10, null=True)
    percentagessc = models.CharField(max_length=30, null=True)

    coursehsc = models.CharField(max_length=100, null=True)
    schoolclghsc = models.CharField(max_length=200, null=True)
    yearofpassinghsc = models.CharField(max_length=10, null=True)
    percentagehsc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100,null=True)
    company1desig = models.CharField(max_length=100,null=True)
    company1salary = models.CharField(max_length=100,null=True)
    company1duration = models.CharField(max_length=100,null=True)

    company2name = models.CharField(max_length=100,null=True)
    company2desig = models.CharField(max_length=100,null=True)
    company2salary = models.CharField(max_length=100,null=True)
    company2duration = models.CharField(max_length=100,null=True)

    company3name = models.CharField(max_length=100,null=True)
    company3desig = models.CharField(max_length=100,null=True)
    company3salary = models.CharField(max_length=100,null=True)
    company3duration = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username
