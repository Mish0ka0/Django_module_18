from django.shortcuts import render

# Create your views here.


def start_menu(request):
    title = 'Игровой магазин'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'fourth_task/start_menu.html', context)


def game_catalog(request):
    title = 'Каталог товаров'
    heading = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    button = 'Купить'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'games': games,
        'button': button,
        'back_button': back_button
    }
    return render(request, 'fourth_task/game_catalog.html', context)


def shopping_cart(request):
    title = 'Корзина'
    heading = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'text': text,
        'back_button': back_button
    }
    return render(request, 'fourth_task/shopping_cart.html', context)
