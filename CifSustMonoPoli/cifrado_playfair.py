# cifrado_playfair.py
# Implementación del cifrado Playfair

from typing import List, Tuple
from utilidades import Alfabeto, limpiar_texto


class CifradoPlayfair:
    """Clase para el cifrado Playfair"""

    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Playfair.

        Args:
            clave: Palabra clave para generar la matriz
            alfabeto: Alfabeto a utilizar (debe tener al menos 25 caracteres para matriz 5x5)

        Raises:
            TypeError: Si clave no es una cadena o alfabeto no es instancia de Alfabeto
            ValueError: Si la clave está vacía o no contiene caracteres válidos
        """
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        clave_limpia = clave.strip()
        if not clave_limpia:
            raise ValueError("La clave no puede estar vacía")

        self.alfabeto = alfabeto or Alfabeto()

        self.clave = limpiar_texto(clave_limpia)
        if not self.clave:
            raise ValueError("La clave debe contener al menos un carácter alfabético")

        if self.alfabeto.obtener_longitud() < 25:
            raise ValueError("El alfabeto debe tener al menos 25 caracteres para Playfair")

        self.matriz = self._construir_matriz()

    def _construir_matriz(self) -> List[List[str]]:
        """Construye la matriz 5x5 para Playfair"""
        matriz = [['' for _ in range(5)] for _ in range(5)]
        usados = set()

        # Agregar clave sin duplicados
        clave_limpia = ""
        for c in self.clave:
            if self.alfabeto.contiene_caracter(c) and c not in usados:
                usados.add(c)
                clave_limpia += c

        # Agregar resto del alfabeto (excluyendo J si es necesario)
        for i in range(self.alfabeto.obtener_longitud()):
            c = self.alfabeto.obtener_caracter(i)
            if c not in usados:
                clave_limpia += c
                usados.add(c)

        # Llenar matriz 5x5
        indice = 0
        for fila in range(5):
            for col in range(5):
                if indice < len(clave_limpia):
                    matriz[fila][col] = clave_limpia[indice]
                    indice += 1

        return matriz

    def _encontrar_posicion(self, caracter: str) -> Tuple[int, int]:
        """Encuentra la posición de un carácter en la matriz"""
        for fila in range(5):
            for col in range(5):
                if self.matriz[fila][col] == caracter:
                    return (fila, col)
        raise ValueError(f"Carácter '{caracter}' no encontrado en la matriz")

    def _preparar_texto(self, texto: str) -> str:
        """Prepara el texto para el cifrado Playfair"""
        texto_limpio = limpiar_texto(texto)
        preparado = ""

        i = 0
        while i < len(texto_limpio):
            c1 = texto_limpio[i]
            i += 1
            c2 = texto_limpio[i] if i < len(texto_limpio) else 'X'

            preparado += c1
            if c1 == c2:
                preparado += 'X'
                i -= 1  # Retroceder para procesar c2 de nuevo
            else:
                preparado += c2
                i += 1

        # Asegurar longitud par
        if len(preparado) % 2 != 0:
            preparado += 'X'

        return preparado

    def _cifrar_digrafo(self, digrafo: str) -> str:
        """Cifra un dígrafo usando las reglas de Playfair"""
        f1, c1 = self._encontrar_posicion(digrafo[0])
        f2, c2 = self._encontrar_posicion(digrafo[1])

        if f1 == f2:
            # Misma fila
            return self.matriz[f1][(c1 + 1) % 5] + self.matriz[f2][(c2 + 1) % 5]
        elif c1 == c2:
            # Misma columna
            return self.matriz[(f1 + 1) % 5][c1] + self.matriz[(f2 + 1) % 5][c2]
        else:
            # Rectángulo
            return self.matriz[f1][c2] + self.matriz[f2][c1]

    def _descifrar_digrafo(self, digrafo: str) -> str:
        """Descifra un dígrafo usando las reglas de Playfair"""
        f1, c1 = self._encontrar_posicion(digrafo[0])
        f2, c2 = self._encontrar_posicion(digrafo[1])

        if f1 == f2:
            # Misma fila
            return self.matriz[f1][(c1 - 1) % 5] + self.matriz[f2][(c2 - 1) % 5]
        elif c1 == c2:
            # Misma columna
            return self.matriz[(f1 - 1) % 5][c1] + self.matriz[(f2 - 1) % 5][c2]
        else:
            # Rectángulo
            return self.matriz[f1][c2] + self.matriz[f2][c1]

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Playfair.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado

        Raises:
            TypeError: Si texto_plano no es una cadena
        """
        if not isinstance(texto_plano, str):
            raise TypeError("El texto a cifrar debe ser una cadena de caracteres")

        preparado = self._preparar_texto(texto_plano)
        resultado = ""

        for i in range(0, len(preparado), 2):
            digrafo = preparado[i:i+2]
            resultado += self._cifrar_digrafo(digrafo)

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Playfair.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
            ValueError: Si texto_cifrado tiene longitud impar
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")
        if len(texto_cifrado) % 2 != 0:
            raise ValueError("El texto cifrado debe tener longitud par para Playfair")

        resultado = ""

        for i in range(0, len(texto_cifrado), 2):
            digrafo = texto_cifrado[i:i+2]
            resultado += self._descifrar_digrafo(digrafo)

        # Eliminar X de relleno al final
        if resultado and resultado[-1] == 'X':
            resultado = resultado[:-1]

        return resultado

    def mostrar_matriz(self):
        """Muestra la matriz Playfair"""
        print("Matriz Playfair:")
        for fila in self.matriz:
            print(" ".join(fila))


# Funciones de conveniencia
def cifrar_playfair(texto: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Playfair.

    Args:
        texto: Texto a cifrar
        clave: Palabra clave
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto cifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    playfair = CifradoPlayfair(clave, alfabeto)
    return playfair.cifrar(texto)


def descifrar_playfair(texto_cifrado: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Playfair.

    Args:
        texto_cifrado: Texto a descifrar
        clave: Palabra clave
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto descifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto_cifrado, str):
        raise TypeError("El texto cifrado debe ser una cadena de caracteres")
    if not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    playfair = CifradoPlayfair(clave, alfabeto)
    return playfair.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    playfair = CifradoPlayfair("CLAVE")
    mensaje = "HOLA MUNDO"
    cifrado = playfair.cifrar(mensaje)
    descifrado = playfair.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")

    print("\nMatriz:")
    playfair.mostrar_matriz()