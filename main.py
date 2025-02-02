import math
#SINTAXIS BUCLE FOR:
'''
cursos = ['ia', 'bigdata', 'sql', 'seo']
for x in cursos:
    print(x)
'''
#SINTAXIS BUCLE while
'''
i = 1
print('insertando pin...')
while i < 3:
    print('error. siguie intentando insertar el pin... tienes ', 3 - i, 'intentos.')
    i += 1
    print('has superado los 3 intenos.. llamadn a @policia...') 
  
'''
#ejemplo
'''
i = 1
while i < 10:
    print(i)
    i += 1
'''
#ejemplo 2
'''
i = 1
while i<=3:
    print(i)

    i += 1
print('programa terminado')
'''
#ejemplo 3
'''
i = 1
while i <=50:
    print(i)
    i = 3 * i + 1
print('programa terminado')
'''
#ejercicio 4
'''
n = int(input('digiite un numero: '))

#MIENTRAS(WHILE) SE CUMPLA UNA CONDICION
while n<=2:
    print('ERROR -> DEBERIA SER UN NUMERO POSITIVO')
    n = int(input('digiite un numero'))

print(f'\nsu raiz cuadrada es: {(math.sqrt(n)):.2f}')#en python la funcion math se utiliza para calcular la raiz cuadrada
'''
#EJERCICIO 5
'''
i = 1
while i<=3:
    print(i)
    i += 1
'''
#ejercicio 6
'''
for  i in range(3,12,3): #condicion de salida
    print(f'el valor del bucle es: {i}')
print('fin del bucle')
'''
#ejercicio 7 ciclo for
'''
c = ['azul','rojo','morado']
print('listado colores')
for color in c:
    #print(f'-{color}.')
    if color == 'morado':
        print(f'se roto')
        break
    print(f'color: {color}')
'''
#ejercicio 8 while
'''
i = 1
while i< 5:
    print(f'se ejecute el codigo: {i}')
    i += 1
'''
#ejercicio 9 (crea un bucle for que impima los valores del 7 al 14)
'''
n = [7,8,9,10,11,12,13,14]
print('numeros')
for nu in n:
    print(f'los siguientes son los numeros de: {nu}')
'''
#mismo ejercicio de otra forma con el ciclo for
'''
for i in range(7,15):
    print(f'numeros del 1 al 14: {i})')
'''
#ejercicio 9 (crea un bucle while que impima los valores del 7 al 14)
n = 7         # variable de inicialilzacion
while n <=14:   # especificamos la condicion
    print(f'el valor del bucle es: {n}')
    n += 1 #incremento para que la ccondicion se vuelva false