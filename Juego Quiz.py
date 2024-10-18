def menu():
    opc = 1  # Se inicializa con un valor distinto a 0 para entrar en el while

    while(opc != 0):
        print("\n\t\t....Bienvenido a Preguntas y Respuestas....")
        print("\n\t\t\t.:MENU:.\n")
        print("\t1. Iniciar juego")
        print("\t2. Ver instrucciones")
        print("\t0. Salir")
        opc = int(input("\tDigite la opcion a realizar: "))

        if(opc == 1):       #Opcion para iniciar el cuestionario/Quiz
            cuestionario()
        elif(opc == 2):     #Opcion para mostrar las instrucciones
            instrucciones()
        elif(opc == 0):     #Opcion para salir de la aplicacion
            print("\n\t\tGracias por usar mi app!!!\n\n")
            print("\t.:FIN DEL PROGRAMA:.\n")
        else:
            print("\n\t\t.:OPCION INCORRECTA:.\n")      #Mostrar si la opcion es incorrecta

def cuestionario():
    print("\tBienvenido a nuestro Quiz!!!\n")
    puntaje = 0  # Inicializamos el puntaje

    # Pregunta 1
    print("Pregunta #1:\n¿Que muestra el siguiente codigo en pantalla?")
    print("print(5 + 3 * 2)")
    print(" A. 16\n B. 11\n C. 13\n D. 10")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "B":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era B.\n")

    # Pregunta 2
    print("\nPregunta #2:\n¿Cual de las siguientes es una estructura de control en Python?")
    print(" A. if\n B. loop\n C. iterate\n D. method")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "A":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era A.\n")

    # Pregunta 3
    print("\nPregunta #3:\n¿Que comando se usa para ver el estado actual de los archivos en Git?")
    print(" A. git status\n B. git show\n C. git pull\n D. git add")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "A":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era A.\n")

    # Pregunta 4
    print("\nPregunta #4:\n¿Cual es el valor de la variable x despues de ejecutar el siguiente codigo?")
    print(" x = 10\n x += 5\n x -= 3")
    print(" A. 8\n B. 12\n C. 13\n D. 10")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "B":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era B.\n")

    # Pregunta 5
    print("\nPregunta #5:\n¿Que muestra el siguiente codigo en Python?")
    print("for i in range(3):\n    print(i)")
    print(" A. 1 2 3\n B. 0 1 2\n C. 0 1 2 3\n D. Error de sintaxis")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "B":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era B.\n")

    # Pregunta 6
    print("\nPregunta #6:\n¿Cual es el proposito del comando git push?")
    print(" A. Enviar cambios al servidor remoto\n B. Traer cambios desde el servidor remoto\n C. Combinar ramas\n D. Inicializar un repositorio")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "A":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era A.\n")

    # Pregunta 7
    print("\nPregunta #7:\n¿Cual es la instruccion para leer datos desde el teclado en PSeInt?")
    print(" A. Escribir\n B. Leer\n C. Mostrar\n D. Input")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "B":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era B.\n")

    # Pregunta 8
    print("\nPregunta #8:\n¿Cuál es la estructura condicional utilizada en PSeInt para tomar decisiones?")
    print(" A. Mientras\n B. Hacer\n C. Si\n D. Segun")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "C":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era C.\n")

    # Pregunta 9
    print("\nPregunta #9:\n¿Cual es el comando para mostrar mensajes en pantalla en PSeInt?")
    print(" A. imprimir\n B. escribir\n C. mostrar\n D. leer")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "B":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era B.\n")

    # Pregunta 10
    print("\nPregunta #10:\n¿Cual de las siguientes estructuras se usa para crear bucles tipo while en PSeInt?")
    print(" A. mientras\n B. Si\n C. Entonces\n D. Caso")
    respuesta = input("Escribe la letra de tu respuesta: ").upper()
    if respuesta == "A":
        print("¡Correcto!\n")
        puntaje += 1
    elif respuesta !="A" or respuesta !="B" or respuesta !="C" or respuesta !="D":
        print(f"El dato es diferente de las opciones 'A, B, C o D' digitaste {respuesta}")
        print("\t.:PENITENCIA -1 PUNTO:.")
        puntaje -= 1
    else:
        print("Incorrecto. La respuesta correcta era A.\n")
    if puntaje < 0:
        print("\n\n\t\t.:No pasaste satisfactoriamente la prueba:.\n")
    else:
        calcularPuntaje(puntaje, 10)#enviamos el puntaje y total de preguntas

def calcularPuntaje(puntaje, totalPreguntas):
    porcentaje = (puntaje / totalPreguntas) * 100   #Calculo del puntaje
    if porcentaje >= 60:
        print(f"¡Aprobaste con un {porcentaje}%! Puntaje total: {puntaje} de {totalPreguntas}")
    else:
        print(f"No aprobaste. Puntaje total: {puntaje} de {totalPreguntas} ({porcentaje}%)")

def instrucciones():        #Instrucciones del Juego tipo Quiz
    print("\n\n\t\t.:INSTRUCCIONES:.\n")
    print("\t1. Elige la opcion correcta para cada pregunta.")
    print("\t2. Responde con A, B, C o D. O recibira una penitencia de -1 punto")
    print("\t3. Necesitas al menos 6 respuestas correctas para aprobar.\n")

menu()
