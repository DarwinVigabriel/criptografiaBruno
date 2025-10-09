# Utilidades - Funciones de Soporte para Criptografía

## Descripción General

El módulo `utilidades.py` es el **corazón** del sistema criptográfico, proporcionando funciones y clases auxiliares esenciales para todos los cifrados clásicos. Incluye manejo avanzado de alfabetos, operaciones matemáticas modulares, análisis estadístico de frecuencias, validación de datos, y algoritmos de soporte para transposiciones.

Este módulo actúa como **capa de abstracción** que permite a los cifrados enfocarse en su lógica específica mientras delegan operaciones comunes a funciones reutilizables y probadas.

## Arquitectura y Diseño

### Principios de Diseño
- **Modularidad**: Funciones independientes y reutilizables
- **Abstracción**: Oculta complejidad matemática y algorítmica
- **Consistencia**: Manejo uniforme de textos y alfabetos
- **Extensibilidad**: Fácil adición de nuevos alfabetos y operaciones
- **Robustez**: Validación exhaustiva de entradas

### Dependencias y Relaciones
- **Base para todos los cifrados**: Cada algoritmo usa al menos una utilidad
- **Interdependencia controlada**: Funciones se llaman entre sí de forma jerárquica
- **Alfabeto como núcleo**: La clase `Alfabeto` es fundamental para todo el sistema

## Clase Alfabeto - Núcleo del Sistema

### Descripción Arquitectural
La clase `Alfabeto` es una **abstracción fundamental** que encapsula la lógica de manejo de caracteres válidos, proporcionando una interfaz unificada para diferentes configuraciones alfabéticas.

#### Características Técnicas
- **Configurable**: Soporta alfabetos personalizados
- **Case Management**: Control preciso de mayúsculas/minúsculas
- **Unicode Support**: Compatible con caracteres extendidos
- **Validation**: Verificación automática de integridad

### Constructor Detallado
```python
def __init__(self, alfabeto_personalizado: Optional[str] = None, case_sensitive: bool = False)
```

#### Parámetros Avanzados
- `alfabeto_personalizado`: String con caracteres personalizados
  - `None`: Usa alfabeto inglés A-Z (mayúsculas)
  - String vacío: Alfabeto vacío (solo validación)
  - String personalizado: Caracteres específicos en orden deseado

- `case_sensitive`: Control de distinción de mayúsculas
  - `False` (default): Convierte todo a mayúsculas
  - `True`: Preserva case, trata mayúsculas y minúsculas como diferentes

#### Ejemplos de Configuración

**Alfabeto Inglés Estándar**
```python
alfabeto_ingles = Alfabeto()  # A-Z, case insensitive
```

**Alfabeto Español con Ñ**
```python
alfabeto_espanol = Alfabeto("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
```

**Alfabeto Binario**
```python
alfabeto_binario = Alfabeto("01")
```

**Alfabeto Case-Sensitive**
```python
alfabeto_cs = Alfabeto(case_sensitive=True)  # A-Z a-z tratados como diferentes
```

### Métodos Principales - API Completa

#### `obtener_longitud() -> int`
**Propósito**: Obtener tamaño del alfabeto
**Complejidad**: O(1)
**Uso**: Dimensionamiento de matrices, validación de claves

```python
alfabeto = Alfabeto()
longitud = alfabeto.obtener_longitud()  # 26 para inglés
```

#### `obtener_indice(caracter: str) -> int`
**Propósito**: Mapear carácter a posición numérica
**Algoritmo**: Búsqueda lineal en string interno
**Retorno**: Índice 0-based o -1 si no encontrado
**Casos especiales**: Case-insensitive por defecto

```python
alfabeto = Alfabeto()
print(alfabeto.obtener_indice('A'))  # 0
print(alfabeto.obtener_indice('a'))  # 0 (case insensitive)
print(alfabeto.obtener_indice('1'))  # -1 (no encontrado)
```

#### `obtener_caracter(indice: int) -> str`
**Propósito**: Mapear posición numérica a carácter
**Validación**: Verifica rango válido
**Excepciones**: IndexError para índices fuera de rango

```python
alfabeto = Alfabeto()
print(alfabeto.obtener_caracter(0))   # 'A'
print(alfabeto.obtener_caracter(25))  # 'Z'
# alfabeto.obtener_caracter(26)  # IndexError
```

#### `contiene_caracter(caracter: str) -> bool`
**Propósito**: Verificar membresía en alfabeto
**Optimización**: Usa búsqueda eficiente
**Uso**: Filtrado y validación de texto

#### `normalizar_texto(texto: str) -> str`
**Propósito**: Convertir texto al formato del alfabeto
**Operaciones**:
- Conversión de case según configuración
- Filtrado de caracteres inválidos
- Preservación de estructura básica

#### `filtrar_texto(texto: str) -> str`
**Propósito**: Eliminar caracteres no alfabéticos
**Diferencia con normalizar**: Solo elimina, no transforma

## Funciones Matemáticas - Soporte Algebraico

### Teoría Matemática Subyacente

#### Aritmética Modular
Los cifrados clásicos (César, Vigenère, Hill) usan aritmética modular para:
- **Ciclicidad**: Operaciones que "envuelven" alrededor del alfabeto
- **Inversibilidad**: Garantizar que cada operación tiene inversa
- **Consistencia**: Propiedades algebraicas preservadas

#### Algoritmo de Euclides
Base para cálculo de MCD e inversos modulares:
- **MCD**: Máximo común divisor
- **Inverso modular**: x tal que (a × x) ≡ 1 mod m

### `calcular_mcd(a: int, b: int) -> int`
**Algoritmo**: Euclides recursivo
**Propósito**: Encontrar divisor común máximo
**Aplicaciones**: Validación de claves en Hill, análisis de coprimos

```python
def calcular_mcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return calcular_mcd(b, a % b)
```

**Ejemplos detallados**:
```python
print(calcular_mcd(48, 18))   # 6: 48÷6=8, 18÷6=3
print(calcular_mcd(100, 75))  # 25: 100÷25=4, 75÷25=3
print(calcular_mcd(17, 23))   # 1: números coprimos
```

### `calcular_inverso_modular(a: int, m: int) -> int`
**Algoritmo**: Euclides extendido
**Requisitos**: a y m deben ser coprimos (MCD(a,m) = 1)
**Excepciones**: ValueError si no existe inverso
**Aplicaciones**: Descifrado Hill, operaciones modulares inversas

```python
def calcular_inverso_modular(a: int, m: int) -> int:
    # Implementación usando algoritmo extendido de Euclides
    # Retorna x tal que (a * x) % m == 1
    pass
```

**Ejemplos**:
```python
# Para alfabeto de 26 letras
print(calcular_inverso_modular(7, 26))   # 15: 7×15 = 105 ≡ 1 mod 26
print(calcular_inverso_modular(3, 26))   # 9: 3×9 = 27 ≡ 1 mod 26

# Caso sin inverso
# calcular_inverso_modular(4, 26)  # ValueError: MCD(4,26)=2 ≠ 1
```

## Análisis Estadístico - Criptoanálisis

### Teoría de la Información
El análisis de frecuencia es fundamental en criptografía porque:
- **Redundancia del lenguaje**: Los idiomas tienen patrones predecibles
- **Ataque estadístico**: Comparar frecuencias del cifrado con el idioma esperado
- **Quebrar cifrados**: Sustitución simple vulnerable a análisis de frecuencia

### `analizar_frecuencia(texto: str) -> Dict[str, int]`
**Propósito**: Contar ocurrencias de cada carácter
**Retorno**: Diccionario carácter → frecuencia
**Case sensitivity**: Respeta configuración del alfabeto

```python
def analizar_frecuencia(texto: str) -> Dict[str, int]:
    frecuencias = {}
    for char in texto:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias
```

**Ejemplos avanzados**:
```python
texto = "ATTACK AT DAWN"
frecuencias = analizar_frecuencia(texto)
print(frecuencias)
# {'A': 3, 'T': 3, 'C': 1, 'K': 1, 'D': 1, 'W': 1, 'N': 1}

# Análisis relativo
total = sum(frecuencias.values())
for char, count in frecuencias.items():
    print(f"{char}: {count/total:.3f}")
```

### Aplicaciones en Criptoanálisis
- **Cifrado César**: Frecuencias desplazadas
- **Cifrado Vigenère**: Análisis por grupos (Kasiski)
- **Cifrado Sustitución**: Comparación con frecuencias esperadas

## Funciones de Transposición - Reordenamiento

### `ordenar_columnas(clave: str) -> List[int]`
**Propósito**: Generar orden de columnas para transposición
**Algoritmo**: Ordenamiento alfabético con índices estables
**Retorno**: Lista de índices en orden de clave

```python
def ordenar_columnas(clave: str) -> List[int]:
    # Crear lista de (caracter, indice) y ordenar
    pares = [(char, i) for i, char in enumerate(clave.upper())]
    pares.sort()  # Ordena por caracter, luego por indice (estable)
    return [i for _, i in pares]
```

**Ejemplos detallados**:
```python
# Clave "KEY"
orden = ordenar_columnas("KEY")
# Resultado: [1, 2, 0]  # E(1), K(2), Y(0) → posiciones 1,2,0

# Clave con duplicados "KE EY"
orden = ordenar_columnas("KEEY")
# Resultado: [0, 1, 2, 3]  # E(1), E(2), K(0), Y(3) → 1,2,0,3
```

### Algoritmo Interno
1. Convertir clave a mayúsculas
2. Crear pares (carácter, índice)
3. Ordenar por carácter (orden lexicográfico)
4. Extraer índices en orden ordenado

## Validación y Limpieza - Calidad de Datos

### `validar_texto(texto: str, alfabeto: Alfabeto) -> bool`
**Propósito**: Verificar que texto contenga solo caracteres válidos
**Criterios**: Caracteres del alfabeto + espacios permitidos
**Uso**: Pre-validación antes de cifrado

```python
def validar_texto(texto: str, alfabeto: Alfabeto) -> bool:
    for char in texto:
        if char != ' ' and not alfabeto.contiene_caracter(char):
            return False
    return True
```

### `limpiar_texto(texto: str) -> str`
**Propósito**: Preparar texto para operaciones criptográficas
**Operaciones**:
- Eliminar espacios
- Convertir a mayúsculas
- Remover caracteres no alfabéticos

```python
def limpiar_texto(texto: str) -> str:
    return ''.join(c for c in texto.upper() if c.isalpha())
```

**Ejemplos**:
```python
print(limpiar_texto("Hola Mundo!"))        # "HOLAMUNDO"
print(limpiar_texto("Ataque al amanecer")) # "ATAQUEALAMANECER"
print(limpiar_texto("Hello123 World!"))    # "HELLOWORLD"
```

## Integración con Cifrados - Casos de Uso

### Cifrado César
```python
# Uso de Alfabeto para mapeo carácter ↔ número
alfabeto = Alfabeto()
pos_a = alfabeto.obtener_indice('A')  # 0
pos_z = alfabeto.obtener_indice('Z')  # 25

# Limpieza de texto
texto_limpio = limpiar_texto("Hola Mundo")
```

### Cifrado Hill
```python
# Cálculo de inverso modular para descifrado
matriz_clave = [[3, 2], [5, 7]]  # Determinantes deben tener inverso mod 26
det = (3*7 - 2*5) % 26  # 11
inv_det = calcular_inverso_modular(det, 26)  # 19

# Validación de clave
if calcular_mcd(det, 26) != 1:
    raise ValueError("Matriz no invertible")
```

### Cifrado Vigenère
```python
# Análisis de frecuencia para criptoanálisis
texto_cifrado = "KSZEPJLKAM"
frecuencias = analizar_frecuencia(texto_cifrado)
# Usar para detectar periodicidad de clave
```

### Cifrados de Transposición
```python
# Ordenamiento de columnas
clave = "MATRIX"
orden = ordenar_columnas(clave)  # Genera permutación para transposición

# Validación de entrada
if not validar_texto(mensaje, alfabeto):
    raise ValueError("Texto contiene caracteres inválidos")
```

## Optimizaciones y Mejores Prácticas

### Eficiencia
- **Alfabeto**: Búsqueda O(n) aceptable para alfabetos pequeños
- **MCD**: Algoritmo Euclides O(log min(a,b))
- **Frecuencias**: Conteo O(n) single pass
- **Validación**: Early exit en primer carácter inválido

### Manejo de Errores
- **Validación de entrada**: Checks exhaustivos en constructores
- **Excepciones descriptivas**: Mensajes claros para debugging
- **Graceful degradation**: Funciones robustas ante entradas inesperadas

### Extensibilidad
- **Nuevos alfabetos**: Fácil adición sin modificar código existente
- **Operaciones matemáticas**: Framework extensible para nuevos algoritmos
- **Análisis estadístico**: Base para herramientas avanzadas de criptoanálisis

## Testing y Validación

### Cobertura de Tests
- **Unidad**: Cada función probada individualmente
- **Integración**: Funciones trabajando juntas
- **Edge cases**: Entradas límite y casos especiales
- **Propiedades matemáticas**: Verificación de invariantes

### Casos de Prueba Críticos
```python
# Alfabeto vacío
alfabeto_vacio = Alfabeto("")
assert alfabeto_vacio.obtener_longitud() == 0

# MCD con cero
assert calcular_mcd(0, 5) == 5
assert calcular_mcd(5, 0) == 5

# Inverso modular inexistente
try:
    calcular_inverso_modular(4, 26)  # MCD(4,26)=2
    assert False, "Debería lanzar excepción"
except ValueError:
    pass
```

## Conclusión

El módulo `utilidades.py` representa una **arquitectura sólida** que soporta todo el sistema criptográfico. Su diseño modular y bien estructurado permite:

**Ventajas principales**:
- **Reutilización**: Funciones usadas por múltiples cifrados
- **Mantenibilidad**: Cambios localizados afectan mínimamente
- **Extensibilidad**: Fácil adición de nuevos cifrados
- **Robustez**: Validación exhaustiva previene errores
- **Eficiencia**: Algoritmos optimizados para casos comunes

**Contribuciones al sistema**:
- **Abstracción matemática**: Oculta complejidad algebraica
- **Consistencia**: Manejo uniforme de textos y datos
- **Facilitación de testing**: Funciones puras fácilmente testeables
- **Base criptoanalítica**: Herramientas para análisis y ataque

Este módulo demuestra cómo una **buena arquitectura de utilidades** puede simplificar enormemente la implementación y mantenimiento de sistemas complejos como un framework criptográfico completo.