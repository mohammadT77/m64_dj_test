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

        new_user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name)

        return HttpResponse(f"User registered by ID: {new_user.id}")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if not user.check_password(password):
            return HttpResponse("invalid password!")
        print(user)

        resp = HttpResponse(f"Welcome user {user.id}!")

        # TODO: complete here! (setting user identification on session)

        return resp


def logout_view(request):
    resp = HttpResponse("Good Bye!")

    # TODO: complete here! (removing sessions)

    return resp


# login required!!!
def profile_view(request):
    user = ... # TODO: complete here! (getting user from session)

    if user is None:
        return HttpResponse("Login first!", 400)
    else:
        return render(request, "auth/profile.html", {'user': user})
