# Cifrado XOR

## Descripción General

El **cifrado XOR** (OR exclusivo) es una operación lógica fundamental que sirve como base para muchos algoritmos criptográficos modernos. A diferencia de los cifrados clásicos que operan sobre caracteres alfabéticos, XOR trabaja a nivel de **bits**, convirtiendo el texto en una secuencia de bits y aplicando la operación XOR bit a bit con una clave.

Es uno de los cifrados más simples y eficientes, pero también uno de los más poderosos cuando se usa correctamente. Es la base del **one-time pad perfecto** y componente esencial de algoritmos como AES, RC4, y muchos otros.

## Historia y Contexto

### Origen y Desarrollo
- **Siglo XIX**: Desarrollo de lógica booleana por George Boole
- **1917**: Gilbert Vernam patenta el one-time pad usando XOR
- **1940s**: Usado en máquinas de cifrado militares (SIGABA)
- **Era digital**: Base de todos los cifrados de flujo modernos

### Importancia Histórica
- **One-time pad**: Primer cifrado matemáticamente inquebrable
- **Base computacional**: Todos los cifrados digitales usan XOR
- **Simplicidad elegante**: Una operación que lo hace todo
- **Transición digital**: Puente entre criptografía clásica y moderna

### Terminología
- **Operación binaria**: Trabaja con bits, no caracteres
- **Cifrado de flujo**: Procesa datos bit a bit o byte a byte
- **Simétrico perfecto**: Mismo algoritmo para cifrar y descifrar
- **One-time pad**: Caso especial con clave aleatoria única

## Lógica Matemática

### Definición Formal

La operación XOR (⊕) se define como:

**a ⊕ b = 1 si a ≠ b**
**a ⊕ b = 0 si a = b**

Para cifrado: **Cᵢ = Pᵢ ⊕ Kᵢ**
Para descifrado: **Pᵢ = Cᵢ ⊕ Kᵢ**

Donde:
- Pᵢ es el i-ésimo bit del texto plano
- Kᵢ es el i-ésimo bit de la clave
- Cᵢ es el i-ésimo bit del texto cifrado

### Propiedades Matemáticas

1. **Asociativa**: (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
2. **Conmutativa**: a ⊕ b = b ⊕ a
3. **Autoinversa**: a ⊕ a = 0 (XOR consigo mismo = 0)
4. **Identidad**: a ⊕ 0 = a (XOR con 0 no cambia nada)

### Tabla de Verdad XOR

| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

### XOR con Bytes

Para datos de 8 bits (bytes):
```
A = 10110011
B = 01101101
A ⊕ B = 11011110
```

Cada bit se procesa independientemente.

## Algoritmo Detallado

### Implementación Básica

```python
def xor_bytes(datos, clave):
    """Aplica XOR byte a byte"""
    resultado = bytearray()
    clave_bytes = clave.encode('utf-8')

    for i, byte in enumerate(datos):
        clave_byte = clave_bytes[i % len(clave_bytes)]
        resultado.append(byte ^ clave_byte)

    return bytes(resultado)
```

### Cifrado de Flujo

```python
def cifrar_xor_flujo(texto_plano, clave):
    """Cifrado XOR con clave repetida"""
    texto_bytes = texto_plano.encode('utf-8')
    clave_bytes = clave.encode('utf-8')

    resultado = bytearray()
    for i, byte in enumerate(texto_bytes):
        clave_byte = clave_bytes[i % len(clave_bytes)]
        resultado.append(byte ^ clave_byte)

    return bytes(resultado)
```

### One-Time Pad (OTP)

```python
def cifrar_otp(texto_plano, clave_aleatoria):
    """One-time pad perfecto"""
    if len(clave_aleatoria) != len(texto_plano):
        raise ValueError("La clave debe tener el mismo tamaño que el mensaje")

    texto_bytes = texto_plano.encode('utf-8')
    clave_bytes = clave_aleatoria.encode('utf-8')

    resultado = bytearray()
    for byte_texto, byte_clave in zip(texto_bytes, clave_bytes):
        resultado.append(byte_texto ^ byte_clave)

    return bytes(resultado)
```

## Ejemplos Detallados

### Ejemplo 1: XOR con Caracteres ASCII
```
Mensaje: "HI" (ASCII: H=72=01001000, I=73=01001001)
Clave: "A" (ASCII: A=65=01000001)

H ⊕ A = 01001000 ⊕ 01000001 = 00001001 = 9 = '\t'
I ⊕ A = 01001001 ⊕ 01000001 = 00001000 = 8 = '\b'

Resultado: "\t\b"
```

### Ejemplo 2: Clave Repetida
```
Mensaje: "HELLO"
Clave: "AB"

Convertir a bytes:
H(72) E(69) L(76) L(76) O(79)
A(65) B(66) A(65) B(66) A(65)

XOR:
72 ⊕ 65 = 9
69 ⊕ 66 = 103
76 ⊕ 65 = 9
76 ⊕ 66 = 102
79 ⊕ 65 = 110

Resultado bytes: [9, 103, 9, 102, 110]
En base64: "CWcJZg=="
```

### Ejemplo 3: Autodescifrado
```
Mensaje: "ABC"
Clave: "XYZ"

Cifrado: A⊕X, B⊕Y, C⊕Z
Descifrado: (A⊕X)⊕X = A, (B⊕Y)⊕Y = B, (C⊕Z)⊕Z = C

Verificación:
A⊕X⊕X = A⊕(X⊕X) = A⊕0 = A ✓
```

### Ejemplo 4: One-Time Pad
```
Mensaje: "TOP"
Clave aleatoria: "R\x8F\x42" (3 bytes aleatorios)

T(84) ⊕ R(82) = 6
O(79) ⊕ \x8F(143) = 192
P(80) ⊕ \x42(66) = 114

Resultado: bytes [6, 192, 114]
```

### Ejemplo 5: XOR con Números Binarios
```
Mensaje: 10110011 01101101 11001010
Clave:   00110100 10011011 01100110

XOR:    10000111 11110110 10101100

Mensaje original: 179, 109, 202
Clave:           52, 155, 102
Resultado:       135, 246, 172
```

## Criptoanálisis (Ataques)

### Ataque por Clave Conocida

**Método**: Si se conoce la clave, trivial.
**Complejidad**: O(1) - instantáneo

### Ataque por Texto Plano Conocido

**Principio**: Si se conoce P y C, entonces K = P ⊕ C

**Ejemplo**:
```
Conocido: P = "HELLO", C = bytes([9, 103, 9, 102, 110])
K = P ⊕ C = "HELLO" ⊕ [9, 103, 9, 102, 110] = "ABABA"
```

### Ataque por Fuerza Bruta

**Complejidad**: 2^(8×longitud_clave) para clave de n bytes
- Clave de 1 byte: 256 posibilidades
- Clave de 8 bytes: 2^64 ≈ 10^18 posibilidades

### Análisis de Frecuencia en Clave Repetida

**Método**: Si la clave se repite, aparecen patrones.

**Ejemplo**:
```
Texto cifrado con clave "AB": C₁ C₂ C₃ C₄ C₅
Si clave se repite cada 2: C₁⊕C₃, C₂⊕C₄ deberían tener propiedades
```

### Ataque al One-Time Pad Reutilizado

**Peligo crítico**: Nunca reutilizar la misma clave OTP
```
Mensaje1 ⊕ Clave = Cifrado1
Mensaje2 ⊕ Clave = Cifrado2
Cifrado1 ⊕ Cifrado2 = Mensaje1 ⊕ Mensaje2
```

Conociendo un mensaje, se puede recuperar el otro.

## Variantes y Extensiones

### XOR con Retroalimentación (Cifrado de Flujo)
- La clave se genera dinámicamente
- Similar a RC4 pero más simple

### XOR en Modo CBC
- XOR con bloque anterior
- Proporciona difusión

### XOR con Salsa20
- Generador de clave criptográfico
- Base de ChaCha20

### XOR en Hardware
- Implementación en circuitos digitales
- Muy eficiente en FPGA/ASIC

## Análisis de Seguridad

### Fortalezas
- **Rápido**: Operación más eficiente en computadoras
- **Simple**: Fácil de implementar y verificar
- **Reversible**: Sin pérdida de información
- **Paralelizable**: Cada bit independiente

### Debilidades
- **Clave reutilizada**: Catastrófico
- **Clave predecible**: Inseguro
- **Sin difusión**: Un bit cambiado afecta solo ese bit
- **Sin integridad**: No detecta modificaciones

### Seguridad por Caso de Uso

| Escenario | Seguridad | Recomendación |
|-----------|-----------|---------------|
| One-time pad | Perfecta | Usar con clave aleatoria única |
| Clave fija | Muy baja | No usar |
| Clave derivada | Media | Usar con algoritmos modernos |
| Componente de AES | Muy alta | Parte de estándar |

## Aplicaciones Modernas

### En Algoritmos Estándar
- **AES**: XOR en cada ronda
- **RC4**: Generador de flujo basado en XOR
- **ChaCha20**: XOR con secuencia generada
- **Salsa20**: Similar a ChaCha20

### En Protocolos
- **HTTPS**: Parte de TLS
- **WiFi WPA2**: En cifrados de flujo
- **VPN**: Componente de IPsec
- **SSH**: En algoritmos de cifrado

### En Sistemas Embebidos
- **Microcontroladores**: XOR para ofuscación simple
- **IoT**: Cifrado ligero
- **Smart cards**: Operaciones básicas

### En Desarrollo de Software
- **Ofuscación**: Protección básica de código
- **Checksums**: Verificación de integridad simple
- **Generadores**: Números pseudoaleatorios

## Implementación Completa

```python
import base64
import os
from typing import Union, bytes as BytesType

class CifradoXOR:
    """
    Implementación del cifrado XOR.
    Soporta modo de flujo con clave repetida y one-time pad.
    """

    def __init__(self, clave: Union[str, bytes]):
        """
        Inicializa el cifrado XOR.

        Args:
            clave: Clave como string o bytes
        """
        if isinstance(clave, str):
            self.clave = clave.encode('utf-8')
        else:
            self.clave = clave

        if len(self.clave) == 0:
            raise ValueError("La clave no puede estar vacía")

    def _xor_bytes(self, datos: bytes) -> bytes:
        """Aplica XOR byte a byte con clave repetida"""
        resultado = bytearray()

        for i, byte in enumerate(datos):
            clave_byte = self.clave[i % len(self.clave)]
            resultado.append(byte ^ clave_byte)

        return bytes(resultado)

    def cifrar(self, datos: Union[str, bytes]) -> bytes:
        """
        Cifra datos usando XOR.

        Args:
            datos: Datos a cifrar (string o bytes)

        Returns:
            Datos cifrados como bytes
        """
        if isinstance(datos, str):
            datos_bytes = datos.encode('utf-8')
        else:
            datos_bytes = datos

        return self._xor_bytes(datos_bytes)

    def descifrar(self, datos_cifrados: bytes) -> bytes:
        """
        Descifra datos cifrados con XOR.
        (Es idéntico al cifrado)

        Args:
            datos_cifrados: Datos a descifrar

        Returns:
            Datos descifrados como bytes
        """
        return self._xor_bytes(datos_cifrados)

    def cifrar_a_base64(self, datos: Union[str, bytes]) -> str:
        """
        Cifra y codifica en base64 para transmisión segura.

        Args:
            datos: Datos a cifrar

        Returns:
            String en base64
        """
        cifrado = self.cifrar(datos)
        return base64.b64encode(cifrado).decode('ascii')

    def descifrar_de_base64(self, datos_base64: str) -> bytes:
        """
        Descifra desde base64.

        Args:
            datos_base64: Datos cifrados en base64

        Returns:
            Datos descifrados como bytes
        """
        try:
            datos_cifrados = base64.b64decode(datos_base64)
            return self.descifrar(datos_cifrados)
        except Exception as e:
            raise ValueError(f"Error al decodificar base64: {e}")

class OneTimePad:
    """
    Implementación del one-time pad perfecto usando XOR.
    """

    @staticmethod
    def generar_clave(longitud: int) -> bytes:
        """
        Genera una clave aleatoria para one-time pad.

        Args:
            longitud: Longitud de la clave en bytes

        Returns:
            Clave aleatoria
        """
        return os.urandom(longitud)

    @staticmethod
    def cifrar(mensaje: Union[str, bytes], clave: bytes) -> bytes:
        """
        Cifra usando one-time pad.

        Args:
            mensaje: Mensaje a cifrar
            clave: Clave aleatoria (mismo tamaño que mensaje)

        Returns:
            Mensaje cifrado

        Raises:
            ValueError: Si clave y mensaje tienen tamaños diferentes
        """
        if isinstance(mensaje, str):
            mensaje_bytes = mensaje.encode('utf-8')
        else:
            mensaje_bytes = mensaje

        if len(clave) != len(mensaje_bytes):
            raise ValueError("La clave debe tener el mismo tamaño que el mensaje")

        resultado = bytearray()
        for byte_mensaje, byte_clave in zip(mensaje_bytes, clave):
            resultado.append(byte_mensaje ^ byte_clave)

        return bytes(resultado)

    @staticmethod
    def descifrar(cifrado: bytes, clave: bytes) -> bytes:
        """
        Descifra one-time pad.

        Args:
            cifrado: Mensaje cifrado
            clave: Clave usada para cifrar

        Returns:
            Mensaje descifrado
        """
        if len(clave) != len(cifrado):
            raise ValueError("La clave debe tener el mismo tamaño que el cifrado")

        return OneTimePad.cifrar(cifrado, clave)  # XOR es simétrico

# Funciones de conveniencia
def cifrar_xor(datos: Union[str, bytes], clave: Union[str, bytes]) -> bytes:
    """Función de conveniencia para cifrar con XOR"""
    xor = CifradoXOR(clave)
    return xor.cifrar(datos)

def descifrar_xor(datos_cifrados: bytes, clave: Union[str, bytes]) -> bytes:
    """Función de conveniencia para descifrar con XOR"""
    xor = CifradoXOR(clave)
    return xor.descifrar(datos_cifrados)

def cifrar_xor_base64(datos: Union[str, bytes], clave: Union[str, bytes]) -> str:
    """Cifra y devuelve en base64"""
    xor = CifradoXOR(clave)
    return xor.cifrar_a_base64(datos)

def descifrar_xor_base64(datos_base64: str, clave: Union[str, bytes]) -> bytes:
    """Descifra desde base64"""
    xor = CifradoXOR(clave)
    return xor.descifrar_de_base64(datos_base64)

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo básico
    mensaje = "HELLO WORLD"
    clave = "SECRET"

    print(f"Mensaje: {mensaje}")
    print(f"Clave: {clave}")

    # Cifrado XOR
    cifrado = cifrar_xor(mensaje, clave)
    print(f"Cifrado (bytes): {cifrado}")
    print(f"Cifrado (base64): {cifrar_xor_base64(mensaje, clave)}")

    # Descifrado
    descifrado = descifrar_xor(cifrado, clave)
    print(f"Descifrado: {descifrado.decode('utf-8')}")

    # Verificar
    print(f"¿Correcto? {mensaje == descifrado.decode('utf-8')}")

    # One-time pad
    print("\n--- One-Time Pad ---")
    mensaje_bytes = mensaje.encode('utf-8')
    clave_otp = OneTimePad.generar_clave(len(mensaje_bytes))

    cifrado_otp = OneTimePad.cifrar(mensaje_bytes, clave_otp)
    descifrado_otp = OneTimePad.descifrar(cifrado_otp, clave_otp)

    print(f"Mensaje OTP: {mensaje_bytes}")
    print(f"Clave OTP: {clave_otp.hex()}")
    print(f"Cifrado OTP: {cifrado_otp.hex()}")
    print(f"Descifrado OTP: {descifrado_otp.decode('utf-8')}")
    print(f"¿OTP correcto? {mensaje == descifrado_otp.decode('utf-8')}")

    # Demostración de propiedades XOR
    print("\n--- Propiedades XOR ---")
    a = bytes([0b10101010])
    b = bytes([0b11001100])
    cero = bytes([0b00000000])

    print(f"A: {a[0]:08b}")
    print(f"B: {b[0]:08b}")
    print(f"A ⊕ B: {cifrar_xor(a, b)[0]:08b}")
    print(f"A ⊕ A: {cifrar_xor(a, a)[0]:08b} (debe ser 0)")
    print(f"A ⊕ 0: {cifrar_xor(a, cero)[0]:08b} (debe ser A)")
```

## Conclusión

El cifrado XOR es un **cimiento fundamental** de la criptografía moderna. Su simplicidad matemática esconde un poder extraordinario: cuando se usa correctamente (como one-time pad), proporciona **seguridad perfecta inquebrable**. Cuando se usa incorrectamente, es completamente vulnerable.

**Lecciones clave**:
- **Simplicidad ≠ debilidad**: Una operación básica puede ser criptográficamente fuerte
- **Clave es todo**: La calidad de la clave determina la seguridad
- **No reutilizar**: Nunca usar la misma clave dos veces
- **Base moderna**: Todos los cifrados digitales dependen de XOR

Su estudio es esencial para entender cómo la criptografía evolucionó desde métodos manuales alfabéticos hacia algoritmos computacionales basados en operaciones binarias, sentando las bases para toda la ciberseguridad contemporánea.