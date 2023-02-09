from django.http.response import HttpResponse
from django.http.request import HttpRequest


def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Домашня сторінка')


def greeting(request: HttpRequest, user_name: str) -> HttpResponse:
    return HttpResponse(f'Greeting, {user_name}')


def progression(start, count, step):
    list_1 = [start]
    for i in range(1, count):
        start += step
        list_1.append(start)
    str_1 = ' '.join([str(elem) for elem in list_1])
    return str_1


def progression_view(request: HttpRequest, start, count, step) -> HttpResponse:
    result_progression = progression(start, count, step)
    return HttpResponse(result_progression)


# Function for nth Fibonacci number
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_view(request: HttpRequest, n) -> HttpResponse:
    result = fibonacci(n)
    return HttpResponse(result)
