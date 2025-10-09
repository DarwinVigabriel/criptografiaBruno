# Cifrado Autokey

## Descripción General

El **cifrado Autokey** es una variante polialfabética del Vigenère donde la clave se **autogenera** a partir del propio mensaje. Inventado por Blaise de Vigenère en el siglo XVI, es más seguro que el Vigenère estándar porque elimina las repeticiones periódicas de la clave.

En lugar de repetir una clave fija, el Autokey usa una **clave inicial** y luego incorpora los caracteres del mensaje mismo para extender la clave, creando una secuencia de clave única para cada mensaje.

## Historia y Contexto

### Origen y Desarrollo
- **Siglo XVI**: Blaise de Vigenère describe el método en "Traicté des Chiffres"
- **Siglo XIX**: Redescubierto por criptógrafos europeos
- **Primera Guerra Mundial**: Considerado para uso militar
- **Era moderna**: Base para generadores de clave en cifrados de flujo

### Importancia Histórica
- **Mejora del Vigenère**: Soluciona la debilidad de repetición periódica
- **Primer sistema autogenérico**: La clave crece con el mensaje
- **Transición conceptual**: De claves fijas a claves dinámicas
- **Influencia moderna**: Precursor de cifrados de flujo como RC4

### Terminología
- **Clave inicial**: Semilla que inicia el proceso
- **Autogeneración**: La clave se construye del mensaje mismo
- **Cifrado de flujo**: Cada carácter usa una clave diferente
- **Sin repetición**: No hay período fijo como en Vigenère

## Lógica Matemática

### Definición Formal

Sea K = k₁k₂...kₘ la clave inicial y M = m₁m₂...mₙ el mensaje. La clave extendida se construye como:

**K' = k₁k₂...kₘ m₁m₂...mₙ₋₁**

El cifrado es:
**Cᵢ = (mᵢ + k'ᵢ) mod 26**

Donde k'ᵢ es el i-ésimo carácter de la clave extendida.

### Propiedades Matemáticas

1. **No periódico**: La clave nunca se repite exactamente
2. **Dependiente del mensaje**: Cada mensaje genera su propia clave extendida
3. **Longitud variable**: La clave crece con el mensaje
4. **Autoinverso**: El mismo algoritmo puede cifrar y descifrar

### Comparación con Vigenère

| Aspecto | Vigenère | Autokey |
|---------|----------|---------|
| Periodicidad | Sí (longitud de clave) | No |
| Repeticiones | Cada período idéntico | Nunca idénticas |
| Longitud clave | Fija | Crece con mensaje |
| Seguridad | Media | Alta |

## Algoritmo Detallado

### Cifrado Autokey

```python
def cifrar_autokey(mensaje, clave_inicial):
    resultado = ""
    clave_extendida = clave_inicial

    for caracter in mensaje:
        if caracter.isalpha():
            # Convertir a índices
            indice_mensaje = ord(caracter.upper()) - ord('A')
            indice_clave = ord(clave_extendida[0].upper()) - ord('A')

            # Cifrar
            indice_cifrado = (indice_mensaje + indice_clave) % 26
            caracter_cifrado = chr(indice_cifrado + ord('A'))

            # Mantener caso
            if caracter.islower():
                caracter_cifrado = caracter_cifrado.lower()

            resultado += caracter_cifrado

            # Agregar caracter original a clave extendida
            clave_extendida += caracter.upper()
        else:
            resultado += caracter

        # Remover primer caracter usado
        clave_extendida = clave_extendida[1:]

    return resultado
```

### Descifrado Autokey

```python
def descifrar_autokey(mensaje_cifrado, clave_inicial):
    resultado = ""
    clave_extendida = clave_inicial

    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            # Convertir a índices
            indice_cifrado = ord(caracter.upper()) - ord('A')
            indice_clave = ord(clave_extendida[0].upper()) - ord('A')

            # Descifrar
            indice_mensaje = (indice_cifrado - indice_clave) % 26
            caracter_mensaje = chr(indice_mensaje + ord('A'))

            # Mantener caso
            if caracter.islower():
                caracter_mensaje = caracter_mensaje.lower()

            resultado += caracter_mensaje

            # Agregar caracter descifrado a clave extendida
            clave_extendida += caracter_mensaje.upper()
        else:
            resultado += caracter

        # Remover primer caracter usado
        clave_extendida = clave_extendida[1:]

    return resultado
```

## Ejemplos Detallados

### Ejemplo 1: Caso Básico
```
Mensaje: "HELLO"
Clave inicial: "KEY"

Paso 1: clave_extendida = "KEY"
H(7) + K(10) = (7+10) mod 26 = 17 → R
clave_extendida = "EYH" (removido K, agregado H)

Paso 2: clave_extendida = "EYH"
E(4) + E(4) = (4+4) mod 26 = 8 → I
clave_extendida = "YHI" (removido E, agregado E)

Paso 3: clave_extendida = "YHI"
L(11) + Y(24) = (11+24) mod 26 = 35 mod 26 = 9 → J
clave_extendida = "HIJ" (removido Y, agregado L)

Paso 4: clave_extendida = "HIJ"
L(11) + H(7) = (11+7) mod 26 = 18 → S
clave_extendida = "IJS" (removido H, agregado L)

Paso 5: clave_extendida = "IJS"
O(14) + I(8) = (14+8) mod 26 = 22 → W
clave_extendida = "JSW" (removido I, agregado O)

Resultado: "RIJSW"
```

### Ejemplo 2: Texto con Espacios
```
Mensaje: "HI MOM"
Clave inicial: "CAT"

Clave extendida inicial: "CAT"

H(7) + C(2) = 9 → J, clave = "ATH"
I(8) + A(0) = 8 → I, clave = "THI"
Espacio → Espacio, clave = "THI"
M(12) + T(19) = 31 mod 26 = 5 → F, clave = "HIF"
O(14) + H(7) = 21 → V, clave = "IFV"
M(12) + I(8) = 20 → U, clave = "FVM"

Resultado: "JI FVU"
```

### Ejemplo 3: Autodescifrado
```
Mensaje original: "ABC"
Clave inicial: "K"

Cifrado:
A(0) + K(10) = 10 → K, clave = "A"
B(1) + A(0) = 1 → B, clave = "B"
C(2) + B(1) = 3 → D, clave = "C"

Resultado cifrado: "KBD"

Descifrado:
K(10) - K(10) = 0 → A, clave = "A"
B(1) - A(0) = 1 → B, clave = "B"
D(3) - B(1) = 2 → C, clave = "C"

Resultado: "ABC" ✓
```

### Ejemplo 4: Comparación con Vigenère
```
Mensaje: "ATTACKATDAWN"
Clave inicial: "LEMON"

Autokey:
A(0) + L(11) = 11 → L, clave = "EMON A"
T(19) + E(4) = 23 → X, clave = "MON AT"
T(19) + M(12) = 31 mod 26 = 5 → F, clave = "ON AT T"
A(0) + O(14) = 14 → O, clave = "N AT TA"
C(2) + N(13) = 15 → P, clave = " AT TAC"
K(10) + A(0) = 10 → K, clave = "T TAC K"
A(0) + T(19) = 19 → T, clave = " TAC KA"
T(19) + T(19) = 38 mod 26 = 12 → M, clave = "AC KA T"
D(3) + A(12) = 15 → P, clave = "C KA TD"
A(0) + C(2) = 2 → C, clave = " KA TDA"
W(22) + K(10) = 32 mod 26 = 6 → G, clave = "A TD AW"
N(13) + A(0) = 13 → N, clave = " TD AWN"

Resultado: "LXFO PKTO MTPC GN"

Vigenère (comparación):
Clave repetida: "LEMONLEMONLE"
Resultado: "LXFOPVEFRNHR"

Autokey es más seguro porque no repite el patrón "LEMON"
```

## Variantes del Autokey

### Autokey Progresivo
- La clave inicial se modifica con cada uso
- Similar a modos modernos de operación

### Autokey con Retroalimentación
- Usa el texto cifrado para generar la clave
- Más complejo pero potencialmente más seguro

### Autokey de Vigenère (Estándar)
- La variante descrita arriba
- Más común y estudiada

### Autokey de Beaufort
- Variante: C(x) = (k - x) mod 26
- Autoinversa como el Beaufort normal

### Autokey de Porta
- Usa tabla de Porta en lugar de Vigenère
- Diferentes reglas de cifrado

## Criptoanálisis (Ataques)

### Ataque por Texto Plano Conocido

**Principio**: Si se conoce parte del mensaje, se puede reconstruir la clave extendida.

**Pasos**:
1. **Conocido inicial**: Usar parte conocida del mensaje
2. **Reconstruir clave**: k'ᵢ = (cᵢ - mᵢ) mod 26
3. **Extender**: Una vez conocida la clave, descifrar el resto

### Análisis de Kasiski Modificado

**Método**: Buscar repeticiones que indiquen la clave inicial.

**Ejemplo**:
```
Texto cifrado: "ABCABC..."
Si "ABC" se repite, podría indicar clave inicial de longitud 3
```

### Ataque por Fuerza Bruta

**Complejidad**: Probar claves iniciales de diferentes longitudes
- Longitud 1: 26 posibilidades
- Longitud 2: 26² = 676
- Longitud 3: 26³ = 17,576

### Análisis de Frecuencia

**Más difícil que Vigenère**: No hay repeticiones periódicas
**Método**: Usar análisis de dígrafos y contexto lingüístico

## Análisis de Seguridad

### Fortalezas
- **Sin periodicidad**: No repite patrones como Vigenère
- **Clave única**: Cada mensaje tiene su propia clave extendida
- **Longitud ilimitada**: La clave crece con el mensaje
- **Resistente a Kasiski**: No hay repeticiones regulares

### Debilidades
- **Texto plano conocido**: Compromete todo el mensaje
- **Clave inicial**: Si se conoce, todo es vulnerable
- **Contexto lingüístico**: Ataques basados en idioma
- **No autenticado**: No detecta modificaciones

### Comparación de Seguridad

| Método | Periodicidad | Resistencia Kasiski | Seguridad Relativa |
|--------|--------------|---------------------|-------------------|
| César | Alta | Muy Baja | Muy Baja |
| Vigenère | Media | Baja | Baja |
| Autokey | Ninguna | Alta | Alta |
| One-time Pad | Ninguna | Muy Alta | Muy Alta |

## Aplicaciones Modernas

### Usos Legítimos
- **Cifrados de flujo**: Base para algoritmos como RC4
- **Generadores de clave**: En protocolos criptográficos
- **Ofuscación**: Para datos no críticos
- **Educación**: Enseñar conceptos avanzados de criptografía

### En Criptografía Moderna
- **Modo CTR**: Contadores como claves autogeneradas
- **Cifrado de flujo**: Generadores pseudoaleatorios
- **Protocolos**: TLS, SSH usan conceptos similares

## Implementación Completa

```python
from typing import List

class CifradoAutokey:
    """
    Implementación del cifrado Autokey.
    Variante del Vigenère donde la clave se autogenera del mensaje.
    """

    def __init__(self, clave_inicial: str):
        """
        Inicializa el cifrado Autokey.

        Args:
            clave_inicial: Clave semilla para iniciar el proceso
        """
        self.clave_inicial = "".join(c.upper() for c in clave_inicial if c.isalpha())
        if not self.clave_inicial:
            raise ValueError("La clave inicial debe contener al menos una letra")

    def _preparar_texto(self, texto: str) -> str:
        """Prepara el texto: mayúsculas, solo letras"""
        return "".join(c.upper() for c in texto if c.isalpha())

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Autokey.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado
        """
        texto_limpio = self._preparar_texto(texto_plano)
        if not texto_limpio:
            return ""

        resultado = ""
        clave_extendida = list(self.clave_inicial)

        for caracter in texto_limpio:
            # Usar primer caracter de clave extendida
            indice_clave = ord(clave_extendida[0]) - ord('A')
            indice_mensaje = ord(caracter) - ord('A')

            # Cifrar
            indice_cifrado = (indice_mensaje + indice_clave) % 26
            caracter_cifrado = chr(indice_cifrado + ord('A'))

            resultado += caracter_cifrado

            # Agregar caracter original a clave extendida
            clave_extendida.append(caracter)

            # Remover primer caracter usado
            clave_extendida.pop(0)

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Autokey.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado
        """
        texto_limpio = self._preparar_texto(texto_cifrado)
        if not texto_limpio:
            return ""

        resultado = ""
        clave_extendida = list(self.clave_inicial)

        for caracter in texto_limpio:
            # Usar primer caracter de clave extendida
            indice_clave = ord(clave_extendida[0]) - ord('A')
            indice_cifrado = ord(caracter) - ord('A')

            # Descifrar
            indice_mensaje = (indice_cifrado - indice_clave) % 26
            caracter_mensaje = chr(indice_mensaje + ord('A'))

            resultado += caracter_mensaje

            # Agregar caracter descifrado a clave extendida
            clave_extendida.append(caracter_mensaje)

            # Remover primer caracter usado
            clave_extendida.pop(0)

        return resultado

    def analizar_longitud_clave(self, texto_cifrado: str, max_longitud: int = 10) -> dict:
        """
        Intenta estimar la longitud de la clave inicial usando análisis de frecuencia.

        Args:
            texto_cifrado: Texto cifrado a analizar
            max_longitud: Longitud máxima de clave a probar

        Returns:
            Diccionario con puntuaciones para cada longitud
        """
        texto_limpio = self._preparar_texto(texto_cifrado)
        puntuaciones = {}

        for longitud in range(1, min(max_longitud + 1, len(texto_limpio))):
            # Dividir en grupos
            grupos = ["" for _ in range(longitud)]
            for i, c in enumerate(texto_limpio):
                grupos[i % longitud] += c

            # Calcular score promedio (frecuencia de ETAOIN)
            score_total = 0
            letras_comunes = "ETAOINSHRDLUCMFYWGPBVKXQJZ"

            for grupo in grupos:
                if len(grupo) > 0:
                    frecuencias = {}
                    for c in grupo:
                        frecuencias[c] = frecuencias.get(c, 0) + 1

                    # Score basado en letras comunes al inicio
                    score_grupo = 0
                    for i, letra in enumerate(letras_comunes[:6]):  # ETAOIN
                        if letra in frecuencias:
                            score_grupo += frecuencias[letra] * (6 - i)
                    score_total += score_grupo / len(grupo)

            puntuaciones[longitud] = score_total / longitud

        return puntuaciones

# Funciones de conveniencia
def cifrar_autokey(texto: str, clave_inicial: str) -> str:
    """Función de conveniencia para cifrar con Autokey"""
    autokey = CifradoAutokey(clave_inicial)
    return autokey.cifrar(texto)

def descifrar_autokey(texto: str, clave_inicial: str) -> str:
    """Función de conveniencia para descifrar con Autokey"""
    autokey = CifradoAutokey(clave_inicial)
    return autokey.descifrar(texto)

# Ejemplo de uso
if __name__ == "__main__":
    clave_inicial = "KEY"
    mensaje = "HELLO WORLD"

    print(f"Clave inicial: {clave_inicial}")
    print(f"Mensaje: {mensaje}")

    # Cifrado
    cifrado = cifrar_autokey(mensaje, clave_inicial)
    print(f"Texto cifrado: {cifrado}")

    # Descifrado
    descifrado = descifrar_autokey(cifrado, clave_inicial)
    print(f"Texto descifrado: {descifrado}")

    # Verificar
    mensaje_limpio = "".join(c.upper() for c in mensaje if c.isalpha())
    descifrado_limpio = "".join(c.upper() for c in descifrado if c.isalpha())
    print(f"¿Correcto? {mensaje_limpio == descifrado_limpio}")

    # Comparación con Vigenère
    print("\n--- Comparación con Vigenère ---")
    from cifrado_vigenere import cifrar_vigenere, descifrar_vigenere

    vigenere_cifrado = cifrar_vigenere(mensaje, clave_inicial)
    print(f"Vigenère cifrado: {vigenere_cifrado}")

    autokey_cifrado = cifrar_autokey(mensaje, clave_inicial)
    print(f"Autokey cifrado:  {autokey_cifrado}")

    print(f"¿Diferentes? {vigenere_cifrado != autokey_cifrado}")

    # Análisis de longitud de clave
    print("\n--- Análisis de longitud de clave ---")
    autokey = CifradoAutokey("dummy")
    analisis = autokey.analizar_longitud_clave(cifrado, 5)

    for longitud, score in analisis.items():
        print(".3f")
```

## Conclusión

El cifrado Autokey representa una **evolución significativa** del Vigenère al eliminar su mayor debilidad: la repetición periódica de la clave. Al autogenerar la clave a partir del mensaje mismo, crea un sistema más dinámico y seguro.

**Contribuciones clave**:
- **Eliminación de periodicidad**: No hay repeticiones predecibles
- **Claves únicas**: Cada mensaje tiene su propia secuencia de clave
- **Transición conceptual**: De claves estáticas a dinámicas
- **Base moderna**: Influencia en cifrados de flujo contemporáneos

Aunque vulnerable a ataques de texto plano conocido, el Autokey demostró que era posible mejorar significativamente la seguridad de los cifrados polialfabéticos mediante la autogeneración de claves, un concepto fundamental en la criptografía moderna.