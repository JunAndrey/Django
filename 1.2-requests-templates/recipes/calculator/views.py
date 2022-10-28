from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    template_name = 'calculator/index.html'
    pages = {
        'omlet': reverse('omlet'),
        'buter': reverse('buter'),
        'pasta': reverse('pasta')
    }

    dishes_final = []
    for dishes in DATA:
        dishes_final.append(dishes)

    context = {'dishes': dishes_final,
               'pages': pages,
               }
    return render(request, 'calculator/index.html', context)


def omlet(request, arg=1):
    ingridients = {}
    for i, ingridient in DATA['omlet'].items():
        ingridients[i] = ingridient * arg
    context = {'ingridients': ingridients, 'arg': arg
               }
    return render(request, 'calculator/omlet.html', context)


def pasta(request, arg=1):
    ingridients = {}
    for i, ingridient in DATA['pasta'].items():
        ingridients[i] = ingridient * arg
    context = {'ingridients': ingridients, 'arg': arg
               }
    return render(request, 'calculator/pasta.html', context)


def buter(request,arg=1):
    ingridients = {}
    for i, ingridient in DATA['buter'].items():
        ingridients[i] = ingridient * arg
    context = {'ingridients': ingridients, 'arg': arg
               }
    return render(request, 'calculator/buter.html',  context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
