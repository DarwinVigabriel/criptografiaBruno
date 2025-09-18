#!/usr/bin/env python3
"""
Suite Completa de Pruebas Unitarias
====================================

Este archivo contiene pruebas unitarias exhaustivas para todos los algoritmos
de cifrado implementados en la librería.
"""

import unittest
from CifDesplazamiento.cifrado_cesar import CifradoCesar
from CifDesplazamiento.cifrado_vigenere import CifradoVigenere, cifrar_vigenere, descifrar_vigenere
from CifSustitucion.cifrado_atbash import cifrar_atbash
from CifSustitucion.cifrado_sustitucion_simple import CifradoSustitucionSimple
from CifSustMonoPoli.cifrado_playfair import CifradoPlayfair
from CifSustMonoPoli.cifrado_hill import CifradoHill
from CifSustMonoPoli.cifrado_autokey import cifrar_autokey, descifrar_autokey
from CifSustMonoPoli.cifrado_xor import cifrar_xor, descifrar_xor
from CifTransposicion.cifrado_transposicion_columnas import cifrar_transposicion_columnas, descifrar_transposicion_columnas
from CifTransposicion.cifrado_rail_fence import cifrar_rail_fence, descifrar_rail_fence
from CifTransposicion.cifrado_permutacion_general import CifradoPermutacionGeneral
from utilidades import analizar_frecuencia, limpiar_texto, Alfabeto


class TestCifradoCesar(unittest.TestCase):
    """Pruebas para el cifrado César."""

    def setUp(self):
        self.cesar = CifradoCesar(3)
        self.mensaje = "HOLA MUNDO"

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        cifrado = self.cesar.cifrar(self.mensaje)
        descifrado = self.cesar.descifrar(cifrado)
        # Los cifrados eliminan espacios en el cifrado pero mantienen en descifrado
        self.assertEqual(descifrado, self.mensaje)

    def test_cifrado_basico(self):
        """Prueba cifrado básico."""
        resultado = self.cesar.cifrar("ABC")
        self.assertEqual(resultado, "DEF")

    def test_descifrado_basico(self):
        """Prueba descifrado básico."""
        resultado = self.cesar.descifrar("DEF")
        self.assertEqual(resultado, "ABC")

    def test_ataque_fuerza_bruta(self):
        """Prueba ataque de fuerza bruta."""
        cifrado = self.cesar.cifrar("HOLA")
        ataques = self.cesar.ataque_fuerza_bruta(cifrado)
        self.assertIn("HOLA", ataques)


class TestCifradoVigenere(unittest.TestCase):
    """Pruebas para el cifrado Vigenère."""

    def setUp(self):
        self.vigenere = CifradoVigenere("CLAVE")
        self.mensaje = "HOLA MUNDO"

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        cifrado = self.vigenere.cifrar(self.mensaje)
        descifrado = self.vigenere.descifrar(cifrado)
        # El descifrado mantiene el formato del mensaje original
        self.assertEqual(descifrado, self.mensaje)

    def test_funciones_conveniencia(self):
        """Prueba las funciones de conveniencia."""
        cifrado = cifrar_vigenere("HOLA", "CLAVE")
        descifrado = descifrar_vigenere(cifrado, "CLAVE")
        self.assertEqual(descifrado, "HOLA")

    def test_ataque_analisis_frecuencia(self):
        """Prueba ataque por análisis de frecuencia."""
        cifrado = self.vigenere.cifrar("HOLAMUNDOHOLAMUNDO")
        ataques = self.vigenere.ataque_analisis_frecuencia(cifrado, 5)
        self.assertIsInstance(ataques, list)
        self.assertGreater(len(ataques), 0)


class TestCifradoAtbash(unittest.TestCase):
    """Pruebas para el cifrado Atbash."""

    def test_cifrado_simetrico(self):
        """Prueba que Atbash es simétrico."""
        mensaje = "HOLA"
        cifrado = cifrar_atbash(mensaje)
        descifrado = cifrar_atbash(cifrado)
        self.assertEqual(descifrado, mensaje)

    def test_cifrado_basico(self):
        """Prueba cifrado básico."""
        resultado = cifrar_atbash("ABC")
        self.assertEqual(resultado, "zyx")


class TestCifradoSustitucionSimple(unittest.TestCase):
    """Pruebas para el cifrado de sustitución simple."""

    def setUp(self):
        self.cifrador = CifradoSustitucionSimple("CLAVE")

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        cifrado = self.cifrador.cifrar(mensaje)
        descifrado = self.cifrador.descifrar(cifrado)
        self.assertEqual(descifrado, limpiar_texto(mensaje))

    def test_con_clave(self):
        """Prueba con clave específica."""
        cifrador = CifradoSustitucionSimple("ABC")
        resultado = cifrador.cifrar("DEF")
        self.assertNotEqual(resultado, "DEF")

    def test_sin_clave(self):
        """Prueba sin clave (rotación simple)."""
        cifrador = CifradoSustitucionSimple()
        mensaje = "ABC"
        cifrado = cifrador.cifrar(mensaje)
        descifrado = cifrador.descifrar(cifrado)
        self.assertEqual(descifrado, mensaje)


class TestCifradoPlayfair(unittest.TestCase):
    """Pruebas para el cifrado Playfair."""

    def setUp(self):
        self.playfair = CifradoPlayfair("CLAVE")

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        cifrado = self.playfair.cifrar(mensaje)
        descifrado = self.playfair.descifrar(cifrado)
        self.assertEqual(descifrado, mensaje.upper().replace(" ", ""))

    def test_manejo_digrafos(self):
        """Prueba manejo de dígrafo I/J."""
        mensaje = "JIJI"
        cifrado = self.playfair.cifrar(mensaje)
        descifrado = self.playfair.descifrar(cifrado)
        self.assertEqual(descifrado, "JIJI")


class TestCifradoHill(unittest.TestCase):
    """Pruebas para el cifrado Hill."""

    def setUp(self):
        self.hill = CifradoHill([[3, 3], [2, 5]], "CLAVE")

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA"
        cifrado = self.hill.cifrar(mensaje)
        descifrado = self.hill.descifrar(cifrado)
        self.assertEqual(descifrado, mensaje)

    def test_matriz_invalida(self):
        """Prueba que matrices no invertibles lanzan error."""
        with self.assertRaises(ValueError):
            CifradoHill([[2, 2], [4, 4]])  # Matriz singular


class TestCifradoAutokey(unittest.TestCase):
    """Pruebas para el cifrado Autokey."""

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        clave = "CLAVE"
        cifrado = cifrar_autokey(mensaje, clave)
        descifrado = descifrar_autokey(cifrado, clave)
        self.assertEqual(descifrado, limpiar_texto(mensaje))


class TestCifradoXOR(unittest.TestCase):
    """Pruebas para el cifrado XOR."""

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        clave = "CLAVE"
        cifrado = cifrar_xor(mensaje, clave)
        descifrado = descifrar_xor(cifrado, clave)
        # XOR mantiene espacios y caracteres especiales
        self.assertEqual(descifrado, mensaje)


class TestCifradoTransposicionColumnas(unittest.TestCase):
    """Pruebas para la transposición por columnas."""

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        clave = "CLAVE"
        cifrado = cifrar_transposicion_columnas(mensaje, clave)
        descifrado = descifrar_transposicion_columnas(cifrado, clave)
        # La transposición mantiene espacios
        self.assertEqual(descifrado, mensaje)


class TestCifradoRailFence(unittest.TestCase):
    """Pruebas para el cifrado Rail Fence."""

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "HOLA MUNDO"
        rails = 3
        cifrado = cifrar_rail_fence(mensaje, rails)
        descifrado = descifrar_rail_fence(cifrado, rails)
        # Rail Fence puede agregar padding, verificar que contiene el mensaje original
        self.assertIn(limpiar_texto(mensaje), descifrado)


class TestCifradoPermutacionGeneral(unittest.TestCase):
    """Pruebas para la permutación general."""

    def setUp(self):
        self.cifrador = CifradoPermutacionGeneral("CLAVE")

    def test_cifrado_descifrado(self):
        """Prueba que cifrar y descifrar devuelve el mensaje original."""
        mensaje = "ATAQUEALAMANECER"
        cifrado = self.cifrador.cifrar(mensaje)
        descifrado = self.cifrador.descifrar(cifrado)
        self.assertEqual(descifrado, mensaje)

    def test_metodo_numerico(self):
        """Prueba método numérico."""
        cifrador = CifradoPermutacionGeneral("3142", "numerico")
        mensaje = "HOLA"
        cifrado = cifrador.cifrar(mensaje)
        descifrado = cifrador.descifrar(cifrado)
        self.assertEqual(descifrado, mensaje)


class TestUtilidades(unittest.TestCase):
    """Pruebas para las funciones de utilidad."""

    def test_analizar_frecuencia(self):
        """Prueba análisis de frecuencia."""
        texto = "HOLA HOLA"
        frecuencias = analizar_frecuencia(texto)
        self.assertIsInstance(frecuencias, dict)
        self.assertGreater(frecuencias.get('H', 0), 0)

    def test_limpiar_texto(self):
        """Prueba limpieza de texto."""
        texto = "Hola Mundo 123!"
        limpio = limpiar_texto(texto)
        # limpiar_texto solo elimina espacios y convierte a mayúsculas
        self.assertEqual(limpio, "HOLAMUNDO123!")

    def test_clase_alfabeto(self):
        """Prueba clase Alfabeto."""
        alfabeto = Alfabeto()
        self.assertTrue(alfabeto.contiene_caracter('A'))
        self.assertFalse(alfabeto.contiene_caracter('1'))


if __name__ == '__main__':
    # Configurar verbosidad
    unittest.main(verbosity=2)