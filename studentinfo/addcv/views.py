from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, username=username)
        user.save()
        return HttpResponse('Data added')

    else:
        return render(request, 'firatpage.html')


def second(request):
    return HttpResponse("welcome")


def home(request):
    user = User.objects.all()
    return render(request, 'home.html', {'user': user})


def addinfo(request):
    if request.method == 'POST':
        picture = request.POST["picture"]
        name = request.POST['name']
        lastname = request.POST['lastname']
        city = request.POST['city']
        contact = request.POST['contact']
        matricnumber = request.POST['matricnumber']
        internumber = request.POST['internumber']
        bachelorcgpa = request.POST['bachelorcgpa']

        users = UserProfile(picture=picture, name=name, lastname=lastname, city=city, contact=contact, matricnumber=matricnumber,
                            internumber=internumber, bachelorcgpa=bachelorcgpa)
        users.save()
        return HttpResponse('Data added')
    else:
        return render(request, 'addinfo.html')


def showdata(request):
    people = UserProfile.objects.all()
    return render(request, 'showdata.html', {'people': people})












