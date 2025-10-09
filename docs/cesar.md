# Cifrado César

## Descripción General

El **cifrado César** (también conocido como **cifrado por desplazamiento**) es uno de los métodos de cifrado más antiguos y simples de la historia de la criptografía. Recibe su nombre en honor a Julio César, quien lo utilizaba para comunicaciones militares secretas alrededor del año 50 a.C.

Este cifrado pertenece a la categoría de **cifrados monoalfabéticos** o **por sustitución simple**, donde cada letra del alfabeto se reemplaza sistemáticamente por otra letra fija.

## Historia y Contexto

### Origen Histórico
- **Siglo I a.C.**: Julio César lo usaba con un desplazamiento de 3 posiciones
- **Siglo IX**: Descrito por el criptógrafo árabe Al-Kindi
- **Edad Media**: Conocido como "cifrado de César" en textos europeos
- **Siglo XX**: Todavía usado en juegos y rompecabezas infantiles

### Usos Históricos
- **Comunicaciones militares romanas**: César enviaba órdenes secretas a sus generales
- **Comunicaciones diplomáticas**: Durante la Edad Media
- **Juegos y pasatiempos**: Aparece en libros infantiles y crucigramas
- **ROT13**: Variante moderna usada en foros de internet (desplazamiento de 13)

## Lógica Matemática

### Definición Formal

Sea Σ un alfabeto finito de tamaño |Σ| = n. Un cifrado César con desplazamiento d ∈ ℤ se define como:

**Cifrado**: C(x) = (x + d) mod n
**Descifrado**: D(y) = (y - d) mod n

Donde:
- x es la posición de la letra original (0 ≤ x < n)
- y es la posición de la letra cifrada (0 ≤ y < n)
- d es el desplazamiento (0 ≤ d < n)

### Propiedades Matemáticas

1. **Bijectividad**: Es una función biyectiva (invertible)
2. **Grupo Cíclico**: Forma un grupo cíclico de orden n
3. **Composición**: C_d₁ ∘ C_d₂ = C_(d₁+d₂) mod n
4. **Inverso**: C_d⁻¹ = C_(n-d)

### Ejemplo Matemático

Alfabeto: A=0, B=1, C=2, ..., Z=25
Desplazamiento: d=3

```
Texto:  H E L L O   W O R L D
Posic:  7 4 11 11 14 22 14 17 11 3
Cifrado: (7+3)=10, (4+3)=7, (11+3)=14, (11+3)=14, (14+3)=17, (22+3)=25, (14+3)=17, (17+3)=20, (11+3)=14, (3+3)=6
Resultado: K H O O R   Z R U O G
```

## Algoritmo Detallado

### Cifrado
```python
def cifrar_cesar(texto, desplazamiento, alfabeto):
    resultado = ""
    n = alfabeto.obtener_longitud()

    for caracter in texto:
        if alfabeto.contiene_caracter(caracter):
            indice_original = alfabeto.obtener_indice(caracter)
            indice_cifrado = (indice_original + desplazamiento) % n
            caracter_cifrado = alfabeto.obtener_caracter(indice_cifrado)
            resultado += caracter_cifrado
        else:
            resultado += caracter  # Mantener caracteres no alfabéticos

    return resultado
```

### Descifrado
```python
def descifrar_cesar(texto_cifrado, desplazamiento, alfabeto):
    return cifrar_cesar(texto_cifrado, -desplazamiento, alfabeto)
```

### Ataque de Fuerza Bruta
```python
def ataque_fuerza_bruta(texto_cifrado, alfabeto):
    n = alfabeto.obtener_longitud()
    resultados = []

    for d in range(1, n):  # d=0 no cambia nada
        candidato = descifrar_cesar(texto_cifrado, d, alfabeto)
        resultados.append(f"Desplazamiento {d}: {candidato}")

    return resultados
```

## Ejemplos Prácticos

### Ejemplo 1: Desplazamiento 3 (Tradicional)
```
Mensaje:     HOLA MUNDO
Desplazamiento: 3
Cifrado:     KROD PXQGR
```

**Proceso paso a paso:**
- H(7) → K(10): (7+3) mod 26 = 10
- O(14) → R(17): (14+3) mod 26 = 17
- L(11) → O(14): (11+3) mod 26 = 14
- A(0) → D(3): (0+3) mod 26 = 3
- Espacio → Espacio (sin cambios)
- M(12) → P(15): (12+3) mod 26 = 15
- U(20) → X(23): (20+3) mod 26 = 23
- N(13) → Q(16): (13+3) mod 26 = 16
- D(3) → G(6): (3+3) mod 26 = 6
- O(14) → R(17): (14+3) mod 26 = 17

### Ejemplo 2: Desplazamiento 13 (ROT13)
```
Mensaje:     HOLA
Desplazamiento: 13
Cifrado:     UBYL
```

**Proceso:**
- H(7) → U(20): (7+13) mod 26 = 20
- O(14) → B(1): (14+13) mod 26 = 27 mod 26 = 1
- L(11) → Y(24): (11+13) mod 26 = 24
- A(0) → N(13): (0+13) mod 26 = 13

### Ejemplo 3: Desplazamiento Negativo
```
Mensaje:     ABC
Desplazamiento: -5
Cifrado:     VWX
```

**Proceso:**
- A(0) → V(21): (0-5) mod 26 = 21
- B(1) → W(22): (1-5) mod 26 = 22
- C(2) → X(23): (2-5) mod 26 = 23

### Ejemplo 4: Con Caracteres Especiales
```
Mensaje:     HOLA, MUNDO!
Desplazamiento: 3
Cifrado:     KROD, PXQGR!
```

Los caracteres de puntuación y espacios se mantienen sin cambios.

## Variantes y Extensiones

### ROT13
- Desplazamiento fijo de 13
- Autoinverso: aplicar dos veces regresa al original
- Usado en foros de internet para ocultar spoilers

### Cifrados Afines
- Generalización: C(x) = (ax + b) mod n
- César es un caso especial con a=1

### Cifrados por Sustitución
- Cada letra se reemplaza por cualquier otra letra
- No sigue un patrón matemático simple

## Análisis de Seguridad

### Vulnerabilidades

1. **Espacio de Claves Pequeño**
   - Solo 25 desplazamientos posibles (excluyendo 0)
   - Ataque de fuerza bruta trivial

2. **Preserva Frecuencias**
   - La frecuencia de letras se mantiene
   - Análisis estadístico revela el patrón

3. **Patrones Estructurales**
   - Mantiene la estructura del lenguaje
   - Palabras comunes son reconocibles

### Ataques Posibles

#### 1. Ataque de Fuerza Bruta
```python
# Probar todos los desplazamientos posibles
for d in range(1, 26):
    candidato = descifrar_cesar(texto_cifrado, d)
    if es_texto_legible(candidato):
        print(f"Posible mensaje: {candidato} (desplazamiento {d})")
```

#### 2. Análisis de Frecuencia
- La letra más frecuente en inglés es 'E'
- En el texto cifrado, encontrar la letra más frecuente
- Calcular el desplazamiento necesario para mapearla a 'E'

#### 3. Ataque por Conocimiento
- Si se conoce parte del mensaje original
- Calcular el desplazamiento y aplicar al resto

### Medidas de Seguridad
- **No usar solo**: Combinar con otros cifrados
- **Cambiar desplazamiento**: Usar diferentes desplazamientos
- **Aumentar alfabeto**: Usar alfabeto extendido

## Comparación con Otros Cifrados

| Cifrado | Complejidad | Seguridad | Velocidad |
|---------|-------------|-----------|-----------|
| César | Muy Baja | Muy Baja | Muy Alta |
| Vigenère | Media | Media | Alta |
| Hill | Alta | Alta | Media |
| AES | Muy Alta | Muy Alta | Alta |

## Casos de Uso Modernos

### Educativos
- Enseñanza de conceptos básicos de criptografía
- Ejercicios en cursos de seguridad informática

### Juegos y Entretenimiento
- Crucigramas y rompecabezas
- Novelas y películas (para representar "códigos secretos")

### Sistemas Legacy
- Algunos sistemas antiguos todavía usan variantes
- Compatibilidad con protocolos históricos

## Implementación Completa

```python
import string
from typing import List

class Alfabeto:
    def __init__(self, case_sensitive: bool = True):
        if case_sensitive:
            self.alfabeto = string.ascii_uppercase  # A-Z
        else:
            self.alfabeto = string.ascii_uppercase + string.ascii_lowercase

    def obtener_longitud(self) -> int:
        return len(self.alfabeto)

    def obtener_indice(self, caracter: str) -> int:
        try:
            return self.alfabeto.index(caracter)
        except ValueError:
            return -1

    def obtener_caracter(self, indice: int) -> str:
        if 0 <= indice < len(self.alfabeto):
            return self.alfabeto[indice]
        raise IndexError("Índice fuera de rango")

    def contiene_caracter(self, caracter: str) -> bool:
        return caracter in self.alfabeto

class CifradoCesar:
    def __init__(self, desplazamiento: int = 3, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.desplazamiento = desplazamiento % self.alfabeto.obtener_longitud()

    def cifrar(self, texto_plano: str) -> str:
        resultado = ""
        for c in texto_plano:
            indice = self.alfabeto.obtener_indice(c)
            if indice != -1:
                nuevo_indice = (indice + self.desplazamiento) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        desplazamiento_inverso = self.alfabeto.obtener_longitud() - self.desplazamiento
        cesar_inverso = CifradoCesar(desplazamiento_inverso, self.alfabeto)
        return cesar_inverso.cifrar(texto_cifrado)

    def ataque_fuerza_bruta(self, texto_cifrado: str) -> List[str]:
        resultados = []
        n = self.alfabeto.obtener_longitud()
        for d in range(1, n):
            candidato = CifradoCesar(d, self.alfabeto).descifrar(texto_cifrado)
            resultados.append(candidato)
        return resultados

# Funciones de conveniencia
def cifrar_cesar(texto: str, desplazamiento: int = 3, alfabeto: Alfabeto = None) -> str:
    cesar = CifradoCesar(desplazamiento, alfabeto)
    return cesar.cifrar(texto)

def descifrar_cesar(texto_cifrado: str, desplazamiento: int = 3, alfabeto: Alfabeto = None) -> str:
    cesar = CifradoCesar(desplazamiento, alfabeto)
    return cesar.descifrar(texto_cifrado)

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = "VENI VIDI VICI"
    desplazamiento = 3

    # Cifrado
    cifrado = cifrar_cesar(mensaje, desplazamiento)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")

    # Descifrado
    descifrado = descifrar_cesar(cifrado, desplazamiento)
    print(f"Descifrado: {descifrado}")

    # Ataque de fuerza bruta
    print("\nAtaque de fuerza bruta:")
    ataque = CifradoCesar().ataque_fuerza_bruta(cifrado)
    for i, candidato in enumerate(ataque[:5]):
        print(f"Desplazamiento {i+1}: {candidato}")
```

## Conclusión

El cifrado César representa los fundamentos de la criptografía moderna. Aunque es extremadamente inseguro para uso práctico, es invaluable para:

- **Comprender conceptos básicos** de cifrado por sustitución
- **Enseñar principios matemáticos** de la criptografía
- **Ilustrar vulnerabilidades** de sistemas aparentemente seguros
- **Servir como base** para cifrados más complejos

Su simplicidad lo hace perfecto para fines educativos, mientras que su debilidad demuestra por qué la criptografía moderna requiere algoritmos mucho más sofisticados.