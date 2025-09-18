# cifrado_transposicion_columnas.py
# Implementación del cifrado por transposición de columnas

from typing import List
from utilidades import Alfabeto, ordenar_columnas, limpiar_texto


class CifradoTransposicionColumnas:
    """Clase para el cifrado por transposición de columnas"""

    def __init__(self, clave: str, relleno: str = 'X', alfabeto: Alfabeto = None):
        """
        Constructor del cifrado por transposición de columnas.

        Args:
            clave: Palabra clave que determina el orden de las columnas
            relleno: Carácter de relleno para completar la matriz
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si los parámetros tienen tipos incorrectos
            ValueError: Si los parámetros tienen valores inválidos
        """
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres")
        if not isinstance(relleno, str):
            raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        clave_limpia = clave.strip()
        if not clave_limpia:
            raise ValueError("La clave no puede estar vacía")
        if len(relleno) != 1:
            raise ValueError("El carácter de relleno debe ser un solo carácter")

        self.alfabeto = alfabeto or Alfabeto()

        self.clave = limpiar_texto(clave_limpia)
        if not self.clave:
            raise ValueError("La clave debe contener al menos un carácter alfabético")

        # Validar que el relleno esté en el alfabeto
        if not self.alfabeto.contiene_caracter(relleno):
            raise ValueError(f"El carácter de relleno '{relleno}' no está en el alfabeto")

        self.relleno = relleno
        self.orden_columnas = ordenar_columnas(self.clave)

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando transposición de columnas.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado

        Raises:
            TypeError: Si texto_plano no es una cadena
        """
        if not isinstance(texto_plano, str):
            raise TypeError("El texto a cifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_plano)
        num_columnas = len(self.clave)

        # Calcular relleno necesario
        faltante = (num_columnas - (len(texto_limpio) % num_columnas)) % num_columnas
        texto_relleno = texto_limpio + self.relleno * faltante

        # Crear matriz
        num_filas = len(texto_relleno) // num_columnas
        matriz = []
        for i in range(0, len(texto_relleno), num_columnas):
            fila = texto_relleno[i:i + num_columnas]
            matriz.append(fila)

        # Reordenar columnas según la clave
        matriz_ordenada = []
        for fila in matriz:
            fila_ordenada = [fila[i] for i in self.orden_columnas]
            matriz_ordenada.append(fila_ordenada)

        # Leer por columnas para obtener el texto cifrado
        resultado = ""
        for col in range(num_columnas):
            for fila in matriz_ordenada:
                resultado += fila[col]

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con transposición de columnas.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
            ValueError: Si la longitud del texto no es múltiplo del número de columnas
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_cifrado)
        num_columnas = len(self.clave)
        len_cifrado = len(texto_limpio)

        if len_cifrado % num_columnas != 0:
            raise ValueError(f"La longitud del texto cifrado debe ser múltiplo de {num_columnas}")

        num_filas = len_cifrado // num_columnas

        # Reconstruir la matriz cifrada
        matriz_cifrada = []
        for i in range(0, len_cifrado, num_filas):
            columna = texto_limpio[i:i + num_filas]
            matriz_cifrada.append(columna)

        # Reordenar columnas a posición original
        matriz_original = [None] * num_columnas
        for pos_original, pos_cifrada in enumerate(self.orden_columnas):
            matriz_original[pos_cifrada] = matriz_cifrada[pos_original]

        # Reconstruir mensaje original
        resultado = ""
        for fila in range(num_filas):
            for col in range(num_columnas):
                resultado += matriz_original[col][fila]

        # Eliminar relleno
        if self.relleno:
            resultado = resultado.rstrip(self.relleno)

        return resultado


# Funciones de conveniencia
def cifrar_transposicion_columnas(texto: str, clave: str, relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con transposición de columnas.

    Args:
        texto: Texto a cifrar
        clave: Palabra clave
        relleno: Carácter de relleno
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
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    transposicion = CifradoTransposicionColumnas(clave, relleno, alfabeto)
    return transposicion.cifrar(texto)


def descifrar_transposicion_columnas(texto_cifrado: str, clave: str, relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con transposición de columnas.

    Args:
        texto_cifrado: Texto a descifrar
        clave: Palabra clave
        relleno: Carácter de relleno
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
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    transposicion = CifradoTransposicionColumnas(clave, relleno, alfabeto)
    return transposicion.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    transposicion = CifradoTransposicionColumnas("CLAVE")
    mensaje = "ATAQUE AL AMANECER"
    cifrado = transposicion.cifrar(mensaje)
    descifrado = transposicion.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")
    print(f"Orden de columnas: {transposicion.orden_columnas}")