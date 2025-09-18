# cifrado_rail_fence.py
# Implementación del cifrado Rail Fence (Zigzag)

from utilidades import Alfabeto, limpiar_texto


class CifradoRailFence:
    """Clase para el cifrado Rail Fence (Zigzag)"""

    def __init__(self, rieles: int, relleno: str = 'X', alfabeto: Alfabeto = None):
        """
        Constructor del cifrado Rail Fence.

        Args:
            rieles: Número de rieles (líneas) del zigzag
            relleno: Carácter de relleno
            alfabeto: Alfabeto a utilizar

        Raises:
            TypeError: Si los parámetros tienen tipos incorrectos
            ValueError: Si los parámetros tienen valores inválidos
        """
        if not isinstance(rieles, int):
            raise TypeError("El número de rieles debe ser un número entero")
        if not isinstance(relleno, str):
            raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
        if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
            raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

        if rieles <= 1:
            raise ValueError("El número de rieles debe ser mayor a 1")
        if len(relleno) != 1:
            raise ValueError("El carácter de relleno debe ser un solo carácter")

        self.alfabeto = alfabeto or Alfabeto()

        # Validar que el relleno esté en el alfabeto
        if not self.alfabeto.contiene_caracter(relleno):
            raise ValueError(f"El carácter de relleno '{relleno}' no está en el alfabeto")

        self.rieles = rieles
        self.relleno = relleno

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Rail Fence.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado

        Raises:
            TypeError: Si texto_plano no es una cadena
            ValueError: Si el texto está vacío después de limpiar
        """
        if not isinstance(texto_plano, str):
            raise TypeError("El texto a cifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_plano)
        if not texto_limpio:
            raise ValueError("El texto no puede estar vacío después de limpiar")

        # Aplicar relleno si es necesario
        ciclo = 2 * (self.rieles - 1)
        faltante = (ciclo - (len(texto_limpio) % ciclo)) % ciclo
        texto_relleno = texto_limpio + self.relleno * faltante

        # Crear rieles
        rieles = [[] for _ in range(self.rieles)]
        fila = 0
        direccion = 1  # 1: abajo, -1: arriba

        for letra in texto_relleno:
            rieles[fila].append(letra)
            fila += direccion
            if fila == 0 or fila == self.rieles - 1:
                direccion *= -1

        # Concatenar todos los rieles
        resultado = ""
        for riel in rieles:
            resultado += "".join(riel)

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Rail Fence.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado

        Raises:
            TypeError: Si texto_cifrado no es una cadena
            ValueError: Si el texto cifrado está vacío
        """
        if not isinstance(texto_cifrado, str):
            raise TypeError("El texto a descifrar debe ser una cadena de caracteres")

        texto_limpio = limpiar_texto(texto_cifrado)
        if not texto_limpio:
            raise ValueError("El texto cifrado no puede estar vacío")

        # Calcular longitudes de cada riel
        ciclo = 2 * (self.rieles - 1)
        len_total = len(texto_limpio)
        q, r = divmod(len_total, ciclo)

        longitudes = [0] * self.rieles
        for i in range(self.rieles):
            if i == 0 or i == self.rieles - 1:
                longitudes[i] = q
            else:
                longitudes[i] = 2 * q

        for i in range(r):
            if i < self.rieles:
                longitudes[i] += 1
            else:
                longitudes[2 * (self.rieles - 1) - i] += 1

        # Extraer los rieles
        rieles_separados = []
        inicio = 0
        for l in longitudes:
            rieles_separados.append(texto_limpio[inicio:inicio + l])
            inicio += l

        # Reconstruir el mensaje original
        resultado = []
        indices = [0] * self.rieles
        fila = 0
        direccion = 1

        for _ in range(len(texto_limpio)):
            resultado.append(rieles_separados[fila][indices[fila]])
            indices[fila] += 1
            fila += direccion
            if fila == 0 or fila == self.rieles - 1:
                direccion *= -1

        return "".join(resultado)


# Funciones de conveniencia
def cifrar_rail_fence(texto: str, rieles: int, relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para cifrar con Rail Fence.

    Args:
        texto: Texto a cifrar
        rieles: Número de rieles
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
    if not isinstance(rieles, int):
        raise TypeError("El número de rieles debe ser un número entero")
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    rail_fence = CifradoRailFence(rieles, relleno, alfabeto)
    return rail_fence.cifrar(texto)


def descifrar_rail_fence(texto_cifrado: str, rieles: int, relleno: str = 'X', alfabeto: Alfabeto = None) -> str:
    """
    Función de conveniencia para descifrar con Rail Fence.

    Args:
        texto_cifrado: Texto a descifrar
        rieles: Número de rieles
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
    if not isinstance(rieles, int):
        raise TypeError("El número de rieles debe ser un número entero")
    if not isinstance(relleno, str):
        raise TypeError("El carácter de relleno debe ser una cadena de caracteres")
    if alfabeto is not None and not isinstance(alfabeto, Alfabeto):
        raise TypeError("El alfabeto debe ser una instancia de la clase Alfabeto")

    rail_fence = CifradoRailFence(rieles, relleno, alfabeto)
    return rail_fence.descifrar(texto_cifrado)


if __name__ == "__main__":
    # Ejemplo de uso
    rail_fence = CifradoRailFence(3)
    mensaje = "ATAQUE AL AMANECER"
    cifrado = rail_fence.cifrar(mensaje)
    descifrado = rail_fence.descifrar(cifrado)

    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")