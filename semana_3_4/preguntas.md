## 8. Preguntas Tipo Entrevista / Examen Universitario

Al terminar la semana, practicá respondiendo estas preguntas por escrito o en voz alta (como si le explicaras a un alumno):

1. ¿Cuál es la diferencia entre `=` y `==` en Python? ¿Por qué es importante?
2. ¿Qué devuelve `10 % 3`? ¿Para qué sirve el operador módulo en la práctica?
3. ¿Por qué `input()` siempre devuelve un string y cuándo es un problema?
4. Explicá con una analogía la diferencia entre un bucle `for` y un bucle `while`. ¿Cuándo usarías cada uno?
5. ¿Qué pasa si una condición `while` nunca se vuelve `False`? ¿Cómo se evita?
6. ¿Qué es una rama en Git y por qué es útil trabajar con ramas en un equipo?

1. La diferencia entre "=" y "==" es que "=" corresponde al signo igual para asignar un valor a una variable, mientras que "==" corresponde al operador para comparar dos valores.
2. 10%3 devuelve 1; el operador módulo sirve para realizar una división y devolver el resto de la misma; en la práctica se suele usar para evaluar si un número es par o si es divisible por otro.
3. Porque es una función que devuelve lo que el usuario ingrese, con tipo de datos cadena; esto es un problema si pedimos un número, y pretendemos operar con el valor ingresado sin convertirlo a int o float.
4. For sirve para iterar sobre un conjunto de elementos, mientras que while es un bucle que se repetirá mientras una condición sea verdadera. Por ejemplo, para mostrar una opción de menú por cada día de la semana, me sirve más for porque ya sé la cantidad de días de la semana y quiero iterar sobre ellos ejecutando una instrucción en c/u. En cambio, para mantener encendido el riego automático de plantas mientras el tiempo sea caluroso, me sirve más el while para evaluar constantemente la condición "tiempo caluroso" y detener el bucle cuando sea falsa.
5. Si la condición while nunca se vuelve falsa, quedamos atrapados adentro del bucle infinito, que puede tildar el sistema. Para evitarlo hay que asegurarse que algo genere el cambio de esa condición. 
6. Una rama en Git es como una bifurcación que sale sobre el proyecto original, y en la que pueden realizarse modificaciones o agregados, que momentáneamente no afectan o impactan al proyecto original por fuera de la rama, hasta que el contenido esté listo para revisarse y unificarse al proyecto principal. Permite preparar algo en prueba sin modificar todo hasta que no esté completo el nuevo módulo o agregado, y también que distintos programadores trabajen en paralelo sobre distintos agregados. 
