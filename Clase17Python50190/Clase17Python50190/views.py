from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola comision 50190-Coder!!!')

def segunda_vista(request):
    return HttpResponse('<progress value="75" max="100"></progress>Hola Coder')