from django.http import HttpResponse


def index(request):
    return HttpResponse('Матусан Станислав Леонидович, покупай джетту, заебал!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
