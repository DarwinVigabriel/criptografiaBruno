# cifrado_vigenere.py
# Implementación del cifrado Vigenère

from typing import List
from utilidades import Alfabeto, limpiar_texto


class CifradoVigenere:
    """Clase para el cifrado Vigenère"""

    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Vigenère.

        Args:
            clave: Palabra clave para el cifrado
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si clave no es una cadena
            ValueError: Si la clave está vacía o no contiene caracteres válidos
        """
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres")

        clave_limpia = clave.strip()
        if not clave_limpia:
            raise ValueError("La clave no puede estar vacía")

        self.alfabeto = alfabeto or Alfabeto()

        self.clave = limpiar_texto(clave_limpia)
        if not self.clave:
            raise ValueError("La clave debe contener al menos un carácter alfabético")

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Vigenère.

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
        if not texto_limpio:
            return texto_plano  # Si no hay texto alfabético, devolver original

        resultado = ""

        # Extender la clave para que coincida con la longitud del texto
        clave_extendida = ""
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1

        # Cifrar letra por letra
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_texto + indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c  # Mantener caracteres no alfabéticos

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Vigenère.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_cifrado)
        if not texto_limpio:
            return texto_cifrado  # Si no hay texto alfabético, devolver original

        resultado = ""

        # Extender la clave
        clave_extendida = ""
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1

        # Descifrar letra por letra
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_cifrado = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_cifrado - indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c  # Mantener caracteres no alfabéticos

        return resultado

    def ataque_analisis_frecuencia(self, texto_cifrado: str, longitud_clave: int) -> List[str]:
        """
        Ataque simplificado por análisis de frecuencia.
        En la práctica, se requeriría un análisis más sofisticado.

        Args:
            texto_cifrado: Texto cifrado a atacar
            longitud_clave: Longitud estimada de la clave

        Returns:
            Lista de posibles textos descifrados

        Raises:
            TypeError: Si los parámetros tienen tipos incorrectos
            ValueError: Si longitud_clave es inválida
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto cifrado debe ser una cadena de caracteres")
        if not isinstance(longitud_clave, int):
            raise TypeError("La longitud de clave debe ser un número entero")
        if longitud_clave <= 0:
            raise ValueError("La longitud de clave debe ser mayor a 0")

        # Implementación simplificada - en la realidad sería más compleja
        resultados = []

        # Para simplificar, probamos claves comunes de la longitud dada
        claves_comunes = ["CLAVE", "KEY", "PASSWORD", "SECRET"]

        for clave_base in claves_comunes:
            if len(clave_base) == longitud_clave:
                vigenere_temp = CifradoVigenere(clave_base, self.alfabeto)
                resultados.append(vigenere_temp.descifrar(texto_cifrado))

        return resultados


# Funciones de conveniencia
def cifrar_vigenere(texto: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Vigenère.

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

    vigenere = CifradoVigenere(clave, alfabeto)
    return vigenere.cifrar(texto)


def descifrar_vigenere(texto_cifrado: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Vigenère.

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

    vigenere = CifradoVigenere(clave, alfabeto)
    return vigenere.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    vigenere = CifradoVigenere("CLAVE")
    mensaje = "ATAQUE AL AMANECER"
    cifrado = vigenere.cifrar(mensaje)
    descifrado = vigenere.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")

    # Ataque de análisis de frecuencia (simplificado)
    print("\nAtaque por análisis de frecuencia:")
    posibles = vigenere.ataque_analisis_frecuencia(cifrado, 5)
    for i, posible in enumerate(posibles):
        print(f"Posible {i+1}: {posible}")