# utilidades.py
# Funciones de utilidad para los cifrados clásicos

import string
from typing import Dict, List, Tuple, Optional
from collections import Counter


class Alfabeto:
    """Clase para manejar alfabetos personalizados"""

    def __init__(self, alfabeto_personalizado: Optional[str] = None, case_sensitive: bool = False):
        """
        Constructor del alfabeto.

        Args:
            alfabeto_personalizado: Alfabeto personalizado (opcional)
            case_sensitive: Si el alfabeto distingue mayúsculas/minúsculas
        """
        if alfabeto_personalizado:
            self.alfabeto = alfabeto_personalizado
            # Verificar caracteres únicos
            if len(set(alfabeto_personalizado)) != len(alfabeto_personalizado):
                raise ValueError("El alfabeto contiene caracteres duplicados")
        else:
            # Alfabeto por defecto (inglés)
            self.alfabeto = string.ascii_uppercase
            if not case_sensitive:
                self.alfabeto += string.ascii_lowercase

        self.case_sensitive = case_sensitive

    def obtener_longitud(self) -> int:
        """Obtiene la longitud del alfabeto"""
        return len(self.alfabeto)

    def obtener_indice(self, caracter: str) -> int:
        """Obtiene el índice de un carácter en el alfabeto"""
        try:
            return self.alfabeto.index(caracter)
        except ValueError:
            return -1

    def obtener_caracter(self, indice: int) -> str:
        """Obtiene el carácter en una posición del alfabeto"""
        if 0 <= indice < len(self.alfabeto):
            return self.alfabeto[indice]
        raise IndexError("Índice fuera del rango del alfabeto")

    def contiene_caracter(self, caracter: str) -> bool:
        """Verifica si un carácter está en el alfabeto"""
        return caracter in self.alfabeto

    def normalizar_texto(self, texto: str) -> str:
        """Normaliza el texto según el alfabeto"""
        resultado = ""
        for c in texto:
            if self.contiene_caracter(c):
                resultado += c
            elif not self.case_sensitive and c.isalpha():
                resultado += c.upper()
        return resultado

    def filtrar_texto(self, texto: str) -> str:
        """Filtra el texto dejando solo caracteres del alfabeto"""
        return "".join(c for c in texto if self.contiene_caracter(c))


def calcular_mcd(a: int, b: int) -> int:
    """Calcula el máximo común divisor usando el algoritmo de Euclides"""
    while b != 0:
        a, b = b, a % b
    return a


def calcular_inverso_modular(a: int, m: int) -> int:
    """Calcula el inverso modular usando el algoritmo extendido de Euclides"""
    m0, y, x = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        y, x = x - q * y, y
    if x < 0:
        x += m0
    return x


def analizar_frecuencia(texto: str) -> Dict[str, int]:
    """Realiza análisis de frecuencia de letras en un texto"""
    texto_limpio = "".join(c.upper() for c in texto if c.isalpha())
    return dict(Counter(texto_limpio))


def ordenar_columnas(clave: str) -> List[int]:
    """Ordena las columnas según la clave para transposiciones"""
    caracteres = [(c.upper(), i) for i, c in enumerate(clave)]
    caracteres_ordenados = sorted(caracteres, key=lambda x: (x[0], x[1]))
    return [i for _, i in caracteres_ordenados]


def validar_texto(texto: str, alfabeto: Alfabeto) -> bool:
    """Valida que el texto contenga solo caracteres válidos"""
    for c in texto:
        if not alfabeto.contiene_caracter(c) and not c.isspace():
            return False
    return True


def limpiar_texto(texto: str) -> str:
    """Limpia el texto eliminando espacios y convirtiendo a mayúsculas"""
    return "".join(c.upper() for c in texto if not c.isspace())