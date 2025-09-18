# main.py
# Programa principal de la librería de cifrados clásicos

import time
from typing import Dict, Any, List, Optional
from utilidades import Alfabeto, analizar_frecuencia

# Importar todos los cifrados
from CifDesplazamiento.cifrado_cesar import CifradoCesar, cifrar_cesar, descifrar_cesar
from CifDesplazamiento.cifrado_vigenere import CifradoVigenere, cifrar_vigenere, descifrar_vigenere
from CifSustitucion.cifrado_atbash import CifradoAtbash, cifrar_atbash, descifrar_atbash
from CifSustMonoPoli.cifrado_playfair import CifradoPlayfair, cifrar_playfair, descifrar_playfair
from CifTransposicion.cifrado_transposicion_columnas import CifradoTransposicionColumnas, cifrar_transposicion_columnas, descifrar_transposicion_columnas
from CifTransposicion.cifrado_rail_fence import CifradoRailFence, cifrar_rail_fence, descifrar_rail_fence
from CifSustMonoPoli.cifrado_hill import CifradoHill, cifrar_hill, descifrar_hill
from CifSustMonoPoli.cifrado_autokey import CifradoAutokey, cifrar_autokey, descifrar_autokey
from CifSustMonoPoli.cifrado_xor import CifradoXOR, cifrar_xor, descifrar_xor


def validar_entrada_numerica(mensaje: str, min_valor: Optional[int] = None,
                           max_valor: Optional[int] = None,
                           valores_permitidos: Optional[List[int]] = None) -> int:
    """
    Valida entrada numérica con restricciones.

    Args:
        mensaje: Mensaje a mostrar al usuario
        min_valor: Valor mínimo permitido (opcional)
        max_valor: Valor máximo permitido (opcional)
        valores_permitidos: Lista de valores específicos permitidos (opcional)

    Returns:
        Número entero validado

    Raises:
        ValueError: Si la entrada no es válida
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                raise ValueError("La entrada no puede estar vacía")

            # Verificar que sea numérico
            if not entrada.isdigit() and not (entrada.startswith('-') and entrada[1:].isdigit()):
                raise ValueError("Debe ingresar un número entero válido")

            valor = int(entrada)

            # Validar rango mínimo
            if min_valor is not None and valor < min_valor:
                raise ValueError(f"El valor debe ser mayor o igual a {min_valor}")

            # Validar rango máximo
            if max_valor is not None and valor > max_valor:
                raise ValueError(f"El valor debe ser menor o igual a {max_valor}")

            # Validar valores específicos
            if valores_permitidos is not None and valor not in valores_permitidos:
                raise ValueError(f"Valor no permitido. Opciones válidas: {valores_permitidos}")

            return valor

        except ValueError as e:
            print(f"[!] Error de entrada: {e}")
            print("Por favor, intente nuevamente.")


def validar_entrada_texto(mensaje: str, permitir_vacio: bool = False,
                         longitud_minima: Optional[int] = None,
                         caracteres_permitidos: Optional[str] = None) -> str:
    """
    Valida entrada de texto con restricciones.

    Args:
        mensaje: Mensaje a mostrar al usuario
        permitir_vacio: Si se permite texto vacío
        longitud_minima: Longitud mínima requerida
        caracteres_permitidos: String con caracteres permitidos

    Returns:
        Texto validado

    Raises:
        ValueError: Si la entrada no es válida
    """
    while True:
        try:
            entrada = input(mensaje).strip()

            if not permitir_vacio and not entrada:
                raise ValueError("La entrada no puede estar vacía")

            if longitud_minima is not None and len(entrada) < longitud_minima:
                raise ValueError(f"La entrada debe tener al menos {longitud_minima} caracteres")

            if caracteres_permitidos:
                for char in entrada:
                    if char not in caracteres_permitidos:
                        raise ValueError(f"Carácter '{char}' no permitido. Solo se permiten: {caracteres_permitidos}")

            return entrada

        except ValueError as e:
            print(f"[!] Error de entrada: {e}")
            print("Por favor, intente nuevamente.")


def validar_matriz_hill(tam_grupo: int) -> List[List[int]]:
    """
    Valida y obtiene una matriz para el cifrado Hill.

    Args:
        tam_grupo: Tamaño de la matriz (2 o 3)

    Returns:
        Matriz validada

    Raises:
        ValueError: Si la matriz no es válida
    """
    print(f"\nIngrese la matriz clave {tam_grupo}x{tam_grupo} (números enteros separados por espacios):")
    print("Nota: La matriz debe ser invertible módulo 26 para poder descifrar.")

    matriz = []
    for i in range(tam_grupo):
        while True:
            try:
                fila_texto = input(f"Fila {i+1}: ").strip()
                if not fila_texto:
                    raise ValueError("La fila no puede estar vacía")

                fila = []
                for num_str in fila_texto.split():
                    if not num_str.isdigit() and not (num_str.startswith('-') and num_str[1:].isdigit()):
                        raise ValueError(f"'{num_str}' no es un número entero válido")
                    fila.append(int(num_str))

                if len(fila) != tam_grupo:
                    raise ValueError(f"La fila debe tener exactamente {tam_grupo} números")

                matriz.append(fila)
                break

            except ValueError as e:
                print(f"[!] Error en fila {i+1}: {e}")
                print("Por favor, intente nuevamente.")

    # Validar que la matriz sea cuadrada
    if len(matriz) != tam_grupo or any(len(fila) != tam_grupo for fila in matriz):
        raise ValueError(f"La matriz debe ser {tam_grupo}x{tam_grupo}")

    return matriz


def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    print("\n" * 50)


def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("=" * 60)
    print("  LIBRERÍA DE CIFRADOS CLÁSICOS  ".center(60))
    print("=" * 60)
    print("\nSeleccione un tipo de cifrado:")
    print("1. Cifrado César")
    print("2. Cifrado Vigenère")
    print("3. Cifrado Atbash")
    print("4. Cifrado Playfair")
    print("5. Cifrado por Transposición de Columnas")
    print("6. Cifrado Rail Fence (Zigzag)")
    print("7. Cifrado Hill")
    print("8. Cifrado Autokey")
    print("9. Cifrado XOR")
    print("10. Análisis de Frecuencias")
    print("11. Salir")
    print("-" * 60)


def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    print("\n" * 50)


def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("=" * 60)
    print("  LIBRERÍA DE CIFRADOS CLÁSICOS  ".center(60))
    print("=" * 60)
    print("\nSeleccione un tipo de cifrado:")
    print("1. Cifrado César")
    print("2. Cifrado Vigenère")
    print("3. Cifrado Atbash")
    print("4. Cifrado Playfair")
    print("5. Cifrado por Transposición de Columnas")
    print("6. Cifrado Rail Fence (Zigzag)")
    print("7. Cifrado Hill")
    print("8. Cifrado Autokey")
    print("9. Cifrado XOR")
    print("10. Análisis de Frecuencias")
    print("11. Salir")
    print("-" * 60)


def menu_cesar():
    """Menú para el cifrado César"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO CÉSAR  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Ataque de fuerza bruta")
        print("4. Volver al menú principal")
        print("\nNota: El desplazamiento debe estar entre 1 y 25.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-4): ",
                                            min_valor=1, max_valor=4)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    desplazamiento = validar_entrada_numerica("Desplazamiento (1-25): ",
                                                             min_valor=1, max_valor=25)

                    resultado = cifrar_cesar(mensaje, desplazamiento)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    desplazamiento = validar_entrada_numerica("Desplazamiento (1-25): ",
                                                             min_valor=1, max_valor=25)

                    resultado = descifrar_cesar(mensaje, desplazamiento)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")

                    cesar = CifradoCesar(3)  # Desplazamiento arbitrario
                    resultados = cesar.ataque_fuerza_bruta(mensaje)
                    print("\n[✓] Resultados del ataque de fuerza bruta:")
                    print("Mostrando los primeros 10 resultados:")
                    for i, resultado in enumerate(resultados[:10]):
                        print(f"Desplazamiento {i+1}: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error en ataque de fuerza bruta: {e}")

            elif opcion == 4:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_vigenere():
    """Menú para el cifrado Vigenère"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO VIGENÈRE  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Ataque por análisis de frecuencia")
        print("4. Volver al menú principal")
        print("\nNota: La clave debe contener solo letras.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-4): ",
                                            min_valor=1, max_valor=4)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    clave = validar_entrada_texto("Clave (solo letras): ",
                                                caracteres_permitidos="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

                    resultado = cifrar_vigenere(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    clave = validar_entrada_texto("Clave (solo letras): ",
                                                caracteres_permitidos="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

                    resultado = descifrar_vigenere(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    longitud_clave = validar_entrada_numerica("Longitud estimada de la clave (1-20): ",
                                                             min_valor=1, max_valor=20)

                    vigenere = CifradoVigenere("DUMMY")  # Clave dummy
                    resultados = vigenere.ataque_analisis_frecuencia(mensaje, longitud_clave)
                    print("\n[✓] Resultados del ataque por análisis de frecuencia:")
                    if resultados:
                        for i, resultado in enumerate(resultados):
                            print(f"Intento {i+1}: {resultado}")
                    else:
                        print("No se encontraron resultados con las claves probadas.")

                except Exception as e:
                    print(f"\n[!] Error en ataque por análisis de frecuencia: {e}")

            elif opcion == 4:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_atbash():
    """Menú para el cifrado Atbash"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO ATBASH  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar/Descifrar mensaje")
        print("2. Volver al menú principal")
        print("\nNota: Atbash es simétrico - la misma operación sirve para cifrar y descifrar.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-2): ",
                                            min_valor=1, max_valor=2)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a procesar: ")

                    resultado = cifrar_atbash(mensaje)
                    print(f"\n[✓] Resultado: {resultado}")
                    print("(Atbash es simétrico - cifrar y descifrar dan el mismo resultado)")

                except Exception as e:
                    print(f"\n[!] Error al procesar: {e}")

            elif opcion == 2:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_playfair():
    """Menú para el cifrado Playfair"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO PLAYFAIR  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Mostrar matriz")
        print("4. Volver al menú principal")
        print("\nNota: La clave debe contener letras (se ignorarán espacios y números).")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-4): ",
                                            min_valor=1, max_valor=4)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    clave = validar_entrada_texto("Clave: ")

                    resultado = cifrar_playfair(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    clave = validar_entrada_texto("Clave: ")

                    resultado = descifrar_playfair(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                try:
                    clave = validar_entrada_texto("Clave para generar matriz: ")

                    playfair = CifradoPlayfair(clave)
                    playfair.mostrar_matriz()

                except Exception as e:
                    print(f"\n[!] Error al mostrar matriz: {e}")

            elif opcion == 4:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_transposicion():
    """Menú para el cifrado por transposición de columnas"""
    while True:
        print("\n" + "=" * 50)
        print("  TRANSPOSICIÓN DE COLUMNAS  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Volver al menú principal")
        print("\nNota: La clave determina el orden de las columnas.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-3): ",
                                            min_valor=1, max_valor=3)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    clave = validar_entrada_texto("Clave: ")

                    resultado = cifrar_transposicion_columnas(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    clave = validar_entrada_texto("Clave: ")

                    resultado = descifrar_transposicion_columnas(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_rail_fence():
    """Menú para el cifrado Rail Fence"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO RAIL FENCE  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Volver al menú principal")
        print("\nNota: El número de rieles debe ser mayor a 1.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-3): ",
                                            min_valor=1, max_valor=3)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    rieles = validar_entrada_numerica("Número de rieles (2-10): ",
                                                     min_valor=2, max_valor=10)

                    resultado = cifrar_rail_fence(mensaje, rieles)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    rieles = validar_entrada_numerica("Número de rieles (2-10): ",
                                                     min_valor=2, max_valor=10)

                    resultado = descifrar_rail_fence(mensaje, rieles)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_hill():
    """Menú para el cifrado Hill"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO HILL  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Volver al menú principal")
        print("\nNota: La matriz debe ser invertible módulo 26.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-3): ",
                                            min_valor=1, max_valor=3)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    tam_grupo = validar_entrada_numerica("Tamaño del grupo (2 o 3): ",
                                                        valores_permitidos=[2, 3])

                    matriz = validar_matriz_hill(tam_grupo)

                    resultado = cifrar_hill(mensaje, tam_grupo, matriz)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    tam_grupo = validar_entrada_numerica("Tamaño del grupo (2 o 3): ",
                                                        valores_permitidos=[2, 3])

                    matriz = validar_matriz_hill(tam_grupo)

                    resultado = descifrar_hill(mensaje, tam_grupo, matriz)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_autokey():
    """Menú para el cifrado Autokey"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO AUTOKEY  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Volver al menú principal")
        print("\nNota: La clave inicial debe contener letras.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-3): ",
                                            min_valor=1, max_valor=3)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a cifrar: ")
                    clave = validar_entrada_texto("Clave inicial (solo letras): ",
                                                caracteres_permitidos="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

                    resultado = cifrar_autokey(mensaje, clave)
                    print(f"\n[✓] Mensaje cifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al cifrar: {e}")

            elif opcion == 2:
                try:
                    mensaje = validar_entrada_texto("Mensaje cifrado: ")
                    clave = validar_entrada_texto("Clave inicial (solo letras): ",
                                                caracteres_permitidos="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

                    resultado = descifrar_autokey(mensaje, clave)
                    print(f"\n[✓] Mensaje descifrado: {resultado}")

                except Exception as e:
                    print(f"\n[!] Error al descifrar: {e}")

            elif opcion == 3:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_xor():
    """Menú para el cifrado XOR"""
    while True:
        print("\n" + "=" * 50)
        print("  CIFRADO XOR  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Cifrar/Descifrar mensaje")
        print("2. Volver al menú principal")
        print("\nNota: XOR es simétrico - la misma operación sirve para cifrar y descifrar.")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-2): ",
                                            min_valor=1, max_valor=2)

            if opcion == 1:
                try:
                    mensaje = validar_entrada_texto("Mensaje a procesar: ")
                    clave = validar_entrada_texto("Clave: ")

                    resultado = cifrar_xor(mensaje, clave)
                    print(f"\n[✓] Resultado: {resultado}")
                    print("(XOR es simétrico - cifrar y descifrar dan el mismo resultado)")

                except Exception as e:
                    print(f"\n[!] Error al procesar: {e}")

            elif opcion == 2:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def menu_frecuencias():
    """Menú para análisis de frecuencias"""
    while True:
        print("\n" + "=" * 50)
        print("  ANÁLISIS DE FRECUENCIAS  ".center(50))
        print("=" * 50)
        print("\nOpciones:")
        print("1. Analizar texto")
        print("2. Volver al menú principal")
        print("\nNota: El análisis cuenta letras alfabéticas (A-Z, a-z).")

        try:
            opcion = validar_entrada_numerica("\nSeleccione una opción (1-2): ",
                                            min_valor=1, max_valor=2)

            if opcion == 1:
                try:
                    texto = validar_entrada_texto("Texto a analizar: ")

                    frecuencias = analizar_frecuencia(texto)
                    print("\n[✓] Análisis de frecuencias:")
                    if frecuencias:
                        print("Carácter | Frecuencia")
                        print("-" * 20)
                        for caracter, frecuencia in sorted(frecuencias.items()):
                            print(f"   {caracter}     |    {frecuencia}")
                    else:
                        print("No se encontraron letras alfabéticas en el texto.")

                except Exception as e:
                    print(f"\n[!] Error en análisis: {e}")

            elif opcion == 2:
                break

        except KeyboardInterrupt:
            print("\n\n[!] Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


def main():
    """Función principal del programa"""
    while True:
        try:
            limpiar_pantalla()
            mostrar_menu_principal()

            opcion = validar_entrada_numerica("Ingrese el número de la opción deseada: ",
                                            min_valor=1, max_valor=11)

            if opcion == 1:
                menu_cesar()
            elif opcion == 2:
                menu_vigenere()
            elif opcion == 3:
                menu_atbash()
            elif opcion == 4:
                menu_playfair()
            elif opcion == 5:
                menu_transposicion()
            elif opcion == 6:
                menu_rail_fence()
            elif opcion == 7:
                menu_hill()
            elif opcion == 8:
                menu_autokey()
            elif opcion == 9:
                menu_xor()
            elif opcion == 10:
                menu_frecuencias()
            elif opcion == 11:
                print("\n¡Gracias por usar la Librería de Cifrados Clásicos!")
                time.sleep(1)
                break

        except KeyboardInterrupt:
            print("\n\n[!] Programa interrumpido por el usuario.")
            print("¡Gracias por usar la Librería de Cifrados Clásicos!")
            break
        except Exception as e:
            print(f"\n[!] Error inesperado en el programa principal: {e}")
            print("Intentando continuar...")
            time.sleep(2)


if __name__ == "__main__":
    main()