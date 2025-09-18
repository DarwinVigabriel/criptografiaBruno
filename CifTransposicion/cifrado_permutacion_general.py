"""
Cifrado de Permutación General
=============================

Este módulo implementa un cifrado de transposición por permutación general,
donde el orden de las posiciones se determina mediante una clave numérica
o alfabética.
"""

from typing import List, Optional
from utilidades import limpiar_texto, ordenar_columnas


class CifradoPermutacionGeneral:
    """
    Cifrado de transposición por permutación general.
    """

    def __init__(self, clave: str, metodo: str = "alfabetico"):
        """
        Constructor del cifrado de permutación general.

        Args:
            clave: Clave que determina el orden de permutación.
            metodo: Método para ordenar ("alfabetico" o "numerico").
                   - "alfabetico": ordena alfabéticamente
                   - "numerico": trata la clave como números

        Raises:
            TypeError: Si los parámetros tienen tipos incorrectos
            ValueError: Si los parámetros tienen valores inválidos
        """
        if not isinstance(clave, str):
            raise TypeError("La clave debe ser una cadena de caracteres")
        if not isinstance(metodo, str):
            raise TypeError("El método debe ser una cadena de caracteres")

        clave_limpia = clave.strip()
        if not clave_limpia:
            raise ValueError("La clave no puede estar vacía")

        metodo_lower = metodo.lower()
        if metodo_lower not in ["alfabetico", "numerico"]:
            raise ValueError("El método debe ser 'alfabetico' o 'numerico'")

        self.clave = clave_limpia.upper()
        self.metodo = metodo_lower
        self.orden_permutacion = self._calcular_orden_permutacion()

    def _calcular_orden_permutacion(self) -> List[int]:
        """
        Calcula el orden de permutación basado en la clave.

        Returns:
            Lista con los índices en orden de permutación.
        """
        if self.metodo == "numerico":
            # Para método numérico, convertir cada dígito a entero
            try:
                # Si la clave contiene números, usarlos directamente
                indices = [int(c) - 1 for c in self.clave if c.isdigit()]
                # Si no hay suficientes números, completar con orden alfabético
                if len(indices) < len(self.clave):
                    indices_alfabetico = ordenar_columnas(self.clave)
                    indices.extend(indices_alfabetico[len(indices):])
                return indices[:len(self.clave)]
            except ValueError:
                # Si falla, usar método alfabético
                return ordenar_columnas(self.clave)
        else:
            # Método alfabético por defecto
            return ordenar_columnas(self.clave)

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando permutación general.

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

        # Si el texto es más corto que la clave, no se puede permutar
        if len(texto_limpio) < len(self.clave):
            return texto_limpio

        # Dividir el texto en bloques del tamaño de la clave
        bloques_cifrados = []

        for i in range(0, len(texto_limpio), len(self.clave)):
            bloque = texto_limpio[i:i + len(self.clave)]

            # Si el bloque es más corto que la clave, no lo permutamos
            if len(bloque) < len(self.clave):
                bloques_cifrados.append(bloque)
                continue

            # Crear bloque permutado
            bloque_permutado = [''] * len(bloque)
            for j, pos in enumerate(self.orden_permutacion):
                if j < len(bloque):
                    bloque_permutado[pos] = bloque[j]

            bloques_cifrados.append(''.join(bloque_permutado))

        return ''.join(bloques_cifrados)

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto usando permutación general.

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

        # Si el texto es más corto que la clave, no se puede despermutar
        if len(texto_limpio) < len(self.clave):
            return texto_limpio

        # Dividir el texto en bloques del tamaño de la clave
        bloques_descifrados = []

        for i in range(0, len(texto_limpio), len(self.clave)):
            bloque = texto_limpio[i:i + len(self.clave)]

            # Si el bloque es más corto que la clave, no lo despermutamos
            if len(bloque) < len(self.clave):
                bloques_descifrados.append(bloque)
                continue

            # Crear bloque original
            bloque_original = [''] * len(bloque)
            for j, pos in enumerate(self.orden_permutacion):
                if j < len(bloque):
                    bloque_original[j] = bloque[pos]

            bloques_descifrados.append(''.join(bloque_original))

        return ''.join(bloques_descifrados)


# Funciones de conveniencia
def cifrar_permutacion_general(texto: str, clave: str, metodo: str = "alfabetico") -> str:
    """
    Función de conveniencia para cifrar con permutación general.

    Args:
        texto: Texto a cifrar.
        clave: Clave para la permutación.
        metodo: Método de ordenamiento ("alfabetico" o "numerico").

    Returns:
        Texto cifrado.

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres")
    if not isinstance(metodo, str):
        raise TypeError("El método debe ser una cadena de caracteres")

    cifrador = CifradoPermutacionGeneral(clave, metodo)
    return cifrador.cifrar(texto)


def descifrar_permutacion_general(texto: str, clave: str, metodo: str = "alfabetico") -> str:
    """
    Función de conveniencia para descifrar con permutación general.

    Args:
        texto: Texto a descifrar.
        clave: Clave usada para el cifrado.
        metodo: Método de ordenamiento usado.

    Returns:
        Texto plano.

    Raises:
        TypeError: Si los parámetros tienen tipos incorrectos
        ValueError: Si los parámetros tienen valores inválidos
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")
    if not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de caracteres")
    if not isinstance(metodo, str):
        raise TypeError("El método debe ser una cadena de caracteres")

    cifrador = CifradoPermutacionGeneral(clave, metodo)
    return cifrador.descifrar(texto)


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    print("=== Cifrado de Permutación General ===")

    clave = "CLAVE"
    mensaje = "ATAQUEALAMANECER"

    print(f"Mensaje original: {mensaje}")
    print(f"Clave: {clave}")

    # Método alfabético
    print("\n--- Método Alfabético ---")
    cifrador_alfabetico = CifradoPermutacionGeneral(clave, "alfabetico")
    print(f"Orden de permutación: {cifrador_alfabetico.orden_permutacion}")

    cifrado_alfabetico = cifrador_alfabetico.cifrar(mensaje)
    print(f"Mensaje cifrado: {cifrado_alfabetico}")

    descifrado_alfabetico = cifrador_alfabetico.descifrar(cifrado_alfabetico)
    print(f"Mensaje descifrado: {descifrado_alfabetico}")
    print(f"¿Descifrado correcto?: {descifrado_alfabetico == mensaje}")

    # Método numérico
    print("\n--- Método Numérico ---")
    clave_numerica = "3142"  # clave numérica
    cifrador_numerico = CifradoPermutacionGeneral(clave_numerica, "numerico")
    print(f"Clave numérica: {clave_numerica}")
    print(f"Orden de permutación: {cifrador_numerico.orden_permutacion}")

    cifrado_numerico = cifrador_numerico.cifrar(mensaje)
    print(f"Mensaje cifrado: {cifrado_numerico}")

    descifrado_numerico = cifrador_numerico.descifrar(cifrado_numerico)
    print(f"Mensaje descifrado: {descifrado_numerico}")
    print(f"¿Descifrado correcto?: {descifrado_numerico == mensaje}")

    # Texto más largo
    print("\n--- Texto más largo ---")
    texto_largo = "ESTEESUNMENSAJEMASLARGOPARAPROBARLAPERMUTACIONGENERAL"
    cifrado_largo = cifrador_alfabetico.cifrar(texto_largo)
    descifrado_largo = cifrador_alfabetico.descifrar(cifrado_largo)

    print(f"Texto largo cifrado: {cifrado_largo}")
    print(f"Texto largo descifrado: {descifrado_largo}")
    print(f"¿Descifrado correcto?: {descifrado_largo == texto_largo}")