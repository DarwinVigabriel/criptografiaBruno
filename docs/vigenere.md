# Cifrado Vigenère

## Descripción General

El **cifrado Vigenère** es un método de cifrado polialfabético inventado por Giovan Battista Bellaso en 1553, pero popularizado por Blaise de Vigenère en el siglo XVI. Es considerado el primer cifrado polialfabético práctico y fue considerado "indescifrable" durante casi 300 años.

A diferencia del cifrado César (monoalfabético), Vigenère usa **múltiples alfabetos** determinados por una palabra clave, lo que rompe los patrones de frecuencia característicos de los cifrados simples.

## Historia y Contexto

### Origen y Desarrollo
- **1553**: Giovan Battista Bellaso publica "La Cifra del Sig. Giovan Battista Bellaso"
- **1586**: Blaise de Vigenère describe el método en "Traicté des Chiffres"
- **Siglo XIX**: Charles Babbage rompe el cifrado (pero mantiene secreto)
- **1917**: William F. Friedman redescubre el método de ataque

### Importancia Histórica
- **"Indescifrable"**: Considerado unbreakable durante siglos
- **Código Beale**: Usó una variante del Vigenère
- **Guerra Civil Americana**: Usado por confederados
- **Primera Guerra Mundial**: Método principal de cifrado diplomático

### Terminología
- **Polialfabético**: Usa múltiples alfabetos de sustitución
- **Autoclave**: Variante donde la clave se genera del mensaje mismo
- **Tabla de Vigenère**: Matriz que muestra todas las posibles sustituciones

## Lógica Matemática

### Definición Formal

Sea Σ un alfabeto de tamaño n. Una clave K = k₁k₂...kₘ determina una secuencia periódica:

**Cifrado**: Cᵢ(x) = (x + kᵢ) mod n
**Descifrado**: Dᵢ(y) = (y - kᵢ) mod n

Donde:
- x es la letra del mensaje (posición en alfabeto)
- kᵢ es la letra correspondiente de la clave extendida
- i es la posición en el mensaje

### Tabla de Vigenère

La tabla clásica para alfabeto A-Z:

```
   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
A  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B  B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C  C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
...
Z  Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

Cada fila representa un desplazamiento César diferente.

### Propiedades Matemáticas

1. **Periodicidad**: La clave se repite periódicamente
2. **Linealidad**: Cada posición usa un César independiente
3. **Simetría**: El descifrado usa desplazamientos negativos

## Algoritmo Detallado

### Preparación de la Clave
```python
def preparar_clave(mensaje, clave):
    # Limpiar clave (solo letras mayúsculas)
    clave_limpia = "".join(c.upper() for c in clave if c.isalpha())

    # Extender clave para cubrir el mensaje
    clave_extendida = ""
    indice_clave = 0

    for caracter in mensaje:
        if caracter.isalpha():
            clave_extendida += clave_limpia[indice_clave % len(clave_limpia)]
            indice_clave += 1

    return clave_extendida
```

### Cifrado
```python
def cifrar_vigenere(mensaje, clave):
    resultado = ""
    clave_extendida = preparar_clave(mensaje, clave)
    indice_clave = 0

    for i, caracter in enumerate(mensaje):
        if caracter.isalpha():
            # Convertir a índices (A=0, B=1, ..., Z=25)
            indice_mensaje = ord(caracter.upper()) - ord('A')
            indice_clave_actual = ord(clave_extendida[indice_clave]) - ord('A')

            # Aplicar cifrado: (mensaje + clave) mod 26
            indice_cifrado = (indice_mensaje + indice_clave_actual) % 26

            # Convertir de vuelta a letra
            letra_cifrada = chr(indice_cifrado + ord('A'))

            # Mantener caso original
            if caracter.islower():
                letra_cifrada = letra_cifrada.lower()

            resultado += letra_cifrada
            indice_clave += 1
        else:
            resultado += caracter  # Mantener no-letras

    return resultado
```

### Descifrado
```python
def descifrar_vigenere(mensaje_cifrado, clave):
    resultado = ""
    clave_extendida = preparar_clave(mensaje_cifrado, clave)
    indice_clave = 0

    for i, caracter in enumerate(mensaje_cifrado):
        if caracter.isalpha():
            # Convertir a índices
            indice_cifrado = ord(caracter.upper()) - ord('A')
            indice_clave_actual = ord(clave_extendida[indice_clave]) - ord('A')

            # Aplicar descifrado: (cifrado - clave) mod 26
            indice_mensaje = (indice_cifrado - indice_clave_actual) % 26

            # Convertir de vuelta a letra
            letra_mensaje = chr(indice_mensaje + ord('A'))

            # Mantener caso original
            if caracter.islower():
                letra_mensaje = letra_mensaje.lower()

            resultado += letra_mensaje
            indice_clave += 1
        else:
            resultado += caracter  # Mantener no-letras

    return resultado
```

## Ejemplos Detallados

### Ejemplo 1: Caso Básico
```
Mensaje:     A T A Q U E
Clave:       L I M A
Clave extendida: L I M A L I

Proceso:
A(0) + L(11) = (0+11) mod 26 = 11 → L
T(19) + I(8) = (19+8) mod 26 = 27 mod 26 = 1 → B
A(0) + M(12) = (0+12) mod 26 = 12 → M
Q(16) + A(0) = (16+0) mod 26 = 16 → Q
U(20) + L(11) = (20+11) mod 26 = 31 mod 26 = 5 → F
E(4) + I(8) = (4+8) mod 26 = 12 → M

Resultado: L B M Q F M
```

### Ejemplo 2: Con Espacios y Puntuación
```
Mensaje:     "HELLO, WORLD!"
Clave:       "KEY"
Clave extendida: K E Y K E Y K E Y K

Proceso (ignorando no-letras):
H(7) + K(10) = (7+10) mod 26 = 17 → R
E(4) + E(4) = (4+4) mod 26 = 8 → I
L(11) + Y(24) = (11+24) mod 26 = 35 mod 26 = 9 → J
L(11) + K(10) = (11+10) mod 26 = 21 → V
O(14) + E(4) = (14+4) mod 26 = 18 → S
W(22) + Y(24) = (22+24) mod 26 = 46 mod 26 = 20 → U
O(14) + K(10) = (14+10) mod 26 = 24 → Y
R(17) + E(4) = (17+4) mod 26 = 21 → V
L(11) + Y(24) = (11+24) mod 26 = 35 mod 26 = 9 → J
D(3) + K(10) = (3+10) mod 26 = 13 → N

Resultado: "RIJV, SUYVJN!"
```

### Ejemplo 3: Autodescifrado (ROT13 como caso especial)
```
Mensaje:     "HELLO"
Clave:       "N" (13 posiciones desde A)
Resultado:   "URYYB"
```

### Ejemplo 4: Clave más larga que mensaje
```
Mensaje:     "HI"
Clave:       "VERYLONGKEY"
Clave usada: "VE"

H(7) + V(21) = (7+21) mod 26 = 28 mod 26 = 2 → C
I(8) + E(4) = (8+4) mod 26 = 12 → M

Resultado: "CM"
```

## Criptoanálisis (Ataques)

### Método de Kasiski (1863)

**Principio**: Las repeticiones en el texto cifrado revelan la longitud de la clave.

**Pasos**:
1. **Encontrar repeticiones**: Buscar secuencias idénticas en el texto cifrado
2. **Medir distancias**: Calcular distancias entre repeticiones
3. **Factorizar**: Encontrar factores comunes de las distancias
4. **Probar longitudes**: La longitud de clave más probable es el MCD de las distancias

**Ejemplo**:
```
Texto cifrado: "KRYPTOSKRYPTOSKRYP..."
Repeticiones encontradas:
- "KRYPTOS" en posiciones 1, 8, 15
- Distancias: 7, 7
- MCD(7,7) = 7 → Longitud de clave = 7
```

### Índice de Coincidencia (IC)

**Fórmula**: IC = Σ(fᵢ(fᵢ-1)) / (N(N-1))

Donde:
- fᵢ = frecuencia de la letra i
- N = longitud del texto

**Propiedad**:
- Texto inglés normal: IC ≈ 0.065-0.070
- Texto cifrado monoalfabético: IC ≈ 0.065-0.070
- Texto cifrado polialfabético: IC ≈ 0.038 (más bajo)

**Uso**: Para confirmar longitud de clave encontrada por Kasiski.

### Análisis de Frecuencia por Grupos

Una vez conocida la longitud m de la clave:

1. **Dividir en m grupos**: Cada grupo usa el mismo desplazamiento César
2. **Análisis de frecuencia**: Cada grupo se comporta como un César independiente
3. **Resolver cada grupo**: Usar análisis de frecuencia estándar

## Variantes y Extensiones

### Autokey Vigenère
- La clave se extiende usando el mensaje mismo
- Mayor seguridad que el Vigenère estándar
- Más resistente a ataques de frecuencia

### Vigenère Progresivo
- La clave cambia con cada uso
- Similar al modo CTR en criptografía moderna

### Cifrado de Beaufort
- Variante: C(x) = (k - x) mod n
- Autoinverso: mismo algoritmo para cifrar y descifrar

### Cifrado de Gronsfeld
- Usa dígitos numéricos como clave
- Más fácil de recordar que letras

## Análisis de Seguridad

### Fortalezas
- **Rompe patrones de frecuencia**: Cada letra puede cifrarse de múltiples formas
- **Período variable**: La clave puede ser arbitrariamente larga
- **Simple de implementar**: Fácil de usar manualmente

### Debilidades
- **Vulnerable a Kasiski**: Si la clave se repite
- **Análisis de frecuencia por grupos**: Una vez conocida la longitud
- **Clave reutilizada**: Compromete toda la seguridad

### Comparación de Seguridad

| Método | Resistencia a Kasiski | Resistencia a IC | Facilidad de Uso |
|--------|----------------------|------------------|------------------|
| César | Muy Baja | Muy Baja | Muy Alta |
| Vigenère | Media | Media-Alta | Alta |
| Autokey | Alta | Alta | Media |
| One-time Pad | Muy Alta | Muy Alta | Baja |

## Implementación Completa

```python
class CifradoVigenere:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto(case_sensitive=True)
        self.clave = "".join(c.upper() for c in clave if c.isalpha())
        if not self.clave:
            raise ValueError("La clave debe contener al menos una letra")

    def _preparar_clave(self, mensaje: str) -> str:
        """Prepara la clave extendida para el mensaje"""
        clave_extendida = ""
        indice_clave = 0

        for caracter in mensaje:
            if self.alfabeto.contiene_caracter(caracter):
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1

        return clave_extendida

    def cifrar(self, mensaje: str) -> str:
        """Cifra un mensaje usando Vigenère"""
        clave_extendida = self._preparar_clave(mensaje)
        resultado = ""
        indice_clave = 0

        for caracter in mensaje:
            if self.alfabeto.contiene_caracter(caracter):
                indice_mensaje = self.alfabeto.obtener_indice(caracter)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])

                indice_cifrado = (indice_mensaje + indice_clave_actual) % self.alfabeto.obtener_longitud()
                caracter_cifrado = self.alfabeto.obtener_caracter(indice_cifrado)

                resultado += caracter_cifrado
                indice_clave += 1
            else:
                resultado += caracter

        return resultado

    def descifrar(self, mensaje_cifrado: str) -> str:
        """Descifra un mensaje cifrado con Vigenère"""
        clave_extendida = self._preparar_clave(mensaje_cifrado)
        resultado = ""
        indice_clave = 0

        for caracter in mensaje_cifrado:
            if self.alfabeto.contiene_caracter(caracter):
                indice_cifrado = self.alfabeto.obtener_indice(caracter)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])

                indice_mensaje = (indice_cifrado - indice_clave_actual) % self.alfabeto.obtener_longitud()
                caracter_mensaje = self.alfabeto.obtener_caracter(indice_mensaje)

                resultado += caracter_mensaje
                indice_clave += 1
            else:
                resultado += caracter

        return resultado

    def analizar_longitud_clave(self, texto_cifrado: str, max_longitud: int = 20) -> dict:
        """
        Intenta determinar la longitud de la clave usando el índice de coincidencia
        """
        resultados = {}

        for longitud in range(1, max_longitud + 1):
            grupos = ["" for _ in range(longitud)]

            # Dividir en grupos
            for i, caracter in enumerate(texto_cifrado):
                if caracter.isalpha():
                    grupos[i % longitud] += caracter

            # Calcular IC promedio
            ic_promedio = 0
            for grupo in grupos:
                if len(grupo) > 1:
                    frecuencias = {}
                    for c in grupo:
                        frecuencias[c] = frecuencias.get(c, 0) + 1

                    ic_grupo = sum(f * (f - 1) for f in frecuencias.values()) / (len(grupo) * (len(grupo) - 1))
                    ic_promedio += ic_grupo

            ic_promedio /= longitud
            resultados[longitud] = ic_promedio

        return resultados

# Funciones de conveniencia
def cifrar_vigenere(mensaje: str, clave: str) -> str:
    vigenere = CifradoVigenere(clave)
    return vigenere.cifrar(mensaje)

def descifrar_vigenere(mensaje_cifrado: str, clave: str) -> str:
    vigenere = CifradoVigenere(clave)
    return vigenere.descifrar(mensaje_cifrado)

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = "ATTACKATDAWN"
    clave = "LEMON"

    print(f"Mensaje original: {mensaje}")
    print(f"Clave: {clave}")

    # Cifrado
    cifrado = cifrar_vigenere(mensaje, clave)
    print(f"Texto cifrado: {cifrado}")

    # Descifrado
    descifrado = descifrar_vigenere(cifrado, clave)
    print(f"Texto descifrado: {descifrado}")

    # Análisis de longitud de clave
    print("\nAnálisis de longitud de clave:")
    vigenere = CifradoVigenere("dummy")
    analisis = vigenere.analizar_longitud_clave(cifrado, 10)

    for longitud, ic in analisis.items():
        print(".4f")
```

## Conclusión

El cifrado Vigenère representa un avance significativo en la criptografía, introduciendo el concepto de **cifrados polialfabéticos**. Aunque ya no se considera seguro para uso moderno, sentó las bases para:

- **Desarrollo de cifrados polialfabéticos modernos**
- **Técnicas de criptoanálisis avanzadas**
- **Comprensión de la importancia de claves largas y aleatorias**
- **Fundamentos del one-time pad** (caso límite perfecto)

Su estudio es esencial para entender la evolución de la criptografía desde métodos manuales hasta algoritmos computacionales modernos.