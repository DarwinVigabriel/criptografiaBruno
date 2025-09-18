"""
Cifrado de Sustitución Simple (Monoalfabética)
===========================================

Este módulo implementa un cifrado de sustitución simple donde cada letra
del alfabeto se reemplaza por otra letra fija según una clave o permutación.
"""

import string
from typing import Dict, Optional
from utilidades import Alfabeto, limpiar_texto


class CifradoSustitucionSimple:
    """
    Cifrado de sustitución monoalfabética con alfabeto permutado.
    """

    def __init__(self, clave: Optional[str] = None, alfabeto: Optional[Alfabeto] = None):
        """
        Constructor del cifrado de sustitución simple.

        Args:
            clave: Clave para generar la permutación del alfabeto.
                  Si no se proporciona, se usa una permutación aleatoria.
            alfabeto: Alfabeto personalizado. Si no se proporciona, usa ASCII mayúsculas.

        Raises:
            TypeError: Si clave o alfabeto tienen tipos incorrectos
            ValueError: Si la clave contiene caracteres inválidos
        """
        if clave is not None and not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres o None")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto o None")

        self.alfabeto = alfabeto or Alfabeto()

        if clave is not None:
            clave_upper = clave.upper()
            # Validar que la clave contenga solo caracteres del alfabeto
            for c in clave_upper:
                if not self.alfabeto.contiene_caracter(c):
                    raise ValueError(f"La clave contiene el carácter '{c}' que no está en el alfabeto")
            self.clave = clave_upper
        else:
            self.clave = None

        # Crear el mapeo de sustitución
        self.mapeo_cifrado = self._crear_mapeo_cifrado()
        self.mapeo_descifrado = {v: k for k, v in self.mapeo_cifrado.items()}

    def _crear_mapeo_cifrado(self) -> Dict[str, str]:
        """
        Crea el mapeo de sustitución basado en la clave.

        Returns:
            Diccionario con el mapeo de cada carácter a su sustituto.
        """
        alfabeto_base = self.alfabeto.alfabeto
        mapeo = {}

        if self.clave:
            # Usar la clave para crear la permutación
            clave_limpia = "".join(dict.fromkeys(self.clave))  # Remover duplicados manteniendo orden

            # Crear alfabeto permutado: clave + letras restantes
            letras_restantes = "".join(c for c in alfabeto_base if c not in clave_limpia)
            alfabeto_permutado = clave_limpia + letras_restantes
        else:
            # Permutación simple: rotar el alfabeto
            alfabeto_permutado = alfabeto_base[1:] + alfabeto_base[0]

        # Crear mapeo
        for i, caracter in enumerate(alfabeto_base):
            if i < len(alfabeto_permutado):
                mapeo[caracter] = alfabeto_permutado[i]
            else:
                mapeo[caracter] = caracter  # Mantener igual si no hay suficiente permutación

        return mapeo

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto plano usando sustitución simple.

        Args:
            texto_plano: Texto a cifrar.

        Returns:
            Texto cifrado.

        Raises:
            TypeError: Si texto_plano no es una cadena
        """
        if not isinstance(texto_plano, str):
            raise TypeError("El texto a cifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_plano)
        resultado = []

        for caracter in texto_limpio:
            if caracter in self.mapeo_cifrado:
                resultado.append(self.mapeo_cifrado[caracter])
            else:
                resultado.append(caracter)  # Mantener caracteres no alfabéticos

        return "".join(resultado)

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado usando sustitución simple.

        Args:
            texto_cifrado: Texto a descifrar.

        Returns:
            Texto plano original.

        Raises:
            TypeError: Si texto_cifrado no es una cadena
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_cifrado)
        resultado = []

        for caracter in texto_limpio:
            if caracter in self.mapeo_descifrado:
                resultado.append(self.mapeo_descifrado[caracter])
            else:
                resultado.append(caracter)  # Mantener caracteres no alfabéticos

        return "".join(resultado)

    def obtener_alfabeto_permutado(self) -> str:
        """
        Obtiene el alfabeto permutado usado para el cifrado.

        Returns:
            Cadena con el alfabeto permutado.
        """
        return "".join(self.mapeo_cifrado.get(c, c) for c in self.alfabeto.alfabeto)


# Funciones de conveniencia
def cifrar_sustitucion_simple(texto: str, clave: Optional[str] = None) -> str:
    """
    Función de conveniencia para cifrar con sustitución simple.

    Args:
        texto: Texto a cifrar.
        clave: Clave para la sustitución.

    Returns:
        Texto cifrado.

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if clave is not None and not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres o None")

    cifrador = CifradoSustitucionSimple(clave)
    return cifrador.cifrar(texto)


def descifrar_sustitucion_simple(texto: str, clave: Optional[str] = None) -> str:
    """
    Función de conveniencia para descifrar con sustitución simple.

    Args:
        texto: Texto a descifrar.
        clave: Clave usada para el cifrado.

    Returns:
        Texto plano.

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if clave is not None and not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres o None")

    cifrador = CifradoSustitucionSimple(clave)
    return cifrador.descifrar(texto)


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Ejemplo con clave
    print("=== Cifrado de Sustitución Simple ===")

    clave = "CLAVE"
    mensaje = "ATAQUE AL AMANECER"

    print(f"Mensaje original: {mensaje}")
    print(f"Clave: {clave}")

    cifrador = CifradoSustitucionSimple(clave)
    print(f"Alfabeto permutado: {cifrador.obtener_alfabeto_permutado()}")

    cifrado = cifrador.cifrar(mensaje)
    print(f"Mensaje cifrado: {cifrado}")

    descifrado = cifrador.descifrar(cifrado)
    print(f"Mensaje descifrado: {descifrado}")

    print(f"¿Descifrado correcto?: {descifrado == limpiar_texto(mensaje)}")

    # Ejemplo sin clave (rotación simple)
    print("\n=== Sin clave (rotación simple) ===")
    cifrador_simple = CifradoSustitucionSimple()
    cifrado_simple = cifrador_simple.cifrar(mensaje)
    descifrado_simple = cifrador_simple.descifrar(cifrado_simple)

    print(f"Mensaje cifrado: {cifrado_simple}")
    print(f"Mensaje descifrado: {descifrado_simple}")
    print(f"¿Descifrado correcto?: {descifrado_simple == limpiar_texto(mensaje)}")