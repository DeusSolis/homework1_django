from django.http.response import HttpResponse
from django.http.request import HttpRequest


def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Домашня сторінка')


def greeting(request: HttpRequest, user_name: str) -> HttpResponse:
    return HttpResponse(f'Greeting, {user_name}')


def progression(request: HttpRequest, start, count, step) -> HttpResponse:
    list_1 = [start]
    for i in range(1, count):
        start += step
        list_1.append(start)
    str_1 = ' '.join([str(elem) for elem in list_1])

    return HttpResponse(str_1)

def fibonacci(request: HttpRequest, n) -> HttpResponse:
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return HttpResponse(a)
    elif n == 1:
        return HttpResponse(b)
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return HttpResponse(b)