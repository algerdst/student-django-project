from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.models import Group
from .models import User




def authorization(request):
    """
    Авторизация пользователя
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    data = {
        'form': form
    }
    return render(request, template_name='users/authorization.html', context=data)


def registration(request):
    """
    Регистрация пользователя
    """
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            group = Group.objects.get(name='Студенты')
            group.user_set.add(user)
            group_permissions = group.permissions.all()
            user.user_permissions.clear()
            user.user_permissions.add(*group_permissions)
            messages.success(request, 'Вы успешно зарегистрировались как студент')
            return HttpResponseRedirect(reverse('authorization'))
    else:
        form = UserRegistrationForm()
    data = {
        'form': form
    }
    return render(request, 'users/registration.html', context=data)


def profile(request):
    """
    Профиль пользователя
    """
    if request.method=='POST':
        form=UserChangeForm(data=request.POST)
        user=User.objects.get(username=request.user.username)
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form=UserChangeForm(instance=request.user)
    if request.user.is_authenticated:
        user = request.user
        data = {
            'user': user,
            'form': form,
        }
    else:
        return HttpResponseRedirect(reverse('authorization'))
    return render(request, 'users/profile.html', context=data)


def logout(request):
    """
    Выход из профиля
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change.html', {
        'form': form
    })




