from random import randint

# TODO: Falta una condición de perder, imprimir en colores
# y cosas extras quizás, falta imprimir las instrucciones.
# también explicar que se puede construir en espacios
# vacíos.


def print_en_colores(texto, color):
    """
    Imprime un texto en un color a escogencia del programador.

    ENTRADAS:
    :str texto: Un texto que será utilizado para ser impreso.
    :str color: Un parámetro que representa el color a imprimir.
    SALIDAS:
    No hay salidas. Es una función que imprime en pantalla.
    RESTRICCIONES:
    No existen restricciones específicas.
    """
    # Si el color es "r" quiere decir red. Se imprimirá en rojo.
    if color == "r":
        print("\33[31m" + texto + "\033[0m")
    # Si el color es "g" quiere decir red. Se imprimirá en verde.
    elif color == "g":
        print("\33[32m" + texto + "\033[0m")
    # Si el color es "b" quiere decir blue. Se imprimirá en azul.
    elif color == "b":
        print("\33[34m" + texto + "\033[0m")
    # Si el color es "y" quiere decir yellow. Se imprimirá en amarillo.
    elif color == "y":
        print("\33[33m" + texto + "\033[0m")
    # Si el color es "v" quiere decir violet. Se imprimirá en violeta.
    elif color == "v":
        print("\33[35m" + texto + "\033[0m")


def en_lista(elemento, lista):
    """
    Revisa si un elemento está dentro de una lista.

    ENTRADAS:
    :str/int elemento: Un elemento que se desea encontrar.
    :list lista: Una lista que contiene el elemento a revisar.

    SALIDAS:
    Un booleano que representa si el elemento está en lista.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Comienza un ciclo para cada elemento de la lista.
    for i in range(len(lista)):
        # Si el elemento en la posición de iterador en la lista
        # es igual, se retornará True.
        if elemento == lista[i]:
            return True
    # Si el ciclo termina, se retornará False.
    return False


def preguntar_texto(mensaje, opciones):
    """
    Pregunta un texto y revisa si la respuesta está
    en las opciones.

    ENTRADAS:
    : str mensaje: Un mensaje personalizado.
    : list opciones: Una lista que contiene las opciones correctas.

    SALIDAS:
    La opción seleccionada por el usuario.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se entra en un ciclo hasta dar con la respuesta.
    while True:
        # Se pregunta con el mensaje.
        ask_option = input(mensaje)
        # Si la opción no está en las opciones, se vuelve al ciclo.
        if en_lista(ask_option, opciones) is False:
            print("Error: Inserte una opción válida porfavor.")
            continue
        # De no ser así, se rompe el ciclo.
        else:
            break
    # Se regresa la opción elegida.
    return ask_option


def generar_tablero():
    """
    Generar el tablero del juego.

    ENTRADAS:
    No hay entradas. Solo se genera el tablero.

    SALIDAS:
    El tablero generado.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se crea una lista con opciones válidas.
    opciones_validas = [str(i) for i in range(3, 101)]
    # Se crean dos iteradores.
    i = 0
    j = 0
    # Se crea un resultado para el tablero.
    res_tablero = []
    # Se crea un resultado para cada fila.
    res_fila = []

    # Generar filas.
    while True:
        # Se pregunta al usuario por las filas.
        ask_rows = input("Inserte el número de filas: ")
        # Si la opción no está entre las opciones válidas,
        # se vuelve a preguntar.
        if en_lista(ask_rows, opciones_validas) is False:
            print("Error: La cantidad de filas debe ser un número mayor o "
                  "igual que tres.")
            continue
        # De no ser así, se puede continuar.
        else:
            break

    # Generar columnas.
    while True:
        # Se pregunta al usuario por las columnas.
        ask_columns = input("Inserte el número de columnas: ")
        # Si la opción no está entre las opciones válidas,
        # se vuelve a preguntar.
        if en_lista(ask_columns, opciones_validas) is False:
            print("Error: La cantidad de filas debe ser un número mayor o "
                  "igual que tres.")
            continue
        # De no ser así, se puede continuar.
        else:
            break

    # Generar tablero.

    # Se recorra según la cantidad de filas.
    while i < int(ask_rows):
        # Se recorre según la cantidad de columnas.
        while j < int(ask_columns):
            # Se agrega a la lista de fila espacío vacío.
            res_fila += ["  "]
            # El contador de columna aumenta en uno.
            j += 1
        # Se le agrega a la lista de tablero el resultado de fila.
        res_tablero += [res_fila]
        # Se resetea al resultado de fila.
        res_fila = []
        # El contador de fila aumenta en uno.
        i += 1
        # El contador de columna se resetea a cero.
        j = 0
    # Se retorna el resultado del tablero.
    return res_tablero


def generar_tablero_semillas(tablero):
    """
    Generar el tablero de las semillas.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    El tablero de semillas generado.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se crea un resultado para el tablero.
    resultado = []
    # Se crea un resultado para cada fila.
    resultado_fila = []
    # Se crean dos iteradores.
    i = 0
    j = 0

    # Generar tablero de semillas.

    # Se recorra según la cantidad de filas.
    while i < len(tablero):
        # Se recorre según la cantidad de columnas.
        while j < len(tablero[0]):
            # Se agrega a la lista de fila espacío vacío.
            resultado_fila += [" "]
            # El contador de columna aumenta en uno.
            j += 1
        # Se le agrega a la lista de tablero el resultado de fila.
        resultado += [resultado_fila]
        # Se resetea al resultado de fila.
        resultado_fila = []
        # El contador de fila aumenta en uno.
        i += 1
        # El contador de columna se resetea a cero.
        j = 0
    # Se retorna el resultado del tablero de semillas.
    return resultado


def revisar_tablero_semillas(tablero, tablero_semillas):
    """
    Revisa cuando una semilla está en el tablero
    y cual es su condición.

    ENTRADAS:
    :list tablero: El tablero del juego.
    :list tablero_semillas: El tablero de la condición de semillas.

    SALIDAS:
    El tablero de la condición de las semillas después
    de ser revisado.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Comienza un ciclo para revisar todas las condiciones del tablero.
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            # Si en la posición del tablero hay una semilla y en el tablero
            # de semillas se encuentra espacio vacío entonces se reemplaza por
            # False (F).
            if tablero[i][j] == "🌱" and tablero_semillas[i][j] == " ":
                tablero_semillas[i][j] = "F"
            # Si en la posición del tablero hay una semilla y en el tablero
            # de semillas se encuentra False (F) entonces se reemplaza por True
            # (T). Esto para poder eclosionar la semilla luego.
            elif tablero[i][j] == "🌱" and tablero_semillas[i][j] == "F":
                tablero_semillas[i][j] = "T"
            # Cuando en la posición del tablero de semillas se encuentra
            # True (T) entonces se reemplaza por espacío vacío.
            elif tablero_semillas[i][j] == "T":
                tablero_semillas[i][j] = " "
    # Se retorna el tablero de semillas.
    return tablero_semillas


def revisar_tablero(tablero, tablero_semillas):
    """
    Revisa cuando una semilla eclosiona.

    ENTRADAS:
    :list tablero: El tablero del juego.
    :list tablero_semillas: El tablero de la condición de semillas.

    SALIDAS:
    El tablero después de haber eclosionado las semillas.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se recorre el tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            # Si en el tablero hay una semilla y en el tablero de semillas
            # la condición de eclosión es T (True) entonces, se cambia la
            # semilla por una flor.
            if tablero[i][j] == "🌱" and tablero_semillas[i][j] == "T":
                tablero[i][j] = "🌻"
    # Se regresa el tablero una vez revisado.
    return tablero


def revisar_victoria(tablero):
    """
    Revisa cuando el usuario haya ganado.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    Un booleano que revisa si el usuario ganó.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Revisar filas: Si alguna fila está llena de plantas
    # significa que el usuario ganó.
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if j == len(tablero[0]) - 1:
                if tablero[i][j] == "🌻":
                    return True
            else:
                if tablero[i][j] != "🌻":
                    break
    # Revisar columnas: Si alguna columna está llena de plantas
    # significa que el usuario ganó.
    for j in range(len(tablero[0])):
        for i in range(len(tablero)):
            if i == len(tablero) - 1:
                if tablero[i][j] == "🌻":
                    return True
            else:
                if tablero[i][j] != "🌻":
                    break
    # Si se revisa fila y columnas y ninguna está llena de plantas
    # se retornará False.
    return False


def imprimir_tablero(tablero):
    """
    Imprime el tablero del juego.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    No hay salidas. Solo imprime el tablero del juego.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    print()
    for k in range(len(tablero[0])):
        if k == 0:
            print("   "+str(k+1), end="  ")
        else:
            print(k+1, end="  ")
    print()
    # Se recorre el tablero para imprimirlo.
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if j == len(tablero[0]) - 1:
                print(tablero[i][j])
            else:
                if j == 0:
                    print(str(i+1)+" "+tablero[i][j], end="|")
                else:
                    print(tablero[i][j], end="|")
        if i != len(tablero) - 1:
            print(" ", end=" ")
            print("-"*3*len(tablero[0]))
    print()


def generar_opciones_fila(tablero):
    """
    Genera las opciones válidas para la fila.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    Una lista que contiene las opciones válidas
    para escoger una fila.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se crea una lista con las opciones de fila. Comienza vacía.
    opciones_fila = []
    # Se hará un ciclo donde se agrega todas las filas válidas.
    for i in range(1, len(tablero)+1):
        opciones_fila += [str(i)]
    # Se retornara la lista de opciones de fila.
    return opciones_fila


def generar_opciones_columna(tablero):
    """
    Genera las opciones válidas para la columna.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    Una lista que contiene las opciones válidas
    para escoger una columna.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se crea una lista con las opciones de columna. Comienza vacía.
    opciones_columna = []
    # Se hará un ciclo donde se agrega todas las columnas válidas.
    for i in range(1, len(tablero[0])+1):
        opciones_columna += [str(i)]
    # Se retornara la lista de opciones de columna.
    return opciones_columna


def imprimir_informacion():
    """
    Imprimir la información de los símbolos.

    ENTRADAS:
    No hay entradas. Solo imprime los símbolos.

    SALIDAS:
    No hay salidas. Solo imprime los símbolos.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se pregunta al usuario si desea saber el significado los símbolos.
    ask_meaning = preguntar_texto("¿Desea saber el significado de los "
                                  "símbolos? (s/n): ", ["s", "n"])
    # Si la respuesta es sí (s) se imprimirá el tablero.
    if ask_meaning == "s":
        print()
        print("---USUARIO---")
        print("🌱: Semilla\n🌻: Planta\n🚲: Ciclovia")
        print("-----CPU-----")
        print("🚧: Concreto\n")
    # De no ser así, no se imprimirá el tablero.
    else:
        print()


def turno_computador(tablero):
    """
    El computador toma la decisión de donde construir.

    ENTRADAS:
    :list tablero: El tablero del juego.

    SALIDAS:
    El tablero modificado donde se construyó.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Un iterador que irá cambiando.
    iterador = 0
    # La lista de opciones usadas.
    opciones_usadas = []
    # El tope de plantas.
    tope = randint(0, len(tablero) // 2)
    # Se entrará en un ciclo siempre que el iterador
    # sea menor que el tope.
    while iterador < tope:
        # Condición de repetir.
        repeat_condition = False
        # Variables temporales de fila y columna.
        tmp_fila = randint(0, len(tablero)-1)
        tmp_columna = randint(0, len(tablero[0])-1)
        # Se revisa las opciones utilizadas, si la fila y
        # columna ya fueron seleccionados, se repite el
        # ciclo.
        for i in range(len(opciones_usadas)):
            if (opciones_usadas[i][0] == tmp_fila and
                    opciones_usadas[i][1] == tmp_columna):
                repeat_condition = True
        # Si la condición de repetición es True, se continua
        # el ciclo y el iterador se mantiene.
        if repeat_condition is True:
            continue
        # De no ser así, se buscará la posición y el objeto
        # que se encuentre en esa posición.
        else:
            # Si la posición es una planta, se agregará a las
            # opciones usadas y el iterador se mantiene.
            if tablero[tmp_fila][tmp_columna] == "🌱":
                opciones_usadas += [[tmp_fila, tmp_columna]]
                continue
            # En cualquier otro caso, se agregará a las opciones
            # usadas y el iterador aumentará en uno.
            else:
                # Si la posición es una ciclovia, se cambiará
                # la posición por un espacio vacío.
                if tablero[tmp_fila][tmp_columna] == "🚲":
                    tablero[tmp_fila][tmp_columna] = "  "
                    print("La muni ha quitado la ciclovía (🚲) en la posición "
                          "({}, {}).".format(tmp_fila+1, tmp_columna+1))
                # Si la posición es una planta, se cambiará
                # la posición por concreto.
                elif tablero[tmp_fila][tmp_columna] == "🌻":
                    tablero[tmp_fila][tmp_columna] = "🚧"
                    print("La muni ha quitado la planta (🌻) en la posición "
                          "({}, {}).".format(tmp_fila+1, tmp_columna+1))
                # Si la posición es un espacío vacío, se cambiará
                # la posición por concreto.
                elif tablero[tmp_fila][tmp_columna] == "  ":
                    tablero[tmp_fila][tmp_columna] = "🚧"
                    print("La muni ha construido en la posición "
                          "({}, {}).".format(tmp_fila+1, tmp_columna+1))
                opciones_usadas += [[tmp_fila, tmp_columna]]
                iterador += 1
    # Se retorna el tablero modificado.
    return tablero


def turno_usuario(fila, columna, tablero):
    """
    El usuario toma la decisión de donde plantar.

    ENTRADAS:
    :int fila: La fila a modificar.
    : int columna: La columna a modificar.
    :list tablero: El tablero del juego.

    SALIDAS:
    El tablero modificado donde se plantó.

    RESTRICCIONES:
    Las restricciones son revisadas por la función que se encargue
    de llamar a esta función.
    """
    # Se pregunta al usuario que desea colocar.
    ask_option = preguntar_texto("\ns: semilla\np: planta\nc: ciclovia\n"
                                 "\nInserte que desea colocar: ",
                                 ["s", "p", "c"])
    # Si la respuesta es semilla (s) se coloca una semilla.
    if ask_option == "s":
        tablero[fila][columna] = "🌱"
        return tablero
    # Si la respuesta es planta (p) se coloca una planta.
    elif ask_option == "p":
        tablero[fila][columna] = "🌻"
        return tablero
    # Si respuesta es ciclovia (c) se coloca ciclovia.
    else:
        # Se toma la decisión de si se coloca horizontal
        # o vertical la ciclovia.
        horizontal_o_vertical = randint(0, 1)
        # Si la respuesta es cero, se colocará horizontal.
        if horizontal_o_vertical == 0:
            # Moverse a la izquierda de la fila.
            for i in reversed(range(0, columna)):
                # Si se encuentra una planta o una semilla.
                # Se deja de poner ciclovía.
                if tablero[fila][i] == "🌻" or tablero == "🌱":
                    break
                # De no ser así, se colocará ciclovia.
                else:
                    tablero[fila][i] = "🚲"

            # Moverse a la derecha de la fila.
            for i in range(columna, len(tablero[0])):
                # Si se encuentra una planta o una semilla.
                # Se deja de poner ciclovía.
                if tablero[fila][i] == "🌻" or tablero[fila][i] == "🌱":
                    break
                # De no ser así, se colocará ciclovia.
                else:
                    tablero[fila][i] = "🚲"
        # Si la respuesta es uno, se colocará vertical.
        else:
            # Moverse abajo de la columna.
            for i in reversed(range(0, fila)):
                # Si se encuentra una planta o una semilla.
                # Se deja de poner ciclovía.
                if tablero[i][columna] == "🌻" or tablero == "🌱":
                    break
                # De no ser así, se colocará ciclovia.
                else:
                    tablero[i][columna] = "🚲"

            # Moverse arriba de la columna.
            for i in range(fila, len(tablero)):
                # Si se encuentra una planta o una semilla.
                # Se deja de poner ciclovía.
                if tablero[i][columna] == "🌻" or tablero[i][columna] == "🌱":
                    break
                # De no ser así, se colocará ciclovia.
                else:
                    tablero[i][columna] = "🚲"
        # Se retorna el tablero modificado.
        return tablero


def menu():
    """
    El menu principal del juego.

    ENTRADAS:
    No hay entradas. No se necesita de algún parámetro.

    SALIDAS:
    No hay salidas. El tablero se irá modificando por turnos.

    RESTRICCIONES:
    Las restricciones son revisadas en cada parte del programa.
    """
    # Se comienza un ciclo para  comenzar el juego.
    while True:
        # Se genera el tablero.
        tablero = generar_tablero()
        # Se genera el tableor de las semillas.
        tablero_semillas = generar_tablero_semillas(tablero)
        # Se generan las opciones válidas de fila y columna.
        opciones_fila = generar_opciones_fila(tablero)
        opciones_columna = generar_opciones_columna(tablero)
        # Se genera el iterador para contar los días.
        iterador = 1
        # Se imprime la información de los símbolos.
        imprimir_informacion()
        # Se genera un ciclo para continuar el juego.
        while True:
            # Se imprime información del tablero y del día.
            print("-----DÍA #{}-----".format(iterador))
            imprimir_tablero(tablero)
            # Si se revisa que la condición de victoria es True,
            # se imprime que el usuario ganó y se pregunta si
            # desea volver a jugar, se rompe este ciclo.
            if revisar_victoria(tablero) is True:
                print_en_colores("¡Felicidades por la victoria!", "g")
                ask_decision = preguntar_texto("¿Desea volver a jugar? "
                                               "(s/n): ", ["s", "n"])
                break
            # De no ser así, el juego seguirá continuando.
            else:
                # Comienza un ciclo para que el usuario defina la
                # fila y columna.
                while True:
                    # Se escoge la fila.
                    escoger_fila = int(preguntar_texto(
                        "Inserte una fila: ", opciones_fila))
                    # Se escoge la columna.
                    escoger_columna = int(preguntar_texto(
                        "Inserte una columna: ", opciones_columna))
                    # Se pregunta al usuario si está seguro de su decisión.
                    ask_correct = preguntar_texto(
                        "¿Está seguro de su decisión? (s/n): ", ["s", "n"])
                    # Si la respuestá es sí (s) entonces se puede seguir.
                    if ask_correct == "s":
                        break
                    # De no ser así, se volverá a preguntar para que decida.
                    else:
                        continue
                # Se modifica el tablero según la decisión del usuario.
                tablero = turno_usuario(escoger_fila-1, escoger_columna-1,
                                        tablero)
                # Se revisa el tablero para ver la condición de la semillas.
                tablero_semillas = revisar_tablero_semillas(tablero,
                                                            tablero_semillas)
                # Se modifica el tablero según la decisión del computador.
                tablero = turno_computador(tablero)
                # Se modifica el tablero para revisar si alguna semilla
                # tiene que eclosionar.
                tablero = revisar_tablero(tablero, tablero_semillas)
                # El iterador irá incrementando en uno.
                iterador += 1
        # Si la decisión de continuar es sí (s) el juego seguirá.
        # El ciclo comienza nuevamente.
        if ask_decision == "s":
            continue
        # De no ser así, el ciclo se rompe y el juego termina.
        else:
            break


menu()
