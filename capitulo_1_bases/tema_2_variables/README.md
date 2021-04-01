# Variables y Tipos de datos básicos

En este capítulo aprenderemos acerca de los diferentes tipos de datos que podemos utilizar en los programas de Python, y aprenderemos que son las variables y cómo se utilizan.

## Entendiendo que pasa con hola_mundo.py

Vamos a ver un poco mas a detalle nuestro archivo hola_mundo.py.

Python hace bastante trabajo incluso cuando nosotros corremos un programa tan pequeño:

```python
print("¡Hola Mundo!")
```

Cuando nosotros corremos ese código el output que tenemos es:

```python
¡Hola Mundo!
```

Cuando corremos el archivo hola_mundo.py la terminacion .py indica que es un archivo de un programa de Python. Tu terminal corre el archivo a través del intérprete de Python, el cual lee el programa y dice que significa cada una de las palabras del programa. Por ejemplo cuando el intérprete ve print seguido de paréntesis va a imprimir lo que sea que esté dentro de los paréntesis.

Cuando escribes código verás como tu editor marca con diferentes colores las palabras para que te ayude a determinar que tipo de valor es.

## Variables

Vamos a crear una variable en hola_mundo.py el codigo deberia de quedar asi:

```python
mensaje = "¡Hola Python!"
print(mensaje)
```

Corre el programa y veras que el resultado deberías ver es:

```python
¡Hola python!
```

Hemos agregado una variable llamada mensaje. Toda variable va a tener un valor, y una información asociada a ese valor, en este caso "¡Hola Python!".

Vamos a modificar de nuevo nuestro código para que quede algo asi:

```python
mensaje = "¡Hola Python!"
print(mensaje)

mensaje = "¡Hola Curso de Python!"
print(mensaje)
```

Ahora cuando corras el programa el output debería ser:

```python
¡Hola python!
¡Hola Curso de Python!
```

Tu puedes cambiar el valor de una variable en cualquier momento y Python siempre va a saber cual es su valor actual.

### Nombrando y usando variables

Cuando utilizas variables hay algunas reglas que debes utilizar para evitar errores y para hacer más fácil de leer el código que estás escribiendo.

* Los nombres de las variables solo pueden contener letras, número y guión bajo. pueden empezar con letra o guión bajo pero nunca con un número.
* Los espacios jamás se deben utilizar para palabras en las variables, ahi usamos guión bajo. Por ejemplo *nombre_pokemon* funciona pero *nombre pokemon* generaría errores.
* No utilices palabras reservadas o de funciones de Python como print.
* Los nombres de las variables deberían de ser cortos pero descriptivos. Por ejemplo *nombre* es mejor que *n*, *nombre_estudiante* es mejor que *n_s* y *numero_nombres* es mejor que *numero_de_nombres_de_personas*.

Hacer buenos nombres de variables es un tema de práctica entre más programas vayas creando y más complejos estos se vuelvan tus nombres irán mejorando.

### Evitando errores cuando se usan variables

Todos los programadores tenemos errores, y casi todos cometen errores a diario.

Y aunque los buenos programadores pueden crear errores también deben saber cómo resolverlos

Vamos a ver un error común que es fácil tener y cómo resolverlo

Escribe el siguiente código al final de hola_mundo.py, incluyendo la palabra mal escrita **mensaj**

```python
mensaje = "No hay error"
print(mensaj)
```

Una vez que corras el programa python nos arroja el siguiente output:

```python
¡Hola Python!
¡Hola Curso de Python!
Traceback (most recent call last):
  File "hola_mundo.py", line 8, in <module>
    print(mensaj)
NameError: name 'mensaj' is not defined
```

Cuando un error ocurre Python va a intentar ayudarnos a descubrir cuál es el error. Python nos mostrara un Traceback el cual nos ayudará a determinar cuál es el error.

En este caso el traceback nos dirá que el error fue en el archivo *hola_mundo.py* en la línea *8*. Nos dirá en donde encontró el error en este caso en *print(mensaj)* y el tipo de error que encontró en este caso que *mensaj* no está definido.

Para solucionarlo simplemente tendríamos que corregir el nombre de nuestra variable a *mensaj* y así solucionamos el problema. Asi quedaria nuestro hola_mundo.py completo

```python
mensaje = "¡Hola Python!"
print(mensaje)

mensaje = "¡Hola Curso de Python!"
print(mensaje)

mensaj = "No hay error"
print(mensaj)
```

### Las variables son etiquetas

Las variables son como etiquetas a las que nosotros podemos asignar valores

### Ejercicios variables

Para repasar lo que hemos aprendido haremos dos ejercicios

1. Crea un archivo nuevo que se llame refran_simple.py y haz que imprima un refran, si no sabes ningun refran usa alguno de esta [pagina](https://psicologiaymente.com/reflexiones/refranes-cortos).

2. Crea un archivo nuevo que se llame cuenta_chiste.py y haz que imprima un chiste de dos o más líneas, si no sabes ninguno puedes usar alguno de esta [pagina](https://nosolochistes.com/chistes-cortos).

Compara tus soluciones con la de tus compañeros, o revisa mis soluciones [refran_simple.py](https://github.com/dragaus/curso-python/blob/main/capitulo_1_bases/tema_2_variables/refran_simple.py) o [cuenta_chiste.py](https://github.com/dragaus/curso-python/blob/main/capitulo_1_bases/tema_2_variables/cuenta_chiste.py)

## Strings o Cadenas de texto

Ya que la mayoría de los programas define y recolecta información, y después se hace útil con ella, es importante clasificar los diferentes tipos de información. El primer tipo que veremos son los Strings o Cadenas de texto(A partir de este momento por simplicidad diré siempre Strings aunque el nombre en español sea Cadenas de texto).

Los Strings son una serie de caracteres. Todo lo que esté dentro de comillas dobles o simples es considerado un String ejemplo:

```python
"Esto es un string"
'Esto también es un string'
```

Esta flexibilidad te permite utilizar comillas o apóstrofes dentro de tus strings ejemplo:

```python
'Le dije "El mejor motor de python es Pygame"'
"El lenguaje 'Python' es nombrado por Monty Python, no por la serpiente"
```

### Cambiando Mayusculas y minusculas

Veamos ahora un poco de lo que podemos lograr con los string.

crea un archivo que se llame nombre.py y agrega el siguiente código:

```python
nombre = "pedro paramo"
print(nombre.title())
```

Guarda el archivo y ejecutalo y deberías de tener el siguiente resultado

```python
Pedro Paramo
```

En este ejemplo lo que estamos haciendo es guardar una variable con la información del nombre en minúsculas. El método **title()** que aparece después de la variable dentro de **print()** se ejecuta.
Un método es una acción que Python ejecuta en un pedazo de información, el punto (.) después de la variable *nombre* es la que le dice a Python que ejecute el método **title()**. Todos los métodos son llamados con unos paréntesis ya que hay veces que requieren información para funcionar.

El método **title()** hace que todas las palabras empiezen con mayúscula.

Hay muchos mas métodos que se encargan de cambiar entre minusculas y mayusculas los strings por ejemplo si quisieramos todas las letras en mayusculas podemos usar **upper()** o para minusculas usaríamos **lower()**, agrega estos metodos a nombre.py tu codigo deberia de quedar así:

```python
nombre = 'pedro paramo'
print(nombre.title())
print(nombre.upper())
print(nombre.lower())
```

Y el resultado se veria asi:

```python
Pedro Paramo
PEDRO PARAMO
pedro paramo
```

### Usando variables en los Strings

En algunas ocasiones necesitas usar variables dentro de un string por ejemplo cuando quieres usar el nombre y el apellido de una una persona y después combinarlos para mostrar el nombre completo.

Haz un codigo nuevo que se llame nombre_completo.py e introduce el siguinte codigo

```python
nombre = "pedro"
apellido = "paramo"
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
```

Para poder insertar un valor dentro de un string lo que tenemos que hacer es poner una letra f justo antes de las comillas. poner llaves alrededor del nombre de la variable que quieres usar y Python cambiará cada una de las variables por un string que usaríamos.

Estos strings son llamado *f-strings*. La *f* is por *format* (Formato en español), el resultado del código anterior quedaría como:

```python
pedro paramo
```

Puedes hacer muchas cosas con los *f-string*. por ejemplo puedes generar un mensaje completo con la información asociada a la variable, por ejemplo si modificamos nombre_completo.py para que quede de esta manera:

```python
nombre = "pedro"
apellido = "paramo"
nombre_completo = f"{nombre} {apellido}"
print(f"Hola {nombre_completo.title()}")
```

Aqui el nombre completo se usa dentro de la oración, y el método title() pone en mayusculas todas las letras iniciales del nombre y apellido y regresa el siguiente saludo:

```python
Hola Pedro Paramo
```

Tú también puedes guardar una *f-string* dentro de una variable:

```python
nombre = "pedro"
apellido = "paramo"
nombre_completo = f"{nombre} {apellido}"
message = f"Hola {nombre_completo.title()}"
print(message)
```

Este código mostraría exactamente lo mismo solo que almacena el mensaje en una variable nueva y hace mucho más entendible la parte final.

**Importante**
Este formato se introdujo en Python 3.6 si estás usando Python 3.5 o inferior esta sintaxis generará un error tendrías que usar el método **format()** para saber como se utiliza visita esta [pagina](https://www.geeksforgeeks.org/python-format-function/)

### Agregar espacio a las strings con tabulador o nuevas líneas

En programación un *whitespace* se refiere a cualquier espacio en blanco o carácter no imprimible, como espacio, tabulación o salto de línea. Tu puedes usar un *whitespace* para hacer más entendible u organizar el output.

* Para agregar una tabulación simplemente usa el signo '\t'
* Para agregar un salto de línea utiliza el signo '\n'
* Puedes utilizar saltos y tabulaciones juntas '\n\t'

Intenta este ejemplo desde la terminal de python:

```python
>>> print('Lenguajes:\n\tPython\n\tC#\n\tTypescript\n\tRuby')
Lenguajes:
 Python
 C#
 Typescript
 Ruby
```

### Espacios en blanco

Los espacios extra en blanco pueden ser muy confusos en tu programa, para nosotros *'python'* y *'python '* pueden lucir prácticamente iguales, pero Python son dos strings completamente diferentes a menos que le digamos lo contrario

Es importante que pienses en la existencia o probable existencia de estos espacios en blanco ya que podría hacer que se generen errores no deseados. por ejemplo cuando un usuario ingresa su correo o contraseña con un espacio extra puede llevar a situaciones desagradables. Afortunadamente python nos hace esta tarea muy simple y nos proveé de diferentes métodos:

* rstrip() se asegura de que no existan espacios en blanco al final de nuestro string a la derecha
* lstrip() se asegura de que no exitan espacion en blanco al final de nuestro string a la izquierda
* strip() se asegura de borrar todos los espacios del final de la derecha e izquierda

podemos probar esto en nuestra terminal de python de la siguiente manera:

```python
>>> lenguaje_programacion = " python "
>>> lenguaje_programacion.rstrip()    
' python'
>>> lenguaje_programacion.lstrip()
'python '
>>> lenguaje_programacion.strip()
'python'
```

### Ejercicios Strings

En cada uno de los siguientes ejercicios crea un archivo con el nombre del ejercio ejemplo mensaje_personal.py

1. **Mensjae Personal**: usa una variable para representar el nombre de una persona e imprimir un mensaje a esa persona por ejemplo: *Buenos dias pedro, ¡Ten un excelente dia!*.

2. **Nombres Mayus** usa una variable para representar el nombre de una persona y después imprime en minúsculas, mayúsculas y capitalizado su nombre.

3. **Cita Famosa** encuentra una cita de una persona famosa que admires imprime el nombre del famoso y la cita entre comillas, [en esta pagina puedes encontrar frases](https://proverbia.net/). Debería verse algo asi: *Hermann Hesse dijo: "Los libros sólo tienen valor cuando conducen a la vida y le son útiles."*

4. **Cita Famosa2** haz lo mismo que en el ejercicio 3 solo que esta vez agrega una variable llamada persona_famosa. luego crea tu mensaje y guárdalo en una variable llamada cita, e imprime la cita

5. **Quitando Espacios** Escribe un nombre con espacios recuerda que puedes usar '\t \n' para agregar espacios y muestra cómo funciona cada una de las funciones **lstrip()**, **rstrip()** y **strip()**

Compara tus soluciones con la de tus compañeros, o revisa [mis soluciones en esta carpeta](https://github.com/dragaus/curso-python/blob/main/capitulo_1_bases/tema_2_variables/)

## Números

Los números son usados frecuentemente en la programación para mantener puntajes en los juegos, representar datos, guardar información en aplicaciones web, etc. Python maneja los números de maneras diferentes dependiendo de cómo son usados.

### Enteros

Puedes sumar (+), restar (-), multiplicar (*) y dividir(/) enteros en Python

```python
>>> 2 + 2
4
>>> 3 + 2
5
>>> 4 - 2
2
>>> 3 * 3
9
>>> 3 / 2
1.5

```

En una sesión de terminal Python simplemente regresa el resultado de la operación. Python utiliza dos signos de multiplicación para representar exponentes

```python
>>> 3 ** 3
27
>>> 5 ** 5
3125
```

Python respeta el orden de las operaciones,y  también puedes usar paréntesis para modificar su orden

```python
>>> 2 + 6 *8
50
>>> (2 + 6) *8
64
```

### Floats (Decimales)

En Python a los números con decimales los llamamos *float*. Este término es usado en la mayoría de los lenguajes de programación, y hace referencia a que un punto decimal puede estar en cualquier lugar del número.

La mayor parte del tiempo puedes usar decimales sin preocuparte cómo se comportan, simplemente úsalos y es muy probable que Python haga lo que estás esperando.

```python
>>> 2 + 6 *8
50
>>> (2 + 6) *8
64
```

Pero hay algunas veces en las que puedes tener un número arbitrario de decimales en tu respuesta

```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

Esto sucede en todos los lenguajes de programación por la manera en la que se representan internamente los números en las computadoras, de momento ignora esos números extra. vamos a aprender a ignorar esos números cuando sea necesario.

### Enteros y Floats

Siempre que divides dos números, incluso si son enteros tendrás como resultado un numero entero:

```python
>>> 10 / 5
2.0
>>> 100 / 4 
25.0
```

Si mezclas un entero con un *float* siempre obtendrás un float de igual manera:

```python
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
```

### _ en Números

Cuando estas escribiendo número muy largos, tú simplemente puedes agruparlos en digitos usando un guion bajo para hacer los números más entendibles

```python
>>> universe_age = 14_000_000_000
```

Cuando tu imprimes un número que fue definido con *_*, Python imprime solo los digitos

```python
>>> print(universe_age)
14000000000
```

Python ignora los guiones bajos cuando guarda este tipo de valores. Incluso si no agrupados en tríos. Para Python 1000, 1_000 o 10_00 son exactamente lo mismo.

Esta característica funciona tanto para enteros como para *floats* sin embargo solo funciona en Python 3.6 y posterior

### Asignaciones Múltiples

Podemos asignar valores a más de una sola variable en una sola línea.

Esto puede ayudar a reducir los programas y hacerlos más sencillos de leer, esta técnica suele utilizarse cuando inicializamos un grupo de números.

Por ejemplo, así es como podremos inicializar x , y, y z a cero:

```python
>>> x, y, z = 0, 0, 0
>>> print(x)
0
>>> print(y)
0
>>> print(z) 
0
```

Simplemente escribe las variables y separarlas por comas, haz lo mismo con los valores, y Python se encargará de asignar cada valor con su variable respectiva.

### Constantes

Python a diferencia de otros lenguajes de programación no tiene constantes, pero una practica entre programadores para indicar que una variable debe ser tratada como constante es el uso de mayúsculas en toda la variable:

```python
>>> NUMERO_MAXIMO_DONAS = 500
```

### Ejercicios Números

1. **Ocho Magico** crea un script que se llame ocho_magico.py e imprime una suma, una resta, una multiplicación y una división que den 8. tu output deberían ser 4 líneas que den 8.
2. **Numero Favorito** Usa una variable que represente tu número favorito. Después usando esa variable, crea un mensaje que revele tu número favorito e imprime tu mensaje

Compara tus soluciones con la de tus compañeros, o revisa [mis soluciones en esta carpeta](https://github.com/dragaus/curso-python/blob/main/capitulo_1_bases/tema_2_variables/)

## Comentarios

Los comentarios son una característica extremadamente útil en la mayoría de los lenguajes de programación. Hasta ahora todo lo que hemos escrito es código de Python. Pero a medida que nuestros proyectos crecen y se vuelven más complejos, debemos escribir comentarios que describan la manera en la que estamos resolviendo un problema. Un comentario te permite poner notas en un idioma humano dentro de tus programas.

### Como se escriben los comentarios

En python el símbolo *#* indica un comentario todo lo que este después de un *#* es ignorado por Python, escribe este código en un nuevo archivo que llamaremos comentario.py

```python
# Decirles a hola a todos
print("¡Hola a todos!")
```

Python ignorara la primera línea y ejecuta la segunda

```python
¡Hola a Todos!
```

### ¿Qué tipo de comentarios debes escribir?

Generalmente cuando estas resolviendo un problema eres capaz de descifrar cómo se ejecuta cada parte del proyecto, pero cuando vuelves un tiempo después es muy probable que lo hayas olvidado algunos detalles (o todo). Siempre puedes estudiar tu código para ver como funciona todo, pero escribir buenos comentarios puede ahorrarte mucho tiempo.

Si quieres colaborar con otras personas siempre es bueno que tengas la capacidad de escribir comentarios importantes para explicar a los demás lo que tu código debe de hacer.

### Ejercicios Comentarios

1. **Agrega Comentarios** agrega en al menos dos programas que hayamos escrito cuando menos un comentario, si los programas son demasiado simples escribe tu nombre al principio del código.
