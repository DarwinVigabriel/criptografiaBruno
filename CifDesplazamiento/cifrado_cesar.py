# cifrado_cesar.py
# Implementación del cifrado César

from typing import List
from utilidades import Alfabeto, limpiar_texto


class CifradoCesar:
    """Clase para el cifrado César"""

    def __init__(self, desplazamiento: int = 3, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado César.

        Args:
            desplazamiento: Número de posiciones a desplazar
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si desplazamiento no es un entero
            ValueError: Si el alfabeto es inválido
        """
        if not isinstance(desplazamiento, int):
            raise TypeError("El desplazamiento debe ser un número entero")

        self.alfabeto = alfabeto or Alfabeto()

        if self.alfabeto.obtener_longitud() == 0:
            raise ValueError("El alfabeto no puede estar vacío")

        self.desplazamiento = desplazamiento % self.alfabeto.obtener_longitud()
        if self.desplazamiento < 0:
            self.desplazamiento += self.alfabeto.obtener_longitud()

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando el cifrado César.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado

        Raises:
            TypeError: Si texto_plano no es una cadena
        """
        if not isinstance(texto_plano, str):
            raise TypeError("El texto a cifrar debe ser una cadena de caracteres")

        resultado = ""
        for c in texto_plano:
            indice = self.alfabeto.obtener_indice(c)
            if indice != -1:
                nuevo_indice = (indice + self.desplazamiento) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c  # Mantener caracteres no alfabéticos
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con César.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        resultado = ""
        desplazamiento_inverso = self.alfabeto.obtener_longitud() - self.desplazamiento
        for c in texto_cifrado:
            indice = self.alfabeto.obtener_indice(c)
            if indice != -1:
                nuevo_indice = (indice + desplazamiento_inverso) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c  # Mantener caracteres no alfabéticos
        return resultado

    def ataque_fuerza_bruta(self, texto_cifrado: str) -> List[str]:
        """
        Realiza un ataque de fuerza bruta probando todos los desplazamientos posibles.

        Args:
            texto_cifrado: Texto cifrado a atacar

        Returns:
            Lista de posibles textos descifrados

        Raises:
            TypeError: Si texto_cifrado no es una cadena
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto cifrado debe ser una cadena de caracteres")

        resultados = []
        for i in range(1, self.alfabeto.obtener_longitud()):
            cesar_temp = CifradoCesar(i, self.alfabeto)
            resultados.append(cesar_temp.descifrar(texto_cifrado))
        return resultados


# Función de conveniencia para uso directo
def cifrar_cesar(texto: str, desplazamiento: int = 3, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con César.

    Args:
        texto: Texto a cifrar
        desplazamiento: Número de posiciones a desplazar
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto cifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if not isinstance(desplazamiento, int):
        raise TypeError("El desplazamiento debe ser un número entero")

    cesar = CifradoCesar(desplazamiento, alfabeto)
    return cesar.cifrar(texto)


def descifrar_cesar(texto_cifrado: str, desplazamiento: int = 3, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con César.

    Args:
        texto_cifrado: Texto a descifrar
        desplazamiento: Número de posiciones que se desplazó
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto descifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
    """
    if not isinstance(texto_cifrado, str):
        raise TypeError("El texto cifrado debe ser una cadena de caracteres")
    if not isinstance(desplazamiento, int):
        raise TypeError("El desplazamiento debe ser un número entero")

    cesar = CifradoCesar(desplazamiento, alfabeto)
    return cesar.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    cesar = CifradoCesar(3)
    mensaje = "HOLA MUNDO"
    cifrado = cesar.cifrar(mensaje)
    descifrado = cesar.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")

    # Ataque de fuerza bruta
    print("\nAtaque de fuerza bruta:")
    posibles = cesar.ataque_fuerza_bruta(cifrado)
    for i, posible in enumerate(posibles[:5]):  # Mostrar solo los primeros 5
        print(f"Desplazamiento {i+1}: {posible}")