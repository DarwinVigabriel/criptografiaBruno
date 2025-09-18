# cifrado_atbash.py
# Implementación del cifrado Atbash

from utilidades import Alfabeto


class CifradoAtbash:
    """Clase para el cifrado Atbash (simétrico)"""

    def __init__(self, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Atbash.

        Args:
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si alfabeto no es una instancia de Alfabeto
        """
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        self.alfabeto = alfabeto or Alfabeto()

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Atbash.
        Atbash es simétrico, por lo que cifrar y descifrar son lo mismo.

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
                # Invertir la posición en el alfabeto
                nuevo_indice = self.alfabeto.obtener_longitud() - 1 - indice
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c  # Mantener caracteres no alfabéticos
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Atbash.
        Como Atbash es simétrico, es igual al cifrado.

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
def cifrar_atbash(texto: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Atbash.

    Args:
        texto: Texto a cifrar
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto cifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    atbash = CifradoAtbash(alfabeto)
    return atbash.cifrar(texto)


def descifrar_atbash(texto_cifrado: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Atbash.

    Args:
        texto_cifrado: Texto a descifrar
        alfabeto: Alfabeto a utilizar

    Returns:
        Texto descifrado

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
    """
    if not isinstance(texto_cifrado, str):
        raise TypeError("El texto cifrado debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    atbash = CifradoAtbash(alfabeto)
    return atbash.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    atbash = CifradoAtbash()
    mensaje = "HOLA MUNDO"
    cifrado = atbash.cifrar(mensaje)
    descifrado = atbash.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")

    # Atbash es simétrico
    print(f"\nAtbash es simétrico: {atbash.cifrar(cifrado) == mensaje}")