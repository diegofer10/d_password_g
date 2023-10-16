from django.shortcuts import render
import random
 
# Create your views here.
def home (request):
    return render (request, 'generator/home.html')

def about (request):
    return render (request, 'generator/about.html')




def password (request):
    #Crear una lista para devolver 
    characters = list ('abcdefghfqrstuvwxyz')
    generate_password=''

    #leo los elementos del url y lo conveierto a entero
    length=int(request.GET.get('length'))
   
   #Valido que no sea mas de 100
    if length> 100:
        print ('Error')


    #Valido si el check esta en yes
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    #Valido caracteres especiales
    if request.GET.get('special'):
        characters.extend('$%#@()!"|}]{-}')

    #Valido numeros
    if request.GET.get('special'):
        characters.extend('1234567890')
    

    #recooro los elementos y los limito con el range por ejemplo 10
    for x in range(length):
        generate_password +=random.choice(characters)

    #le paso el resultado del generate
    return render (request, 'generator/password.html' , {'password': generate_password})

