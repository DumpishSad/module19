from django.shortcuts import render

from task1.forms import UserRegister
from task1.models import Buyer, Game


def sign_up_by_django(request):
    info = ''
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            if password != repeat_password:
                info = "Пароли не совпадают."
            elif age < 18:
                info = "Возраст должен быть не менее 18 лет."
            elif Buyer.objects.filter(name=username).exists():
                info = "Пользователь с таким именем уже существует."
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info = f"Приветствуем, {username}!"

    return render(request, 'registration_page.html', {'form': form, 'info': info})


def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


def home_view(request):
    return render(request, 'home.html')


def cart_view(request):
    return render(request, 'cart.html')
