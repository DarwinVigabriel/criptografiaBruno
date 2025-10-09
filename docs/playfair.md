# Cifrado Playfair

## Descripción General

El **cifrado Playfair** es un cifrado digráfico (procesa pares de letras) inventado por Charles Wheatstone en 1854, pero popularizado por Lord Playfair. Fue ampliamente usado por los británicos durante la Primera Guerra Mundial y la Segunda Guerra Mundial. Es uno de los cifrados manuales más sofisticados y fue considerado "indescifrable" por el público general.

A diferencia de los cifrados monoalfabéticos, Playfair opera sobre **bigramas** (pares de letras) y utiliza una **matriz 5×5** generada a partir de una palabra clave.

## Historia y Contexto

### Origen y Desarrollo
- **1854**: Charles Wheatstone inventa el cifrado
- **1854**: Lord Playfair lo presenta al gobierno británico
- **1890s**: Usado por el ejército británico en Sudáfrica
- **Primera Guerra Mundial**: Cifrado principal del ejército británico
- **Segunda Guerra Mundial**: Usado por resistencia y servicios de inteligencia

### Importancia Histórica
- **Primer cifrado digráfico práctico**: Procesaba letras en pares
- **Uso militar extenso**: Confiado para comunicaciones sensibles
- **Mayor seguridad**: Mucho más resistente que César o Vigenère
- **Transición a cifrados modernos**: Puente entre métodos clásicos y contemporáneos

### Terminología
- **Digráfico**: Opera sobre pares de letras (dígrafos)
- **Matriz de Playfair**: Cuadrado 5×5 con clave y alfabeto
- **Regla de Wheatstone**: Algoritmo de cifrado básico
- **Homófonos**: Múltiples formas de cifrar la misma letra

## Lógica Matemática

### Definición Formal

Sea K una palabra clave y Σ = {A,B,C,...,Z} menos J (o I=J). La matriz M se construye como:

1. **Primera fila**: Letras de K sin repeticiones
2. **Resto**: Letras restantes en orden alfabético

Para un dígrafo (a,b), las reglas son:
- **Fila común**: Desplazamiento circular derecho
- **Columna común**: Desplazamiento circular abajo
- **Rectángulo**: Intercambio de columnas

### Propiedades Matemáticas

1. **No lineal**: Relación compleja entre entrada y salida
2. **Difusión**: Un cambio afecta al par completo
3. **Confusión**: La clave se distribuye en toda la matriz
4. **Periodo 5**: La matriz tiene simetría circular

## Algoritmo Detallado

### Construcción de la Matriz

```python
def construir_matriz_playfair(clave, alfabeto="ABCDEFGHIKLMNOPQRSTUVWXYZ"):
    # I y J se tratan como el mismo caracter
    clave = clave.upper().replace('J', 'I')

    # Remover duplicados manteniendo orden
    clave_limpia = ""
    for c in clave:
        if c in alfabeto and c not in clave_limpia:
            clave_limpia += c

    # Agregar letras restantes
    for c in alfabeto:
        if c not in clave_limpia:
            clave_limpia += c

    # Crear matriz 5x5
    matriz = []
    for i in range(0, 25, 5):
        matriz.append(list(clave_limpia[i:i+5]))

    return matriz
```

### Preparación del Texto

```python
def preparar_texto_playfair(texto):
    # Convertir a mayúsculas, I=J
    texto = texto.upper().replace('J', 'I')

    # Remover no-letras
    texto_limpio = "".join(c for c in texto if c.isalpha())

    # Procesar en pares
    preparado = ""
    i = 0
    while i < len(texto_limpio):
        a = texto_limpio[i]
        i += 1

        if i < len(texto_limpio):
            b = texto_limpio[i]
            i += 1

            preparado += a
            if a == b:
                # Insertar X entre letras iguales
                preparado += 'X'
            preparado += b
        else:
            # Última letra sola
            preparado += a + 'X'

    return preparado
```

### Reglas de Cifrado

#### 1. Misma Fila
```
Si a y b están en la misma fila:
Nueva_a = letra a la derecha de a (circular)
Nueva_b = letra a la derecha de b (circular)
```

**Ejemplo**:
```
Matriz: C L A V E
         B D F G H
         ...
Posición: L(0,1), A(0,2) → V(0,3), E(0,4)
```

#### 2. Misma Columna
```
Si a y b están en la misma columna:
Nueva_a = letra abajo de a (circular)
Nueva_b = letra abajo de b (circular)
```

**Ejemplo**:
```
Matriz: C L A V E
         B D F G H
         I K M N O
         ...
Posición: L(0,1), D(1,1) → D(1,1), K(2,1)
```

#### 3. Rectángulo (Diferente fila y columna)
```
Forman un rectángulo:
Nueva_a = letra en fila de a, columna de b
Nueva_b = letra en fila de b, columna de a
```

**Ejemplo**:
```
Matriz: C L A V E
         B D F G H
         I K M N O
Posición: L(0,1), M(2,2) → F(1,2), K(2,1)
```

## Ejemplos Detallados

### Ejemplo 1: Caso Básico
```
Clave: "PLAYFAIR"
Mensaje: "HI"

Matriz resultante:
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z

Preparación: "HI" (sin cambios)

Cifrado:
H(2,2), I(1,0) → rectángulo → B(1,2), E(2,0) → "BE"
```

### Ejemplo 2: Con Repeticiones
```
Clave: "PLAYFAIR"
Mensaje: "HELLO"

Preparación: "HE LX LO" (X insertado entre Ls)

Cifrado:
HE: H(2,2), E(2,0) → rectángulo → B(1,2), I(1,0) → "BI"
LX: L(0,1), X(4,3) → rectángulo → Y(0,3), P(4,1) → "YP"
LO: L(0,1), O(3,1) → misma columna → R(1,1), T(4,1) → "RT"

Resultado: "BIYPRT"
```

### Ejemplo 3: Texto Completo
```
Clave: "ROYAL"
Mensaje: "ATTACK AT DAWN"

Preparación: "AT TA CK AT DA WN" (agregado X donde necesario)

Matriz:
R O Y A L
B C D E F
G H I K M
N P Q S T
U V W X Z

Cifrado paso a paso:
AT: A(0,3), T(3,4) → rectángulo → L(0,4), Y(3,3) → "LY"
TA: T(3,4), A(0,3) → rectángulo → L(3,3), T(0,4) → "LT"
CK: C(1,1), K(2,3) → rectángulo → I(1,3), D(2,1) → "ID"
AT: A(0,3), T(3,4) → "LY" (mismo que primer par)
DA: D(1,2), A(0,3) → rectángulo → A(0,2), D(1,3) → "AD"
WN: W(4,2), N(3,0) → rectángulo → P(4,0), W(3,2) → "PW"

Resultado: "LYLTIDLYADPW"
```

### Ejemplo 4: Misma Fila
```
Clave: "CIPHER"
Mensaje: "WE"

Matriz:
C I P H E
R A B D F
G K L M N
O Q S T U
V W X Y Z

WE: W(4,1), E(0,4) → rectángulo → H(0,1), V(4,4) → "HV"
```

### Ejemplo 5: Misma Columna
```
Clave: "CIPHER"
Mensaje: "NO"

NO: N(2,4), O(3,0) → rectángulo → Q(3,4), G(2,0) → "QG"
```

## Criptoanálisis (Ataques)

### Análisis de Frecuencia de Dígrafos

**Dígrafos comunes en inglés**:
- TH (3.8%), HE (3.1%), IN (2.4%), ER (2.2%)
- Dígrafos raros: QZ, JX, etc.

**En Playfair**: Los dígrafos se transforman siguiendo las reglas de la matriz.

### Ataque por Texto Plano Conocido

**Método**: Si se conoce un dígrafo original y su cifrado, se puede deducir la estructura de la matriz.

**Ejemplo**:
- Conocido: "TH" → "KM"
- Posibles configuraciones de T, H, K, M en la matriz
- Probar diferentes hipótesis

### Ataque por Fuerza Bruta

**Complejidad**: 26! / (26-5)! ≈ 7.9×10¹⁰ matrices posibles
**Reducción**: Contexto lingüístico reduce significativamente

### Análisis de Patrones

**Observaciones**:
- **Letras que no cambian**: Si un dígrafo resulta en sí mismo
- **Simetrías**: Propiedades de la matriz circular
- **Frecuencias**: Algunos dígrafos aparecen más que otros

## Variantes y Extensiones

### Playfair Cuádruple
- Procesa cuatro letras simultáneamente
- Matrices más grandes (6×6, 7×7)
- Mayor seguridad pero más complejo

### Playfair con Números
- Incluye dígitos en la matriz
- Alfabeto extendido

### Playfair Bifid
- Combina Playfair con cifrado bifid
- Dos etapas de transformación

### Playfair Moderno
- Implementaciones computacionales
- Matrices más grandes
- Automatización del proceso

## Análisis de Seguridad

### Fortalezas
- **Rompe análisis de frecuencia simple**: Opera sobre pares
- **Difusión buena**: Cambio en una letra afecta al par
- **Confusión**: Clave distribuida en matriz 5×5
- **Manual**: No requiere computadoras

### Debilidades
- **Vulnerable a texto plano conocido**: Un par revela estructura
- **Análisis de dígrafos**: Frecuencias de pares son características
- **Tamaño de clave limitado**: Solo 25 posiciones
- **Reglas determinísticas**: Una vez conocida la matriz, trivial

### Comparación de Seguridad

| Método | Resistencia a Frecuencia | Resistencia a Conocido | Complejidad |
|--------|--------------------------|------------------------|-------------|
| César | Muy Baja | Muy Baja | Muy Baja |
| Vigenère | Media | Baja | Baja |
| Playfair | Alta | Media | Media |
| Hill | Alta | Alta | Alta |

## Aplicaciones Modernas

### Usos Legítimos
- **Educación**: Enseñar conceptos de cifrados digráficos
- **Juegos**: Rompecabezas y acertijos
- **Ofuscación**: Para texto no crítico
- **Arte**: Efectos estilísticos en literatura

### Usos Históricos
- **Militar**: Comunicaciones en guerras mundiales
- **Inteligencia**: Servicios secretos británicos
- **Diplomático**: Comunicaciones oficiales
- **Comercial**: Empresas de telégrafos

## Implementación Completa

```python
from typing import List, Tuple

class CifradoPlayfair:
    """
    Implementación del cifrado Playfair.
    Cifrado digráfico que usa una matriz 5x5.
    """

    def __init__(self, clave: str):
        """
        Inicializa el cifrado Playfair.

        Args:
            clave: Palabra clave para generar la matriz
        """
        self.clave = clave.upper().replace('J', 'I')
        self.matriz = self._construir_matriz()
        self.posiciones = self._calcular_posiciones()

    def _construir_matriz(self) -> List[List[str]]:
        """Construye la matriz 5x5 de Playfair"""
        alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Sin J
        matriz = [['' for _ in range(5)] for _ in range(5)]

        # Agregar clave sin duplicados
        usados = set()
        clave_limpia = ""

        for c in self.clave:
            if c in alfabeto and c not in usados:
                usados.add(c)
                clave_limpia += c

        # Agregar letras restantes
        for c in alfabeto:
            if c not in usados:
                clave_limpia += c

        # Llenar matriz
        indice = 0
        for fila in range(5):
            for col in range(5):
                matriz[fila][col] = clave_limpia[indice]
                indice += 1

        return matriz

    def _calcular_posiciones(self) -> dict:
        """Calcula las posiciones de cada letra en la matriz"""
        posiciones = {}
        for fila in range(5):
            for col in range(5):
                posiciones[self.matriz[fila][col]] = (fila, col)
        return posiciones

    def _preparar_texto(self, texto: str) -> str:
        """
        Prepara el texto para cifrado:
        - Mayúsculas
        - I = J
        - Solo letras
        - Separar letras repetidas con X
        - Rellenar con X si impar
        """
        # Limpiar texto
        texto = texto.upper().replace('J', 'I')
        texto_limpio = "".join(c for c in texto if c.isalpha())

        # Procesar en pares
        preparado = ""
        i = 0
        while i < len(texto_limpio):
            a = texto_limpio[i]
            i += 1

            if i < len(texto_limpio):
                b = texto_limpio[i]
                i += 1

                preparado += a
                if a == b:
                    preparado += 'X'
                preparado += b
            else:
                # Última letra sola
                preparado += a + 'X'

        return preparado

    def _cifrar_digrafo(self, digrafo: str) -> str:
        """Cifra un dígrafo según las reglas de Playfair"""
        a, b = digrafo[0], digrafo[1]
        fila_a, col_a = self.posiciones[a]
        fila_b, col_b = self.posiciones[b]

        if fila_a == fila_b:
            # Misma fila: desplazar derecha
            return (self.matriz[fila_a][(col_a + 1) % 5] +
                    self.matriz[fila_b][(col_b + 1) % 5])

        elif col_a == col_b:
            # Misma columna: desplazar abajo
            return (self.matriz[(fila_a + 1) % 5][col_a] +
                    self.matriz[(fila_b + 1) % 5][col_b])

        else:
            # Rectángulo: intercambiar columnas
            return (self.matriz[fila_a][col_b] +
                    self.matriz[fila_b][col_a])

    def _descifrar_digrafo(self, digrafo: str) -> str:
        """Descifra un dígrafo (reglas inversas)"""
        a, b = digrafo[0], digrafo[1]
        fila_a, col_a = self.posiciones[a]
        fila_b, col_b = self.posiciones[b]

        if fila_a == fila_b:
            # Misma fila: desplazar izquierda
            return (self.matriz[fila_a][(col_a - 1) % 5] +
                    self.matriz[fila_b][(col_b - 1) % 5])

        elif col_a == col_b:
            # Misma columna: desplazar arriba
            return (self.matriz[(fila_a - 1) % 5][col_a] +
                    self.matriz[(fila_b - 1) % 5][col_b])

        else:
            # Rectángulo: mismo intercambio
            return (self.matriz[fila_a][col_b] +
                    self.matriz[fila_b][col_a])

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Playfair.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado
        """
        preparado = self._preparar_texto(texto_plano)
        resultado = ""

        for i in range(0, len(preparado), 2):
            digrafo = preparado[i:i+2]
            resultado += self._cifrar_digrafo(digrafo)

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Playfair.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado (puede contener X de relleno)
        """
        # El texto cifrado ya viene en pares
        resultado = ""

        for i in range(0, len(texto_cifrado), 2):
            digrafo = texto_cifrado[i:i+2]
            resultado += self._descifrar_digrafo(digrafo)

        return resultado

    def obtener_matriz(self) -> List[List[str]]:
        """Retorna la matriz de Playfair"""
        return [fila[:] for fila in self.matriz]

    def mostrar_matriz(self) -> str:
        """Retorna representación visual de la matriz"""
        return "\n".join(" ".join(fila) for fila in self.matriz)

# Funciones de conveniencia
def cifrar_playfair(texto: str, clave: str) -> str:
    """Función de conveniencia para cifrar con Playfair"""
    playfair = CifradoPlayfair(clave)
    return playfair.cifrar(texto)

def descifrar_playfair(texto: str, clave: str) -> str:
    """Función de conveniencia para descifrar con Playfair"""
    playfair = CifradoPlayfair(clave)
    return playfair.descifrar(texto)

# Ejemplo de uso
if __name__ == "__main__":
    clave = "PLAYFAIR"
    mensaje = "HIDE THE GOLD"

    print(f"Clave: {clave}")
    print(f"Mensaje: {mensaje}")

    playfair = CifradoPlayfair(clave)
    print("\nMatriz generada:")
    print(playfair.mostrar_matriz())

    # Cifrado
    cifrado = playfair.cifrar(mensaje)
    print(f"\nTexto cifrado: {cifrado}")

    # Descifrado
    descifrado = playfair.descifrar(cifrado)
    print(f"Texto descifrado: {descifrado}")

    # Limpiar X de relleno
    descifrado_limpio = descifrado.replace('X', '')
    print(f"Descifrado limpio: {descifrado_limpio}")

    # Verificar
    original_limpio = mensaje.upper().replace(' ', '').replace('J', 'I')
    print(f"¿Correcto? {original_limpio == descifrado_limpio}")

    # Ejemplo con letras repetidas
    print("\n--- Ejemplo con letras repetidas ---")
    mensaje2 = "HELLO"
    cifrado2 = playfair.cifrar(mensaje2)
    descifrado2 = playfair.descifrar(cifrado2)

    print(f"Mensaje: {mensaje2}")
    print(f"Cifrado: {cifrado2}")
    print(f"Descifrado: {descifrado2}")
    print(f"Limpio: {descifrado2.replace('X', '')}")
```

## Conclusión

El cifrado Playfair representa un **hito en la criptografía manual**, siendo uno de los primeros métodos prácticos que rompe efectivamente el análisis de frecuencia simple. Aunque ya no se considera seguro por estándares modernos, su diseño elegante y efectividad histórica lo convierten en un algoritmo fundamental para entender la evolución de los cifrados.

**Legado**:
- **Transición a cifrados modernos**: Puente entre métodos clásicos y contemporáneos
- **Conceptos fundamentales**: Difusión, confusión, procesamiento por bloques
- **Influencia duradera**: Base para muchos cifrados digráficos posteriores
- **Valor educativo**: Excelente para enseñar principios de criptografía práctica

Su estudio es esencial para comprender cómo la criptografía evolucionó desde métodos simples de sustitución hacia algoritmos más sofisticados basados en matemáticas avanzadas.