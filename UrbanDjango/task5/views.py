from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister
# Create your views here.


def sign_up_by_html(request):
    users = ['user', 'user1', 'user2']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age
        }
        if password == repeat_password and username not in users and int(age) > 18:
            return HttpResponse(f'Приветсвуем, {username}!')
        if password != repeat_password:
            info.update({'error': "Пароли не совпадают"})
        if int(age) < 18:
            info.update({'error': "Вы должны быть старше 18"})
        if username in users:
            info.update({'error': "Пользователь уже существует"})

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    users = ['user', 'user1', 'user2']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {
                'username': username,
                'password': password,
                'repeat_password': repeat_password,
                'age': age,
                'form': form
            }
            if password == repeat_password and username not in users and int(age) > 18:
                return HttpResponse(f'Приветствуем, {username}')
            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            if int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
            if username in users:
                info['error'] = "Пользователь уже существует"
        else:
            form = UserRegister()
            info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
