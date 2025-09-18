# cifrado_hill.py
# Implementación del cifrado Hill

import numpy as np
from typing import List
from utilidades import Alfabeto, calcular_mcd, limpiar_texto


class CifradoHill:
    """Clase para el cifrado Hill"""

    def __init__(self, tam_grupo: int, matriz_clave: List[List[int]], relleno: str = 'X', alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Hill.

        Args:
            tam_grupo: Tamaño del grupo (matriz cuadrada tam_grupo x tam_grupo)
            matriz_clave: Matriz clave invertible módulo 26
            relleno: Carácter de relleno
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si los parámetros tienen tipos incorrectos
            ValueError: Si los parámetros tienen valores inválidos
        """
        if not isinstance(tam_grupo, int):
            raise TypeError("El tamaño del grupo debe ser un número entero")
        if not isinstance(matriz_clave, list) or not all(isinstance(fila, list) for fila in matriz_clave):
            raise TypeError("La matriz clave debe ser una lista de listas de números enteros")
        if not isinstance(relleno, str):
            raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        if tam_grupo <= 0:
            raise ValueError("El tamaño del grupo debe ser mayor a 0")
        if len(relleno) != 1:
            raise ValueError("El carácter de relleno debe ser un solo carácter")

        self.alfabeto = alfabeto or Alfabeto()
        self.tam_grupo = tam_grupo
        self.relleno = relleno

        # Validar que el relleno esté en el alfabeto
        if not self.alfabeto.contiene_caracter(relleno):
            raise ValueError(f"El carácter de relleno '{relleno}' no está en el alfabeto")

        # Validar matriz
        self._validar_matriz_clave(matriz_clave)
        self.matriz_clave = np.array(matriz_clave)

        # Calcular matriz inversa
        self.matriz_inversa = self._calcular_matriz_inversa()

    def _validar_matriz_clave(self, matriz: List[List[int]]):
        """Valida que la matriz clave sea válida"""
        if len(matriz) != self.tam_grupo or any(len(fila) != self.tam_grupo for fila in matriz):
            raise ValueError("La matriz clave debe ser cuadrada y coincidir con el tamaño de grupo")

        # Validar que todos los elementos sean enteros
        for fila in matriz:
            for elemento in fila:
                if not isinstance(elemento, int):
                    raise TypeError("Todos los elementos de la matriz clave deben ser números enteros")

        matriz_np = np.array(matriz)
        det = int(round(np.linalg.det(matriz_np)))
        if det == 0 or calcular_mcd(abs(det), self.alfabeto.obtener_longitud()) != 1:
            raise ValueError("La matriz clave no es invertible módulo del alfabeto")

    def _calcular_matriz_inversa(self) -> np.ndarray:
        """Calcula la matriz inversa módulo el tamaño del alfabeto"""
        det = int(round(np.linalg.det(self.matriz_clave)))
        det_inv = pow(det, -1, self.alfabeto.obtener_longitud())

        matriz_adj = np.round(det * np.linalg.inv(self.matriz_clave)).astype(int)
        matriz_inv = (det_inv * matriz_adj) % self.alfabeto.obtener_longitud()

        return matriz_inv

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Hill.

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

        # Aplicar relleno si necesario
        if len(texto_limpio) % self.tam_grupo != 0:
            texto_limpio += self.relleno * (self.tam_grupo - (len(texto_limpio) % self.tam_grupo))

        # Convertir a números
        numeros = [self.alfabeto.obtener_indice(c) for c in texto_limpio]

        # Dividir en grupos
        grupos = [numeros[i:i + self.tam_grupo] for i in range(0, len(numeros), self.tam_grupo)]

        # Cifrar cada grupo
        resultado = ""
        for grupo in grupos:
            grupo_vector = np.array(grupo).reshape((self.tam_grupo, 1))
            cifrado_grupo = np.dot(self.matriz_clave, grupo_vector) % self.alfabeto.obtener_longitud()
            for num in cifrado_grupo.flatten():
                resultado += self.alfabeto.obtener_caracter(int(num))

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Hill.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
            ValueError: Si la longitud del texto no es múltiplo del tamaño del grupo
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_cifrado)

        if len(texto_limpio) % self.tam_grupo != 0:
            raise ValueError(f"La longitud del texto debe ser múltiplo de {self.tam_grupo}")

        # Convertir a números
        numeros = [self.alfabeto.obtener_indice(c) for c in texto_limpio]

        # Dividir en grupos
        grupos = [numeros[i:i + self.tam_grupo] for i in range(0, len(numeros), self.tam_grupo)]

        # Descifrar cada grupo
        resultado = ""
        for grupo in grupos:
            grupo_vector = np.array(grupo).reshape((self.tam_grupo, 1))
            descifrado_grupo = np.dot(self.matriz_inversa, grupo_vector) % self.alfabeto.obtener_longitud()
            for num in descifrado_grupo.flatten():
                resultado += self.alfabeto.obtener_caracter(int(num))

        return resultado


# Funciones de conveniencia
def cifrar_hill(texto: str, tam_grupo: int, matriz_clave: List[List[int]], relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Hill.

    Args:
        texto: Texto a cifrar
        tam_grupo: Tamaño del grupo
        matriz_clave: Matriz clave
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
    if not isinstance(tam_grupo, int):
        raise TypeError("El tamaño del grupo debe ser un número entero")
    if not isinstance(matriz_clave, list) or not all(isinstance(fila, list) for fila in matriz_clave):
        raise TypeError("La matriz clave debe ser una lista de listas de números enteros")
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    hill = CifradoHill(tam_grupo, matriz_clave, relleno, alfabeto)
    return hill.cifrar(texto)


def descifrar_hill(texto_cifrado: str, tam_grupo: int, matriz_clave: List[List[int]], relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Hill.

    Args:
        texto_cifrado: Texto a descifrar
        tam_grupo: Tamaño del grupo
        matriz_clave: Matriz clave
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
    if not isinstance(tam_grupo, int):
        raise TypeError("El tamaño del grupo debe ser un número entero")
    if not isinstance(matriz_clave, list) or not all(isinstance(fila, list) for fila in matriz_clave):
        raise TypeError("La matriz clave debe ser una lista de listas de números enteros")
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    hill = CifradoHill(tam_grupo, matriz_clave, relleno, alfabeto)
    return hill.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso con matriz 2x2
    matriz_clave = [[3, 3], [2, 5]]  # Matriz invertible módulo 26
    hill = CifradoHill(2, matriz_clave)
    mensaje = "HOLA MUNDO"
    cifrado = hill.cifrar(mensaje)
    descifrado = hill.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")
    print(f"Matriz clave: {matriz_clave}")