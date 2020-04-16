from django.shortcuts import render, HttpResponse
def hello(requests, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos.</h1>')
# Create your views here.
