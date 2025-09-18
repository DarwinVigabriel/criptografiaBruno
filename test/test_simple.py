#!/usr/bin/env python3
"""
Script de prueba simple para verificar que la estructura funciona
"""

from CifDesplazamiento.cifrado_cesar import CifradoCesar
from CifSustitucion.cifrado_atbash import cifrar_atbash
from utilidades import analizar_frecuencia

def test_basico():
    print("Probando funcionalidades básicas...")

    # César
    cesar = CifradoCesar(3)
    mensaje = "HOLA"
    cifrado = cesar.cifrar(mensaje)
    descifrado = cesar.descifrar(cifrado)
    assert descifrado == mensaje, f"César falló: {descifrado} != {mensaje}"
    print("✓ Cifrado César OK")

    # Atbash
    mensaje = "HOLA"
    cifrado = cifrar_atbash(mensaje)
    descifrado = cifrar_atbash(cifrado)
    assert descifrado == mensaje, f"Atbash falló: {descifrado} != {mensaje}"
    print("✓ Cifrado Atbash OK")

    # Utilidades
    texto = "HOLA MUNDO"
    frecuencias = analizar_frecuencia(texto)
    assert 'H' in frecuencias, "Análisis de frecuencia falló"
    print("✓ Utilidades OK")

    print("\n🎉 Pruebas básicas pasaron exitosamente!")

if __name__ == "__main__":
    test_basico()