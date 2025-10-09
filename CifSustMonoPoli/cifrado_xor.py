# cifrado_xor.py
# Implementación del cifrado XOR simple

import base64
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
            # XOR con el código ASCII del carácter
            clave_char = self.clave[indice_clave % len(self.clave)]
            nuevo_codigo = ord(c) ^ ord(clave_char)
            resultado += chr(nuevo_codigo)
            indice_clave += 1

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
        Texto cifrado codificado en base64 para legibilidad

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
    resultado_binario = xor.cifrar(texto)
    # Codificar en base64 para legibilidad
    return base64.b64encode(resultado_binario.encode('latin-1')).decode('ascii')


def descifrar_xor(texto_cifrado: str, clave: str, alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con XOR.

    Args:
        texto_cifrado: Texto a descifrar (puede estar en base64 o como string binario)
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

    # Intentar decodificar de base64 primero
    try:
        datos_binarios = base64.b64decode(texto_cifrado)
        texto_para_descifrar = datos_binarios.decode('latin-1')
    except:
        # Si no es base64 válido, asumir que es string binario directo
        texto_para_descifrar = texto_cifrado

    xor = CifradoXOR(clave, alfabeto)
    return xor.descifrar(texto_para_descifrar)


if __name__ == "__main__":
    # Ejemplo de uso
    mensaje = "HOLA MUNDO"
    clave = "CLAVE"
    cifrado = cifrar_xor(mensaje, clave)
    descifrado = descifrar_xor(cifrado, clave)

    print(f"Original: {mensaje}")
    print(f"Cifrado (base64): {cifrado}")
    print(f"Descifrado: {descifrado}")

    # XOR es simétrico
    print(f"\nXOR es simétrico: {descifrar_xor(cifrar_xor(mensaje, clave), clave) == mensaje}")