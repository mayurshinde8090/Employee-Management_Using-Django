from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate



def index(request):
    return render(request, 'index.html')


def registration(request):

    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        e = request.POST['email']
        pwd = request.POST['pwd']
        ec = request.POST['employeecode']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=e, password=pwd)
            EmployeeEntry.objects.create(user=user, employeecode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)

            error = "no"
        except:
            error = "yes"

    return render(request, 'registration.html', locals())


def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, 'emp_login.html', locals())
def footer(request):
     return render(request, 'footer.html')


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')


def emp_logout(request):
    return render(request,'emp_logout.html')

def admin_logout(request):
    return render(request,'admin_logout.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeEntry.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        salary = request.POST['salary']
        address = request.POST['address']
        age = request.POST['age']
        dob = request.POST['dob']



        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.employeecode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.salary = salary
        employee.address = address
        employee.age = age
        employee.dob = dob


        if jdate:
            employee.joiningdate = jdate
        employee.gender = gender



        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"


    return render(request, 'profile.html', locals())





def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request, 'myexperience.html', locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"
        except:

            error = "yes"
    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        try:
            education.save()
            error = "no"
        except:

            error = "yes"
    return render(request, 'edit_myeducation.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_password.html', locals())


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'admin_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_passwordadmin.html', locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeEntry.objects.all()
    return render(request, 'all_employee.html', locals())


def delete_employee(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')


def edit_profile(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    employee = EmployeeEntry.objects.get(id=pid)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeecode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.employeecode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        if jdate:
            employee.joiningdate = jdate
        employee.gender = gender

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_profile.html', locals())


def edit_education(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        try:
            education.save()
            education.user.save()
            error = "no"
        except:

            error = "yes"
    return render(request,'edit_education.html', locals())


def edit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"
        except:

            error = "yes"
    return render(request, 'edit_experience.html', locals())
