# cifrado_autokey.py
# Implementación del cifrado Autokey (variante de Vigenère)

from utilidades import Alfabeto, limpiar_texto


class CifradoAutokey:
    """Clase para el cifrado Autokey"""

    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Autokey.

        Args:
            clave: Palabra clave inicial
            alfabeto: Alfabeto a utilizar

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

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Autokey.
        La clave se extiende usando el texto plano mismo.

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
        resultado = ""

        # Construir clave extendida
        clave_extendida = self.clave
        indice_clave = 0

        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_texto + indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)

                # Agregar el carácter original a la clave extendida
                clave_extendida += c
                indice_clave += 1
            else:
                resultado += c  # Mantener caracteres no alfabéticos

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Autokey.

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
        resultado = ""

        # Reconstruir clave extendida
        clave_extendida = self.clave
        indice_clave = 0

        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_cifrado = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_cifrado - indice_clave_actual) % self.alfabeto.obtener_longitud()
                caracter_original = self.alfabeto.obtener_caracter(nuevo_indice)
                resultado += caracter_original

                # Agregar el carácter descifrado a la clave extendida
                clave_extendida += caracter_original
                indice_clave += 1
            else:
                resultado += c  # Mantener caracteres no alfabéticos

        return resultado


# Funciones de conveniencia
def cifrar_autokey(texto: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Autokey.

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

    autokey = CifradoAutokey(clave, alfabeto)
    return autokey.cifrar(texto)


def descifrar_autokey(texto_cifrado: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Autokey.

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

    autokey = CifradoAutokey(clave, alfabeto)
    return autokey.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    autokey = CifradoAutokey("CLAVE")
    mensaje = "ATAQUE AL AMANECER"
    cifrado = autokey.cifrar(mensaje)
    descifrado = autokey.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")
    print(f"Clave inicial: {autokey.clave}")