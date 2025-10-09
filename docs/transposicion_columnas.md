# Cifrados de Transposición

## Descripción General

Los **cifrados de transposición** son métodos criptográficos que **reorganizan** los caracteres del mensaje sin cambiarlos, a diferencia de los cifrados de sustitución que los reemplazan. Son algunos de los métodos más antiguos de cifrado y fueron ampliamente usados en la antigüedad.

Existen varios tipos principales:
- **Rail Fence (Zigzag)**: Escribe en diagonales
- **Transposición de Columnas**: Usa una matriz con clave
- **Permutación General**: Reordena según una clave arbitraria

## Historia y Contexto

### Origen y Desarrollo
- **Antigua Grecia**: Escítala espartana (siglo V a.C.)
- **Renacimiento**: Desarrollo de métodos sistemáticos
- **Primera Guerra Mundial**: Uso militar extenso
- **Segunda Guerra Mundial**: Parte de sistemas complejos

### Importancia Histórica
- **Primeros cifrados prácticos**: Más simples que sustitución
- **Uso militar**: Confiables para comunicaciones
- **Base conceptual**: Fundamento de cifrados modernos
- **Transición**: De métodos manuales a computacionales

### Terminología
- **Transposición**: Reordenamiento de elementos
- **Permutación**: Reordenamiento específico
- **Rieles**: Líneas diagonales en Rail Fence
- **Matriz**: Tabla para organizar caracteres

## Tipos de Cifrados de Transposición

### 1. Rail Fence (Zigzag)

#### Descripción
El cifrado Rail Fence escribe el texto zigzagueando a través de "rieles" diagonales imaginarios.

#### Algoritmo
```python
def rail_fence_cifrar(texto, rieles):
    if rieles == 1:
        return texto

    # Crear rieles
    rail = [[] for _ in range(rieles)]
    direccion = 1
    fila = 0

    # Escribir en zigzag
    for char in texto:
        rail[fila].append(char)
        fila += direccion

        # Cambiar dirección en los extremos
        if fila == 0 or fila == rieles - 1:
            direccion = -direccion

    # Leer rieles
    resultado = ""
    for r in rail:
        resultado += "".join(r)

    return resultado
```

#### Ejemplos Detallados

**Ejemplo 1: 3 Rieles**
```
Mensaje: "ATTACKATDAWN"

Escritura zigzag:
A   A   A   A
 T C   T D W
  T   K   A N

Riel 1: A A A A
Riel 2: T C T D W
Riel 3: T K A N

Resultado: "AAAA TCTDW TKAN"
```

**Ejemplo 2: 4 Rieles**
```
Mensaje: "HELLO WORLD"

H     L     R
 E   O   O   D
  L   W   L
   L       D

Resultado: "HLR EOOD LWL LD"
```

**Ejemplo 3: 2 Rieles (Simple)**
```
Mensaje: "ATTACK"

A T C K
 T A C

Resultado: "ATCK TAC"
```

#### Criptoanálisis
- **Patrón visual**: Fácil detectar el zigzag
- **Longitud de rieles**: Determina número de rieles
- **Frecuencias**: Se preservan en cada riel

### 2. Transposición de Columnas

#### Descripción
Escribe el texto en filas de una matriz y lee por columnas en orden determinado por una clave.

#### Algoritmo
```python
def transposicion_columnas_cifrar(texto, clave):
    # Crear matriz
    num_cols = len(clave)
    num_filas = (len(texto) + num_cols - 1) // num_cols

    # Rellenar matriz
    matriz = [['' for _ in range(num_cols)] for _ in range(num_filas)]
    idx = 0
    for fila in range(num_filas):
        for col in range(num_cols):
            if idx < len(texto):
                matriz[fila][col] = texto[idx]
                idx += 1

    # Ordenar columnas por clave
    orden = sorted(range(num_cols), key=lambda x: clave[x])

    # Leer por columnas ordenadas
    resultado = ""
    for col in orden:
        for fila in range(num_filas):
            if matriz[fila][col]:
                resultado += matriz[fila][col]

    return resultado
```

#### Ejemplos Detallados

**Ejemplo 1: Clave "KEY"**
```
Mensaje: "ATTACKATDAWN"
Clave: "KEY" → orden: E(1), K(2), Y(0) → [2, 0, 1]

Matriz:
A T T
A C K
A T D
A W N

Ordenado por clave (Y, E, K):
Col2 Col0 Col1
T   A   T
K   C   C
D   A   K
N   A   T

Lectura: T K D N A C A A T T C T

Resultado: "TKDNACAATTCT"
```

**Ejemplo 2: Con Relleno**
```
Mensaje: "HELLO"
Clave: "ABC"

Matriz (relleno X):
H E L
L O X

Orden: A(0), B(1), C(2) → [0, 1, 2]

Lectura: H L L E O X

Resultado: "HLLEOX"
```

#### Criptoanálisis
- **Análisis de columnas**: Cada columna mantiene frecuencias
- **Longitud de clave**: Determina número de columnas
- **Orden alfabético**: Claves suelen ordenarse alfabéticamente

### 3. Permutación General

#### Descripción
Reordena bloques de texto según una permutación arbitraria definida por una clave.

#### Algoritmo
```python
def permutacion_general_cifrar(texto, clave):
    tam_bloque = len(clave)

    # Crear permutación
    permutacion = crear_permutacion(clave)

    resultado = ""
    for i in range(0, len(texto), tam_bloque):
        bloque = texto[i:i+tam_bloque]

        # Aplicar permutación
        bloque_permutado = [''] * len(bloque)
        for j, pos in enumerate(permutacion):
            if j < len(bloque):
                bloque_permutado[pos] = bloque[j]

        resultado += "".join(bloque_permutado)

    return resultado
```

#### Ejemplos Detallados

**Ejemplo 1: Clave "3142"**
```
Mensaje: "ATTACKATDAWN"
Bloques de 4: "ATTA", "CKAT", "DAWN"

Permutación: 3,1,4,2 → posiciones [2,0,3,1]

"ATTA" → pos2=A, pos0=T, pos3=T, pos1=A → "A T T A"
"CKAT" → "A K C T"
"DAWN" → "W D N A"

Resultado: "ATTAAKCTWDNA"
```

## Comparación de Métodos

| Método | Complejidad | Seguridad | Facilidad de Uso |
|--------|-------------|-----------|------------------|
| Rail Fence | Baja | Baja | Alta |
| Columnas | Media | Media | Media |
| Permutación | Alta | Alta | Baja |

## Criptoanálisis General

### Ataque por Fuerza Bruta
- **Rail Fence**: Probar 2-10 rieles
- **Columnas**: Probar claves de diferentes longitudes
- **Permutación**: Muy costoso

### Análisis de Patrones
- **Frecuencias preservadas**: Transposición no cambia frecuencias
- **Longitud de palabras**: Puede mantenerse
- **Estructura**: Buscar patrones regulares

### Ataque Lingüístico
- **Palabras comunes**: Buscar en posiciones probables
- **Contexto**: Usar conocimiento del idioma
- **Longitud**: Determinar tamaño de bloques

## Análisis de Seguridad

### Fortalezas
- **No cambia frecuencias**: Más difícil que sustitución simple
- **Estructura rota**: Desordena secuencias
- **Simple implementación**: Fácil de usar manualmente
- **Reversible**: Siempre se puede descifrar

### Debilidades
- **Frecuencias preservadas**: Análisis estadístico posible
- **Patrones visuales**: Algunos métodos detectables
- **Clave crítica**: Si se conoce, trivial
- **Sin difusión**: Un cambio afecta localmente

### Seguridad por Método

| Método | Resistencia a Frecuencia | Resistencia Visual | Robustez |
|--------|--------------------------|-------------------|-----------|
| Rail Fence | Baja | Muy Baja | Baja |
| Columnas | Media | Media | Media |
| Permutación | Alta | Alta | Alta |

## Implementación Completa

```python
from typing import List, Union
import math

class CifradoTransposicion:
    """
    Implementación unificada de cifrados de transposición.
    Soporta Rail Fence, Transposición de Columnas y Permutación General.
    """

    def __init__(self, metodo: str, parametro: Union[int, str], relleno: str = 'X'):
        """
        Inicializa el cifrado de transposición.

        Args:
            metodo: "rail_fence", "columnas", o "permutacion"
            parametro: número de rieles (int) o clave (str)
            relleno: caracter para rellenar
        """
        self.metodo = metodo.lower()
        self.parametro = parametro
        self.relleno = relleno

        if self.metodo not in ["rail_fence", "columnas", "permutacion"]:
            raise ValueError("Método debe ser 'rail_fence', 'columnas', o 'permutacion'")

    def _rail_fence_cifrar(self, texto: str, rieles: int) -> str:
        """Cifra usando Rail Fence"""
        if rieles <= 1:
            return texto

        rail = [[] for _ in range(rieles)]
        direccion = 1
        fila = 0

        for char in texto:
            rail[fila].append(char)
            fila += direccion
            if fila == 0 or fila == rieles - 1:
                direccion = -direccion

        return "".join("".join(r) for r in rail)

    def _rail_fence_descifrar(self, texto: str, rieles: int) -> str:
        """Descifra Rail Fence"""
        if rieles <= 1:
            return texto

        # Calcular longitud de cada riel
        longitudes = [0] * rieles
        direccion = 1
        fila = 0

        for _ in range(len(texto)):
            longitudes[fila] += 1
            fila += direccion
            if fila == 0 or fila == rieles - 1:
                direccion = -direccion

        # Distribuir caracteres en rieles
        rieles_data = []
        idx = 0
        for longitud in longitudes:
            rieles_data.append(texto[idx:idx + longitud])
            idx += longitud

        # Reconstruir zigzag
        resultado = []
        indices = [0] * rieles
        fila = 0
        direccion = 1

        for _ in range(len(texto)):
            resultado.append(rieles_data[fila][indices[fila]])
            indices[fila] += 1
            fila += direccion
            if fila == 0 or fila == rieles - 1:
                direccion = -direccion

        return "".join(resultado)

    def _columnas_cifrar(self, texto: str, clave: str) -> str:
        """Cifra usando transposición de columnas"""
        clave = clave.upper()
        num_cols = len(clave)
        num_filas = math.ceil(len(texto) / num_cols)

        # Crear matriz con relleno
        matriz = [['' for _ in range(num_cols)] for _ in range(num_filas)]
        idx = 0
        for fila in range(num_filas):
            for col in range(num_cols):
                if idx < len(texto):
                    matriz[fila][col] = texto[idx]
                    idx += 1
                else:
                    matriz[fila][col] = self.relleno

        # Orden de columnas por clave
        orden = sorted(range(num_cols), key=lambda x: clave[x])

        # Leer por columnas ordenadas
        resultado = ""
        for col in orden:
            for fila in range(num_filas):
                resultado += matriz[fila][col]

        return resultado.rstrip(self.relleno)

    def _columnas_descifrar(self, texto: str, clave: str) -> str:
        """Descifra transposición de columnas"""
        clave = clave.upper()
        num_cols = len(clave)
        num_filas = math.ceil(len(texto) / num_cols)

        # Crear matriz para resultado
        matriz = [['' for _ in range(num_cols)] for _ in range(num_filas)]

        # Orden de columnas por clave
        orden = sorted(range(num_cols), key=lambda x: clave[x])

        # Distribuir texto cifrado
        idx = 0
        for col_idx, col in enumerate(orden):
            for fila in range(num_filas):
                if idx < len(texto):
                    matriz[fila][col] = texto[idx]
                    idx += 1

        # Leer por filas
        resultado = ""
        for fila in range(num_filas):
            for col in range(num_cols):
                if matriz[fila][col] and matriz[fila][col] != self.relleno:
                    resultado += matriz[fila][col]

        return resultado

    def _permutacion_cifrar(self, texto: str, clave: str) -> str:
        """Cifra usando permutación general"""
        tam_bloque = len(clave)

        # Crear permutación (orden alfabético por defecto)
        permutacion = sorted(range(tam_bloque), key=lambda x: clave[x])

        resultado = ""
        for i in range(0, len(texto), tam_bloque):
            bloque = texto[i:i + tam_bloque]

            # Aplicar permutación
            bloque_permutado = [''] * len(bloque)
            for j, pos in enumerate(permutacion):
                if j < len(bloque):
                    bloque_permutado[pos] = bloque[j]

            resultado += "".join(bloque_permutado)

        return resultado

    def _permutacion_descifrar(self, texto: str, clave: str) -> str:
        """Descifra permutación general"""
        tam_bloque = len(clave)

        # Crear permutación
        permutacion = sorted(range(tam_bloque), key=lambda x: clave[x])

        # Crear inversa
        inversa = [0] * tam_bloque
        for i, pos in enumerate(permutacion):
            inversa[pos] = i

        resultado = ""
        for i in range(0, len(texto), tam_bloque):
            bloque = texto[i:i + tam_bloque]

            # Aplicar permutación inversa
            bloque_original = [''] * len(bloque)
            for j, pos in enumerate(inversa):
                if j < len(bloque):
                    bloque_original[pos] = bloque[j]

            resultado += "".join(bloque_original)

        return resultado

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando el método de transposición especificado.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado
        """
        texto = "".join(c for c in texto_plano if c.isalpha()).upper()

        if self.metodo == "rail_fence":
            return self._rail_fence_cifrar(texto, self.parametro)
        elif self.metodo == "columnas":
            return self._columnas_cifrar(texto, self.parametro)
        elif self.metodo == "permutacion":
            return self._permutacion_cifrar(texto, self.parametro)

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con transposición.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado
        """
        texto = "".join(c for c in texto_cifrado if c.isalpha()).upper()

        if self.metodo == "rail_fence":
            return self._rail_fence_descifrar(texto, self.parametro)
        elif self.metodo == "columnas":
            return self._columnas_descifrar(texto, self.parametro)
        elif self.metodo == "permutacion":
            return self._permutacion_descifrar(texto, self.parametro)

# Funciones de conveniencia
def cifrar_rail_fence(texto: str, rieles: int) -> str:
    """Función de conveniencia para Rail Fence"""
    cifrado = CifradoTransposicion("rail_fence", rieles)
    return cifrado.cifrar(texto)

def cifrar_transposicion_columnas(texto: str, clave: str) -> str:
    """Función de conveniencia para transposición de columnas"""
    cifrado = CifradoTransposicion("columnas", clave)
    return cifrado.cifrar(texto)

def cifrar_permutacion_general(texto: str, clave: str) -> str:
    """Función de conveniencia para permutación general"""
    cifrado = CifradoTransposicion("permutacion", clave)
    return cifrado.cifrar(texto)

# Ejemplos de uso
if __name__ == "__main__":
    mensaje = "ATTACKATDAWN"

    # Rail Fence
    print("=== Rail Fence ===")
    rail_fence = CifradoTransposicion("rail_fence", 3)
    cifrado_rf = rail_fence.cifrar(mensaje)
    descifrado_rf = rail_fence.descifrar(cifrado_rf)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado_rf}")
    print(f"Descifrado: {descifrado_rf}")

    # Transposición de Columnas
    print("\n=== Transposición de Columnas ===")
    columnas = CifradoTransposicion("columnas", "KEY")
    cifrado_col = columnas.cifrar(mensaje)
    descifrado_col = columnas.descifrar(cifrado_col)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado_col}")
    print(f"Descifrado: {descifrado_col}")

    # Permutación General
    print("\n=== Permutación General ===")
    permutacion = CifradoTransposicion("permutacion", "3142")
    cifrado_perm = permutacion.cifrar(mensaje)
    descifrado_perm = permutacion.descifrar(cifrado_perm)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado_perm}")
    print(f"Descifrado: {descifrado_perm}")
```

## Conclusión

Los cifrados de transposición representan una **clase fundamental** de algoritmos criptográficos que operan mediante **reordenamiento** en lugar de sustitución. Aunque más seguros que los cifrados de sustitución simples, son vulnerables a análisis estadísticos y ataques lingüísticos.

**Contribuciones clave**:
- **Principio de transposición**: Reordenamiento preserva contenido
- **Quebrado de secuencias**: Dificulta análisis de patrones
- **Base para modernos**: Influencia en cifrados de bloque
- **Simplicidad conceptual**: Fácil comprensión y análisis

Su estudio es esencial para entender la evolución de la criptografía desde métodos manuales simples hacia algoritmos más sofisticados, sentando las bases para el desarrollo de sistemas criptográficos modernos.