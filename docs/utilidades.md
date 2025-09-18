# Utilidades - Funciones de Soporte

## Descripción

El módulo `utilidades.py` contiene funciones y clases auxiliares que soportan la implementación de los cifrados clásicos. Incluye manejo de alfabetos, operaciones matemáticas, análisis de frecuencia y funciones de validación y limpieza de texto.

## Clase Alfabeto

### Descripción
La clase `Alfabeto` maneja alfabetos personalizados para los cifrados, permitiendo configuraciones flexibles de caracteres válidos.

### Constructor
```python
def __init__(self, alfabeto_personalizado: Optional[str] = None, case_sensitive: bool = False)
```

**Parámetros:**
- `alfabeto_personalizado`: Cadena con caracteres personalizados (opcional)
- `case_sensitive`: Si distingue mayúsculas/minúsculas

**Ejemplo:**
```python
# Alfabeto por defecto (A-Z, a-z)
alfabeto_default = Alfabeto()

# Alfabeto personalizado
alfabeto_espanol = Alfabeto("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

# Case sensitive
alfabeto_cs = Alfabeto(case_sensitive=True)
```

### Métodos Principales

#### `obtener_longitud() -> int`
Retorna la cantidad de caracteres en el alfabeto.

#### `obtener_indice(caracter: str) -> int`
Obtiene la posición de un carácter en el alfabeto.
- Retorna el índice (0-based) si existe
- Retorna -1 si no existe

**Ejemplo:**
```python
alfabeto = Alfabeto()
print(alfabeto.obtener_indice('A'))  # 0
print(alfabeto.obtener_indice('Z'))  # 25
print(alfabeto.obtener_indice('1'))  # -1
```

#### `obtener_caracter(indice: int) -> str`
Obtiene el carácter en una posición específica.

**Ejemplo:**
```python
alfabeto = Alfabeto()
print(alfabeto.obtener_caracter(0))   # 'A'
print(alfabeto.obtener_caracter(25))  # 'Z'
```

#### `contiene_caracter(caracter: str) -> bool`
Verifica si un carácter pertenece al alfabeto.

#### `normalizar_texto(texto: str) -> str`
Convierte el texto al formato del alfabeto (mayúsculas, caracteres válidos).

#### `filtrar_texto(texto: str) -> str`
Elimina caracteres que no están en el alfabeto.

## Funciones Matemáticas

### `calcular_mcd(a: int, b: int) -> int`
Calcula el máximo común divisor usando el algoritmo de Euclides.

**Ejemplo:**
```python
print(calcular_mcd(48, 18))  # 6
print(calcular_mcd(100, 75)) # 25
```

### `calcular_inverso_modular(a: int, m: int) -> int`
Calcula el inverso modular usando el algoritmo extendido de Euclides. Esencial para el cifrado Hill.

**Ejemplo:**
```python
# Encontrar x tal que (7 * x) mod 26 = 1
print(calcular_inverso_modular(7, 26))  # 15, porque 7*15 = 105, 105 mod 26 = 1
```

## Análisis de Frecuencia

### `analizar_frecuencia(texto: str) -> Dict[str, int]`
Realiza análisis de frecuencia de letras en un texto, útil para criptoanálisis.

**Ejemplo:**
```python
texto = "HOLA MUNDO HOLA"
frecuencias = analizar_frecuencia(texto)
print(frecuencias)
# {'H': 2, 'O': 2, 'L': 2, 'A': 2, 'M': 1, 'U': 1, 'N': 1, 'D': 1}
```

## Funciones de Transposición

### `ordenar_columnas(clave: str) -> List[int]`
Ordena los índices de las columnas según el orden alfabético de la clave. Usado en cifrados de transposición.

**Ejemplo:**
```python
clave = "CLAVE"
orden = ordenar_columnas(clave)
print(orden)  # [2, 4, 0, 1, 3]  # A(0), C(2), E(1), L(4), V(3)
```

## Validación y Limpieza

### `validar_texto(texto: str, alfabeto: Alfabeto) -> bool`
Valida que el texto contenga solo caracteres válidos del alfabeto (más espacios).

**Ejemplo:**
```python
alfabeto = Alfabeto()
print(validar_texto("HOLA MUNDO", alfabeto))  # True
print(validar_texto("HOLA123", alfabeto))     # False
```

### `limpiar_texto(texto: str) -> str`
Limpia el texto eliminando espacios y convirtiendo a mayúsculas.

**Ejemplo:**
```python
print(limpiar_texto("Hola Mundo!"))  # "HOLAMUNDO"
print(limpiar_texto("Ataque al amanecer"))  # "ATAQUEALAMANECER"
```

## Uso en Cifrados

Estas utilidades son fundamentales para todos los cifrados implementados:

- **Alfabeto**: Proporciona consistencia en el manejo de caracteres
- **Funciones matemáticas**: Soportan operaciones modulares en Hill
- **Análisis de frecuencia**: Ayuda en ataques criptográficos
- **Ordenar columnas**: Base para transposiciones
- **Validación y limpieza**: Preparan textos para cifrado

Todas las funciones están diseñadas para ser reutilizables y mantener la coherencia entre diferentes implementaciones de cifrados.