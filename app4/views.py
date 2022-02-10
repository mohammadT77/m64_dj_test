from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def register_view(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # validations
        # normalization
        # error handling

        new_user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name)

        return HttpResponse(f"User registered by ID: {new_user.id}")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        # Fetch user:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return HttpResponse("invalid password!")

        # set cookie (login)
        resp = HttpResponse(f"Welcome {user.first_name}!")
        resp.set_cookie('uid', user.id)

        return resp


def logout_view(request):
    resp = HttpResponse("Good bye!")
    resp.delete_cookie('uid')
    return resp


# login required!!!
def profile_view(request):
    uid = request.COOKIES.get('uid', None)

    if uid is None:
        return HttpResponse("Login first!", 400)
    else:
        user = User.objects.get(id=uid)
        return render(request, "auth/profile.html", {'user': user})
