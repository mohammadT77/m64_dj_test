from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


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

        new_user = User.objects.create_user(username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)

        return HttpResponse(f"User registered by ID: {new_user.id}")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile_view')
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        from django.contrib.auth import authenticate, login

        # # Fetch user:
        # user = User.objects.get(username=username)
        # if not user.check_password(password):
        #     return HttpResponse("invalid password!")
        user = authenticate(username=username, password=password)  # user: User if true, else None!

        if user is None:
            return HttpResponse("Invalid login!")

        print('user:', user)

        # #  (login)
        # resp = HttpResponse(f"Welcome {user.first_name}!")
        # resp.set_cookie('uid', user.id)
        login(request, user)

        return HttpResponse(f"Welcome {user.first_name}!")


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return HttpResponse("Good bye!")


@login_required
def profile_view(request):
    return render(request, "auth/profile.html", {'user': request.user})
