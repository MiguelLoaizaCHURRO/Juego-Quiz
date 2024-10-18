Algoritmo PreguntasYRespuestas
    Definir opc Como Entero
    Definir puntaje Como Entero
    Definir totalPreguntas Como Entero
    Definir porcentaje Como Real
	
    opc = 1  // Inicializamos opc diferente de 0 para entrar en el bucle
	
    Mientras opc <> 0 Hacer
        Escribir "....Bienvenido a Preguntas y Respuestas...."
        Escribir ".:MENU:."
        Escribir "1. Iniciar juego"
        Escribir "2. Ver instrucciones"
        Escribir "0. Salir"
        Leer opc
		
        Segun opc Hacer
            Caso 1:
                Cuestionario() // Llamamos a la función Cuestionario
            Caso 2:
                Instrucciones() // Llamamos a la función Instrucciones
            Caso 0:
                Escribir "Gracias por usar mi app!!!"
                Escribir ".:FIN DEL PROGRAMA:."
            De Otro Modo:
                Escribir ".:OPCION INCORRECTA:."
        FinSegun
    FinMientras
FinAlgoritmo

SubProceso Cuestionario
    Definir puntaje Como Entero
    puntaje = 0
	
    // Pregunta 1
    Escribir "Pregunta #1:¿Que muestra el siguiente codigo en pantalla?"
    Escribir "print(5 + 3 * 2)"
    Escribir " A. 16 B. 11 C. 13 D. 10"
    Leer respuesta
    Si respuesta = "B" o respuesta = "b" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era B."
    FinSi
	
    // Pregunta 2
    Escribir "Pregunta #2:¿Cual de las siguientes es una estructura de control en Python?"
    Escribir " A. if B. loop C. iterate D. method"
    Leer respuesta
    Si respuesta = "A" o respuesta = "a" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era A."
    FinSi
	
    // Pregunta 3
    Escribir "Pregunta #3:¿Que comando se usa para ver el estado actual de los archivos en Git?"
    Escribir " A. git status B. git show C. git pull D. git add"
    Leer respuesta
    Si respuesta = "A" o respuesta = "a" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era A."
    FinSi
	
    // Pregunta 4
    Escribir "Pregunta #4:¿Cual es el valor de la variable x despues de ejecutar el siguiente codigo?"
    Escribir " x = 10 x += 5 x -= 3;"
    Escribir " A. 8 B. 12 C. 13 D. 10"
    Leer respuesta
    Si respuesta = "B" o respuesta = "b" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era B."
    FinSi
	
    // Pregunta 5
    Escribir "Pregunta #5:¿Que muestra el siguiente codigo en Python?"
    Escribir "for i in range(3):    print(i)"
    Escribir " A. 1 2 3 B. 0 1 2 C. 0 1 2 3 D. Error de sintaxis"
    Leer respuesta
    Si respuesta = "B" o respuesta = "b" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era B."
    FinSi
	
    // Pregunta 6
    Escribir "Pregunta #6:¿Cual es el proposito del comando git push?"
    Escribir " A. Enviar cambios al servidor remoto B. Traer cambios desde el servidor remoto C. Combinar ramas D. Inicializar un repositorio"
    Leer respuesta
    Si respuesta = "A" o respuesta = "a" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era A."
    FinSi
	
    // Pregunta 7
    Escribir "Pregunta #7:¿Cual es la instruccion para leer datos desde el teclado en PSeInt?"
	Escribir " A. Escribir B. Leer C. Mostrar D. Input"
	Leer respuesta
	Si respuesta = "B" o respuesta = "b" Entonces
		Escribir "¡Correcto!"
		puntaje = puntaje + 1
	SiNo
		Escribir "Incorrecto. La respuesta correcta era B."
	FinSi
	
    // Pregunta 8
    Escribir "Pregunta #8:¿Cual es la estructura condicional utilizada en PSeInt para tomar decisiones?"
    Escribir " A. Mientras B. Hacer C. Si D. Segun"
    Leer respuesta
    Si respuesta = "C" o respuesta = "c" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era C."
    FinSi
	
    // Pregunta 9
    Escribir "Pregunta #9:¿Cual es el comando para mostrar mensajes en pantalla en PSeInt?"
    Escribir " A. imprimir B. escribir C. mostrar D. leer"
    Leer respuesta
    Si respuesta = "B" o respuesta = "b" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era B."
    FinSi
	
    // Pregunta 10
    Escribir "Pregunta #10:¿Cual de las siguientes estructuras se usa para crear bucles en PSeInt?"
    Escribir " A. Para B. Si C. Entonces D. Caso"
    Leer respuesta
    Si respuesta = "A" o respuesta = "a" Entonces
        Escribir "¡Correcto!"
        puntaje = puntaje + 1
    SiNo
        Escribir "Incorrecto. La respuesta correcta era A."
    FinSi
	
    CalcularPuntaje(puntaje, 10)
FinSubProceso

SubProceso CalcularPuntaje(puntaje, totalPreguntas)
    Definir porcentaje Como Real
	
    porcentaje = (puntaje / totalPreguntas) * 100
	
    Si porcentaje >= 60 Entonces
        Escribir "¡Aprobaste con un ", porcentaje, "%! Puntaje total: ", puntaje, " de ", totalPreguntas
    SiNo
        Escribir "No aprobaste. Puntaje total: ", puntaje, " de ", totalPreguntas, " (", porcentaje, "%)"
    FinSi
FinSubProceso

SubProceso Instrucciones
    Escribir ".:INSTRUCCIONES:."
    Escribir "1. Elige la opción correcta para cada pregunta."
    Escribir "2. Responde con A, B, C o D."
    Escribir "3. Necesitas al menos 6 respuestas correctas para aprobar."
FinSubProceso
