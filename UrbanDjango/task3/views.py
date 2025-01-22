from django.shortcuts import render

# Create your views here.


def start_menu(request):
    title = 'Игровой магазин'
    heading = 'Главная страница'
    main = 'Главная'
    store = 'Магазин'
    trash = 'Корзина'
    context = {
        'title': title,
        'heading': heading,
        'main': main,
        'store': store,
        'trash': trash
    }
    return render(request, 'third_task/start_menu.html', context)


def game_catalog(request):
    title = 'Каталог товаров'
    heading = 'Игры'
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpunk 2077'
    game_3 = 'PayDay 2'
    button = 'Купить'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'button': button,
        'back_button': back_button
    }
    return render(request, 'third_task/game_catalog.html', context)


def shopping_cart(request):
    title = 'Корзина'
    heading = 'Извините, ваша корзина пуста'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'back_button': back_button
    }
    return render(request, 'third_task/shopping_cart.html', context)
