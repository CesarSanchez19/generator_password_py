from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    # Obtener la longitud de la contraseña del formulario
    length = int(request.GET.get('length', 12))

    # Iniciar con letras minúsculas
    characters = list(string.ascii_lowercase)

    # Añadir otros caracteres según las opciones seleccionadas
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))

    # Generar la contraseña
    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': password})
