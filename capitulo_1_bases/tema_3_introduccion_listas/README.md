# Introducción a las listas

En este capítulo aprenderemos qué son las listas y cómo empezar a trabajar con ellas. Las listas nos permiten almacenar información en un solo lugar, ya sea unos cuantos elementos o millones de ellos

## ¿Qué es una lista?

Una lista es una colección de items en un orden particular. Por ejemplo podemos hacer una lista que incluya todas la letras del alfabeto, o los números del 0 al 9, o los nombres de todos los tipos de peces que hay en tu acuario. Puedes guardar cualquier información que tu quieras en una lista, y los items que tengas en tu lista no deben estar relacionados de ninguna manera en particular. Debido a que las listas suelen contener más de un tipo de elemento, los nombres suele ser una buena idea ponerlos en plural, ejemplo *letras*, *razas_perros*, etc.

En Python  estos símbolos *[]* indican que estamos trabajando con una lista, y las comas representan la separación entre los elementos dentro de una lista.

Hagamos un ejemplo de esto en un código que llamaremos peces.py escribe el siguiente codigo:

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces)
```

Estamos haciendo una lista y estamos pidiéndole a Python que nos de una representación de esa lista.

```python
['angel', 'guppy', 'betta', 'payaso']
```

### Acceder a un elemento de una lista

Las listas son colecciones ordenadas, lo que hace que puedas acceder a cualquier elemento en esa lista, simplemente al decirle a Python la posición. Para acceder a un elemento de una lista, escribe el nombre de la lista seguido por llaves cuadradas y dentro de estas el índice del contenido al que quieres acceder modifiquemos nuestro ejemplo para verlo:

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces[0])
```

Lo cual nos debería de regresar el elemento que estamos pidiendo

```python
angel
```

Ya que el contenido de una lista es un elemento individual puedes usar cualquiera de los métodos que vimos en el capítulo anterior cómo title(), modifiquemos nuestro ejemplo para ver como funcionaria:

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces[0].title())
```

Esto nos devolverá el mismo elemento pero ahora con la primera letra en mayúscula

```python
Angel
```

### Posición del index

Python (y muchos otros lenguajes de programación) siempre consideran el primer índice o index de una lista como cero, no uno. La razón es como se implementan las operaciones en las computadoras.

El segundo ítem en una lista tendrá el índice 1. Siguiendo este sistema puedes obtener cualquier elemento que quieras de la lista simplemente restando uno de su posición en la lista.

Por ejemplo si nosotros quisiéramos acceder al cuarto elemento de nuestra lista simplemente seleccionaremos el index 3.

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces[0])
print(peces[3])
```

Este código regresaría el primer y el ultimo pez de nuestra lista

```python
angel
payaso
```

Python tiene una sintaxis espacial para acceder a los valores desde atrás para adelante asi si quisiéramos acceder al último valor de nuestra lista simplemente ingresaríamos el índice *-1* ejemplo

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces[-1])
```

nos regresaría el último pez de la lista

```python
payaso
```

y así sucesivamente si quisiéramos entrar al penúltimo valor usamos el *-2*, al antepenúltimo el *-3* y así sucesivamente, ejemplo:

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
print(peces[-2])
print(peces[-3])
```

resultado:

```python
betta
guppy
```

### Usando un valor individual de una lista

Puedes usar un valor individual de una lista como cualquier otra variable por ejemplo, puedes usar un *f-string* para crear un mensaje basado en un valor de una lista.

modifica peces.py para que quede algo así:

```python
peces = ['angel', 'guppy', 'betta', 'payaso']
mensaje = f"Mi primer pez fue un {peces[2]}"

print(mensaje)
```

y obtendremos el siguiente resultado

```python
Mi primer pez fue un betta
```

### Ejercicios Listas

Intenta estos ejercicios para practicar la listas, crea un archivo por cada ejercicio:

1. **Nombres** guarda los nombres de algunos de tus amigos y familiares en una lista llamada nombres, y después imprime uno por uno los nombres de la lista.

2. **Saludos** comienza con lista del ejercicio pasado, solo que esta vez saluda a cada una de las personas, el texto del saludo debe ser el mismo para todos, pero cada mensaje debe estar personalizado con el nombre de la persona

3. **Lista Personal** piensa en una lista de tus alimentos favoritos, como manzana, donas, tacos, y usa tu lista para imprimir diferentes oraciones acerca de esos alimentos. como "Yo tengo antojo de tacos"

Cuando hayas terminado comapra tus resultados con tus compañeros o revisa mis [respuestas](https://github.com/dragaus/curso-python/tree/main/capitulo_1_bases/tema_3_introduccion_listas)

## Cambiando, Agregando, y Removiendo elementos

La mayoría de las listas que vayas a crear van a ser dinámicas, eso significa que vas a crear una lista y después vas a tener que agregar y eliminar elementos, en el transcurso de tu programa. Por ejemplo, quizá quieras crear un juego en donde debes disparar a unos aliens. Para eso debería de guardar un set inicial de aliens en una lista y después ir quitándolos cada vez que dispares a uno.Cada vez que uno aparece en pantalla debes agregar uno a tu lista. La lista de aliens va a incrementar o a disminuir en el transcurso del juego.

### Modificando elementos en una lista

La sintaxis para modificar una lista es similar a la sintaxis para acceder a un elemento en una lista. Para conseguirlo simplemente usa el nombre de la lista a la que quieres acceder con el índice del elemento que quieres cambiar, y después asigna un nuevo valor a ese elemento.

Por ejemplo pensemos que tenemos una lista de razas de perro, y el primer dato en la lista es *'labrador'*. Así cambiaríamos el valor:

```python
razas_perros = ['labrador', 'caniche', 'pitbull']
print(razas_perros)

razas_perros[0] = 'border collie'
print(razas_perros)
```

Podemos ver como en la lista teníamos el valor de *'labrador'* al principio pero lo cambiamos por *'border collie'*. El output que tenemos debería ser el siguiente:

```python
['labrador', 'caniche', 'pitbull']
['border collie', 'caniche', 'pitbull']
```

Puedes cambiar asi cualquier elemento de la lista

### Agregando elementos a una lista

Hay múltiples razones por las cuales necesites agregar elementos en una lista. Puedes querer que parezcan más enemigos en un juego, o agregar nueva información para unas gráficas, o agregar un nuevo usuario a un sitio web, etc. Python ofrece diferentes maneras de conseguir este objetivo.

#### Agregando elementos al final de una lista

La manera más sencilla de agregar un elemento a una lista es con **append()**, este método nos servirá para agregar un elemento al final de la lista, con el ejemplo anterior podemos demostrar esto con el siguiente código:

```python
razas_perros = ['labrador', 'caniche', 'pitbull']
print(razas_perros)

razas_perros.append('border collie')
print(razas_perros)
```

El método **append()** agrega *'border collie'* sin afectar al resto de elementos:

```python
['labrador', 'caniche', 'pitbull']
['labrador', 'caniche', 'pitbull', 'border collie']
```

Crear lista de manera dinámica se vuelve muy sencillo con **append()**. por ejemplo puedes empezar con una lista vacía e ir incorporando elementos con una serie de **append()**. Por ejemplo si quisiéramos replicar la lista del ejercicio anterior usaríamos el siguiente código:

```python
razas_perros = []

razas_perros.append('labrador')
razas_perros.append('caniche')
razas_perros.append('pitbull')
razas_perros.append('border collie')

print(razas_perros)
```

el resultado se veria exactamente igual que la lista en el ejercicio pasado

```python
['labrador', 'caniche', 'pitbull', 'border collie']
```

El crear listas de esta manera es muy comun ya que es comun que no sepas que elementos vas a alamacenar en el programa hasta que tu programa ya esta corrriendo.

#### Insetando elementos en una lista

Puedes agregar un objeto en la posicion que quieras de una lista simplemente usando el metodo **insert()**. Esto lo logras especificando el index del nuevo elemento, y el valor del nuevo elemento ejemplo:

```pyhton
razas_perros = ['labrador', 'caniche', 'pitbull']

razas_perros.insert(0, 'border collie')
print(razas_perros)
```

En el ejemplo lo que logramos es agregar *'border collie'* al principio de nuestra lista, y recorre los elementos en uno:

```python
['border collie', 'labrador', 'caniche', 'pitbull']
```

### Removiendo elementos de una lista

Así como agregar elementos es muy común también lo es eliminarlos. Como cuando destruyes un enemigo de un juego, o si un usuario decide cancelar su suscripción, en esos casos vas querer eliminar un elemento de una lista

#### Eliminando elementos por su índice

Si tu sabes la posición de item que quieres eliminar de una lista simplemente puedes usar **del**:

```python
razas_perros = ['labrador', 'caniche', 'pitbull']

del razas_perros[0]
print(razas_perros)
```

El codigo que estamos ejecutando elimina el primer ítem de la lista de razas_perros

```python
['labrador', 'caniche', 'pitbull']
['caniche', 'pitbull']
```

puedes eliminar cualquier elemento de la lista con **del** por ejemplo si nosotros quisiéramos borrar *'caniche'* simplemente deberíamos escoger el segundo índice

```python
razas_perros = ['labrador', 'caniche', 'pitbull']
print(razas_perros)

del razas_perros[1]
print(razas_perros)
```

y el segundo elemento de la lista es eliminado:

```python
['labrador', 'caniche', 'pitbull']
['labrador', 'pitbull']
```

En los dos ejemplos anteriores ya no puedes acceder de nuevo al valor eliminado.

#### Eliminando un elemento usando el método **pop()**

Hay veces en las que quieres trabajar con un elemento de una lista que acabas de eliminar de una lista. Por ejemplo si un usuario cancela su suscripción y quisieras ponerlo en una lista de usuarios inactivos. o si eliminas un enemigo y quieres usar su posición para comenzar una explosion en la posición donde se encontraba.

El método **pop()** quita el ultimo item de la lista. pero nos permite trabajar con ese elemento después de eliminarlo ejemplo:

```python
razas_perros = ['labrador', 'caniche', 'pitbull']
print(razas_perros)

perro_eliminado = razas_perros.pop()
print(razas_perros)
print(perro_eliminado)
```

Lo que estamos haciendo en el código es definir la lista razas_perros imprimirlas y cuando utilizamos el método **pop()** guardamos el valor que estamos eliminando en la variable perro_eliminado. Después volvemos a imprimir razas_perro y vemos que *'pitbull'* fue eliminado de la lista. Y después imprimimos de el perro_eliminado y vemos que podemos acceder el valor eliminado:

```python
['labrador', 'caniche', 'pitbull']
['labrador', 'caniche']
pitbull
```

Si quieres eliminar un elemento especifico de la lista con el metodo **pop()** lo unico que debes hacer es poner el indice del elemento entre los parentesis ejemplo:

```python
razas_perros = ['labrador', 'caniche', 'pitbull']
print(razas_perros)

perro_eliminado = razas_perros.pop(1)
print(razas_perros)
print(perro_eliminado)
```

Esto va a funcionar exactamente igual que el código anterior solo que al ahora especificar un índice el elemento que se selecciona para borrar es *'caniche'*

```python
['labrador', 'caniche', 'pitbull']
['labrador', 'pitbull']
caniche
```

### Ejercicios Modificando Listas

Haremos unos ejercicios en este caso serán un poco más complejos de lo que hemos hecho hasta ahora.

1. **Lista de Invitados** Piensa en un una lista de 3 personas que podrías invitar a una fiesta no importa si están vivas o muertas, Imprime un mensaje para cada una de ellas.

2. **Lista de Invitados Cambio** Te enteraste de que uno de los invitados no podrá ir a tu fiesta, entonces necesitas mandar nuevas invitaciones. Piensa en alguien más a invitar.

    * Empieza con el código del ejercicio 1. Agrega un **print()** al final del programa con el nombre de la persona que no lo podrá lograr.

    * Modifica tu lista, cambia el nombre de la persona que no lo lograra ir a la fiesta y pon el nombre del nuevo invitado.

    * Imprime un segundo grupo de invitaciones para tus nuevos invitados.

3. **Mas Invitados** Acabas de conseguir una mesa aún más grande y tienes espacio para invitar a 3 personas más a invitar.

    * Empieza con el código del ejercicio 2 y agrega un **print()** al final del código para informar a tus invitados que tienes una mesa más grande.

    * Utiliza **insert()** para agregar un nuevo invitado al principio de la lista

    * Utiliza **insert()** para agregar un nuevo invitado a la mitad de la lista

    * Utiliza **append()** para agregar a un nuevo invitado al final de tu lista

    * Imprime un nuevo grupo de invitaciones para tus nuevos invitados.

4. **Encogiendo la lista** Te enteraste de que tu mesa nueva no llegará hasta después de tu fiesta, y solo tienes espacio para 2 invitados.

    * Empieza con el código del ejercicio 3 y agrega un **print()** al final del código para informar a tus invitados que tienes un problema y que solo podrás invitar a 2 personas.

    * Utiliza **pop()** para eliminar un invitado de la lista de uno por uno y mandarle un mensaje de que no podrás invitarlo a la fiesta, hasta que solo queden 2 invitados.

    * Imprime un mensaje para cada uno de los invitados que aún están en la lista para hacerles saber que aun estan invitados.

    * Usa **del** para eliminar los últimos nombres de la lista. e imprime la lista para comprobar que no queda nadie en la lista.

Cuando hayas terminado compara tus resultados con tus compañeros o revisa mis [respuestas](https://github.com/dragaus/curso-python/tree/main/capitulo_1_bases/tema_3_introduccion_listas).

## Organizando una lista

Es muy común que las listas sean creadas de manera impredecible, ya que no siempre puedes controlar el orden en el cual los usuarios van a proveer la información, A pesar de que es inevitable en la mayoría de las circunstancias, frequentemente necesitaremos presentar la información en un orden en particular.

Python nos provee de un número de diferentes formas de organizar la lista dependiendo la situación.

### Organizando una lista permanentemente con sort

El método **sort()** hace relativamente fácil el organizar una lista Imagina que nosotros tenemos una lista de aves y quieres cambiar el orden de la lista para guardarla de manera alfabética. Para mantenerlo simple vamos a suponer que todos los valores de la lista están minúscula.

```python
aves = ['tucan', 'canario', 'perico', 'cuervo']
aves.sort()
print(aves)
```

El método **sort()**cambiará el orden de la lista permanentemente, la lista de las aves ahora está en orden alfabético y nunca se podrá revertir al orden original.

```python
['canario', 'cuervo', 'perico', 'tucan']
```

También puedes usar **sort()** para ordenar los elementos en orden alfabético inverso, simplemente pasando el argumento *reverse=True* al método **sort()**, el siguiente ejemplo ordena la misma lista en orden inverso:

```python
aves = ['tucan', 'canario', 'perico', 'cuervo']
aves.sort(reverse=True)
print(aves)
```

Nuevamente el orden es cambiado permanentemente:

```python
['tucan', 'perico', 'cuervo', 'canario']
```

### Organizando una lista temporalmente con sorted

Para mantener el orden original de la lista pero presentándola de una manera ordenada, podemos usar la función **sorted()**. La función **sorted()** te permite mostrar una lista en un orden en particular sin modificar la lista principal.

Veámoslo en el ejemplo de las aves:

```python
aves = ['tucan', 'canario', 'perico', 'cuervo']

print("Este es el orden original de la lista")
print(aves)

print("Aqui esta la lista ordenada")
print(sorted(aves))

print("Aqui esta la lista original de nuevo")
print(aves)
```

Primero imprimimos el orden original de la lista, después la ordenamos de manera alfabética con **sorted()** la lista y la imprimimos, para finalmente volver a mostrar que la lista original no sufrío ningún cambio.

```python
Este es el orden original de la lista
['tucan', 'canario', 'perico', 'cuervo']
Aqui esta la lista ordenada
['canario', 'cuervo', 'perico', 'tucan']
Aqui esta la lista original de nuevo
['tucan', 'canario', 'perico', 'cuervo']
```

**Nota** Ordenar de manera alfabética es bastante más complejo cuando los valores no están en minúscula. Hay diferentes maneras de interpretar las letras mayúsculas, y es un tema que podría ser demasiado complejo por el momento, sin embargo la mayoría de los acercamientos para ordenar se construyen con lo que hemos aprendido hasta ahora.

### Imprimiendo una lista en orden inverso

Para invertir una lista nosotros podemos usar el método **reverse()**. Si nosotros agregamos las aves en función de cuando la fuimos viendo, nosotros podemos sencillamente revertir ese orden:

```python
aves = ['tucan', 'canario', 'perico', 'cuervo']

print(aves)

aves.reverse()
print(aves)
```

Observa como **reverse()** revierte la lista en el orden en que se fueron agregando los elementos.

```python
['tucan', 'canario', 'perico', 'cuervo']
['cuervo', 'perico', 'canario', 'tucan']
```

El método **reverse()** invierte la lista de manera permanente pero regresar a la lista original es tan fácil como volver a aplicar el método **reverse()**.

### Encontrando la longitud de una lista

Tu puedes saber rápidamente la longitud de una lista usando la función **len()**. La lista de nuestro ejemplo tiene cuatro elementos por lo tanto su longitud es 4:

```python
>>> aves = ['tucan', 'canario', 'perico', 'cuervo']
>>> len(aves)
4
```

Esta función verás que es muy útil en diferentes momentos. por ejemplo cuando quieres saber el número total de enemigos que aún quedan en la pantalla, o cuando quieres saber la cantidad de transacción de una semana, o cuantos usuarios registrados tienes en tu página web.

### Ejercicios Organización

1. **Ver Mundo** piensa en al menos cinco lugares del mundo que te gustaría visitar.

    * Guarda las ubicaciones en una lista con minúsculas. Asegurate de que la lista no está ordenada alfabéticamente.

    * Imprime la lista en su orden original, no te preocupes por que se vea lindo con que imprimas la lista esta bien.

    * Usa **sorted()** para imprimir la lista en orden alfabético sin modificar la lista.

    * Muestra que tu lista sigue sin ser modificada.

    * Usa **sorted()** para imprimir la lista de orden alfabético inverso sin modificar la lista.

    * Muestra que tu lista sigue sin ser modificada.

    * Usa **reverse()** para cambiar el orden cronológico de tu lista, e imprimelo.

    * Usa **reverse()** para cambiar reordenar cronológicamente tu lista, e imprimelo.

    * Usa **sort()** para ordenar alfabéticamente, y de manera definitiva la lista, e imprime el resultado.

    * Usa **sort()** para ordenar alfabeticamente inverso, y de manera definitiva la lista, e imprime el resultado.

2. **Invitados Fiesta** selecciona del ejercicio 1 al 3 de **Ejercicios Modificando Listas** para usar la función **len()** y conocer el número de invitados a la fiesta.

Cuando hayas terminado compara tus resultados con tus compañeros o revisa mis [respuestas](https://github.com/dragaus/curso-python/tree/main/capitulo_1_bases/tema_3_introduccion_listas).
