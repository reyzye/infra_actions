from django.http import HttpResponse


def index(request):
    return HttpResponse('Матусан Станислав Леонидович, покупай джетту по-братски!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
