# cifrado_xor.py
# Implementación del cifrado XOR simple

from utilidades import Alfabeto


class CifradoXOR:
    """Clase para el cifrado XOR simple"""

    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado XOR.

        Args:
            clave: Clave binaria para XOR
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si clave no es una cadena o alfabeto no es instancia de Alfabeto
            ValueError: Si la clave está vacía
        """
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        clave_limpia = clave.strip()
        if not clave_limpia:
            raise ValueError("La clave no puede estar vacía")

        self.alfabeto = alfabeto or Alfabeto()
        self.clave = clave_limpia

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando XOR.
        XOR es simétrico, por lo que cifrar y descifrar son lo mismo.

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
        indice_clave = 0

        for c in texto_plano:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = ord(self.clave[indice_clave % len(self.clave)])
                nuevo_indice = indice_texto ^ indice_clave_actual
                # Asegurar que esté dentro del rango del alfabeto
                nuevo_indice %= self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c  # Mantener caracteres no alfabéticos

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con XOR.
        Como XOR es simétrico, es igual al cifrado.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        return self.cifrar(texto_cifrado)


# Funciones de conveniencia
def cifrar_xor(texto: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con XOR.

    Args:
        texto: Texto a cifrar
        clave: Clave para XOR
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

    xor = CifradoXOR(clave, alfabeto)
    return xor.cifrar(texto)


def descifrar_xor(texto_cifrado: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con XOR.

    Args:
        texto_cifrado: Texto a descifrar
        clave: Clave para XOR
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

    xor = CifradoXOR(clave, alfabeto)
    return xor.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    xor = CifradoXOR("CLAVE")
    mensaje = "HOLA MUNDO"
    cifrado = xor.cifrar(mensaje)
    descifrado = xor.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")
    print(f"Clave: {xor.clave}")

    # XOR es simétrico
    print(f"\nXOR es simétrico: {xor.cifrar(cifrado) == mensaje}")