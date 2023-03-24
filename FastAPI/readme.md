# Fast Api
## Creacion del entorno
1. Instalar la libreria del entorno virtual ''''pip install virtualenv''''
2. Creacion del entorno virtual ''' python -m virtualenv [nombre]"
3. verificamos el python general 'pip freeze' deben salir varias librerias.
4. ENtro a mi entorno virtual (EN WINDOWS DESDE GIT BASH) 'sourche [nombre]/Script/activate' y sale el nombre de mi entorno virtual en mi linea de comandos.   

## Instalar FastAPI
1. Instalacion de FastAPI 'pip install fastapi uvicorn''' 

--- 

# Python 

Es un lenguaje de programación interpretado, de tipo dinámico, cuya filosofía destaca en una sintaxis que favorezca el código legible. Python es interpretado por que se ejecuta sin necesidad de ser procesado por el compilador y se detectan los errores en tiempo de ejecución. 

Print = tal como dice, se usa para imprimir o mostrar algo en la consola

	print(“hello world”)

## **Variables** 

Forma de almacenar los datos de un código, es decir, tu puedes almacenar en una variable, números, cadenas de texto o datos insertados por el usuario. Pueden ser locales o globales, si son locales el valor de este solo se mantiene dentro de cierta operación, pero los globales se guarda dentro de todo el codigo

## **String (str)** 

Cadenas de texto, se escriben entre comillas, para que en la consola se vea tal cual lo pones en el código con triple comilla. 
		
		print(“hello world”) 

f-string= Se usa para introducir variables y texto al mismo tiempo, usamos comillas simples y encerramos la variable entre corchetes.

	print(f’{i} string’)

	Concatenación = unir dos trozos de código, se hace con el signo + entre datos tipo str, pero 	cuando hay datos numéricos, se usa la coma.

		nombre = “Sergio”
		apellido = “ Romulo”
		nombre_completo = nombre + apellido
		print(nombre_completo)
	
	Salto de línea = \n, para saltarse una línea, es stackable, (esto se pone dentro de las  		comillas).
			print(“\nHola world”)

	Sangría = \t, para hacer un espaciado, es stackable(esto se pone dentro de las comillas)

			print(“\tHello”)




Mayúscula = para convertir todo una cadena de texto a mayúscula usamos un método de                  str, el .upper, al ser  un método es importante poner .upper()

		nombre=Samuel
print(nombre.upper())
 
end = Se usa para que las cadenas de texto o impresiones en un bucle, se impriman en la misma línea, se usa, end=””, en las comillas se inserta de la manera que quieres que se distancien. 

Minúscula =  Para convertir una cadena de texto a minúscula usamos el método .lower()	
		
		nombre=Samuel
		print(nombre.lower())

Para convertir  a mayúscula solo la primera letra usamos el método “.capitalize()“

Podemos usar el método .split para dividir una cadena de texto por cierto intervalo, retornando una lista, esta lista puede ser recorrida,por ejemplo.

x = ‘hola como estas’
y = x.split = ‘ ‘
print(y)

Esto imprimirá [‘hola,.’como,’estas’]

La función len(), también puede ser usada en los str, pero lo que hace en este caso es contar cada letra, una aplicación de todo lo aplicado en la lista se ve en el siguiente ejemplo:

h = 'hola como estas'
y = h.split(' ')
z = len(h)
print(z)
print(type(y))


## **Numéricos**  

Números enteros (int) o números decimales (float)

Operadores Aritméticos = Los operadores aritméticos son aquellos con los que realizamos operaciones matemáticas, son 6, la suma (+), la resta (-), la multiplicación (*), la división (/), la división exacta (//) y usamos el porcentaje para ver el residuo de una operación (%), para elevar a cualquier exponente se usa (**)




Operadores de asignación = Le asignamos a una variable un valor y trabajamos con este, tal cual la álgebra, pero para que se guarde en la variable el resultado de la operación, usamos un igual del signo, un programa usando operadores de asignación se ve mas o menos así:

	x = float(input("Cual es el valor de x: " ))
x+=2
print("El nuevo valor de x es: ", x)

Este mismo proceso se puede hacer con el resto de operaciones aritméticas. Para evitar que el usuario inserte cadenas de texto, podemos usar el try and except, de esta forma:

	try:    
  	 valor1=int(input("Ingrese primer valor:"))
  	 valor2=int(input("Ingrese segundo valor:"))
  	 suma=valor1+valor2
 	 print("La suma es",suma)
except ValueError:
  print("debe ingresar números.")

	## Booleano 

 Datos verdaderos o falsos, true or false.

Operadores comparativos = Son aquellos que podemos usar para comparar dos datos, y que la consola nos diga si son verdaderos o falsos, podemos usar, mayor que o menor que (<>), igual que (=), diferente que (!=), mayor o igual (>=), menor o igual (<=)

	print(2<3) == true
	print(2=2) == true

Interacciones con usuario

Input = Puedes usar input para que el usuario inserte un dato, en este mismo le puedes especificar a la consola que tipo de dato tiene que tomar (str,float,int). Se puede usar para pedirle a un usuario que le asigne un valor a una variable.

	n1 =  float(input(“Cuantos años tienes ?: “)

El igual funciona para indicarle que n1 es igual al input del usuario, y float indica a la consola que los únicos tipos de datos que puede aceptar, por esto cuando el usuario inserte un tipo de dato y en caso de que no lo haga bien le salga error, pero en caso de que esto pase, usaremos el comando try and except ValueError, poner esto en uso se ve así:

try:
  	numero = int(input("Cuantos años tienes ?: "))
 	 print(numero)
except ValueError:
 	 print("Inserta un valor numérico sin letras")
