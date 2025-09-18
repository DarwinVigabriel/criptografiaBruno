# Informe Ampliado: Librería de Cifrados Clásicos

## Introducción

Esta librería implementa una colección completa de algoritmos de cifrado clásicos de sustitución y transposición. El proyecto está diseñado con fines educativos para estudiar criptografía histórica y sus vulnerabilidades.

A continuación se presenta un análisis detallado de cada algoritmo implementado, incluyendo su funcionamiento matemático, ejemplos paso a paso, vulnerabilidades conocidas y métodos de criptoanálisis.

## Algoritmos Implementados

### 1. Cifrado César

#### Descripción y Funcionamiento

El cifrado César es uno de los métodos de cifrado más antiguos y simples. Consiste en desplazar cada letra del alfabeto un número fijo de posiciones. Si el desplazamiento es 3, entonces:

- A → D
- B → E
- C → F
- ...
- X → A
- Y → B
- Z → C

**Fórmula matemática**: Para una letra P (posición en alfabeto), el cifrado C es:
```
C = (P + K) mod 26
```
Donde K es la clave (desplazamiento).

#### Ejemplo Detallado

**Texto plano**: "HOLA"
**Clave**: 3
**Proceso paso a paso**:

1. H (posición 7) → (7 + 3) mod 26 = 10 → J
2. O (posición 14) → (14 + 3) mod 26 = 17 → R
3. L (posición 11) → (11 + 3) mod 26 = 14 → O
4. A (posición 0) → (0 + 3) mod 26 = 3 → D

**Texto cifrado**: "JROD"

#### Vulnerabilidades

1. **Fuerza bruta**: Solo 25 posibilidades posibles (26 letras - 1 identidad)
2. **Análisis de frecuencia**: Mantiene exactamente el patrón de frecuencias del idioma original
3. **Patrones conocidos**: Ataques basados en palabras comunes como "EL", "LA", "DE"

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "KROD PXQGR"

**Paso 1: Análisis de frecuencia**
- Conteo de letras: K=1, R=2, O=2, D=1, P=1, X=1, Q=1, G=1
- Frecuencias relativas: R=2/8=25%, O=2/8=25%, etc.

**Paso 2: Comparación con frecuencias esperadas del español**
- En español: E=13.7%, A=11.7%, O=8.7%, S=7.9%, R=6.9%, N=6.7%, etc.
- En el texto cifrado: R y O aparecen con frecuencia similar

**Paso 3: Prueba de desplazamientos**
- Desplazamiento 3: K→H, R→O, O→L, D→A, P→M, X→U, Q→N, G→D
- Resultado: "HOLA MUNDO" ✓

#### Casos Prácticos
- Comunicación militar romana (siglo I a.C.)
- ROT13 en foros de internet modernos
- Educación básica de criptografía

---

### 2. Cifrado Vigenère

#### Descripción y Funcionamiento

El cifrado Vigenère es un método polialfabético que utiliza una clave para determinar diferentes desplazamientos para cada letra del texto. La clave se repite cíclicamente sobre el texto plano.

**Algoritmo**:
1. Repetir la clave hasta que tenga la misma longitud que el texto
2. Para cada par (letra_texto, letra_clave), aplicar desplazamiento César

**Fórmula**: Para posiciones P (texto) y K (clave):
```
C = (P + K) mod 26
```

#### Ejemplo Detallado

**Texto plano**: "ATAQUE"
**Clave**: "CLAVE"
**Proceso paso a paso**:

1. Extender clave: "CLAVE" → "CLAVEC" (se repite)
2. Procesar cada letra:

| Posición | Texto | Clave | Desplazamiento | Cifrado |
|----------|-------|-------|----------------|---------|
| 0 | A(0) | C(2) | (0+2) mod 26 = 2 | C |
| 1 | T(19) | L(11) | (19+11) mod 26 = 4 | X |
| 2 | A(0) | A(0) | (0+0) mod 26 = 0 | A |
| 3 | Q(16) | V(21) | (16+21) mod 26 = 11 | L |
| 4 | U(20) | E(4) | (20+4) mod 26 = 24 | Y |
| 5 | E(4) | C(2) | (4+2) mod 26 = 6 | G |

**Texto cifrado**: "CXALYG"

#### Vulnerabilidades

1. **Análisis de Kasiski**: Las repeticiones en el texto cifrado revelan la longitud de la clave
2. **Análisis de frecuencia por posición**: Cada posición modular tiene distribución diferente
3. **Ataque de plaintext conocido**: Si se conoce parte del texto plano, se puede deducir la clave

#### Ejemplo de Criptoanálisis (Análisis de Kasiski)

**Texto cifrado**: "KDVF KDVF ZKDVF"

**Paso 1: Buscar repeticiones**
- "KDVF" aparece en posiciones 0, 5, 10
- Distancia entre repeticiones: 5, 5
- MCD(5,5) = 5 → Longitud probable de clave: 5

**Paso 2: Dividir en grupos por posición modular**
- Posición 0: K, K, Z
- Posición 1: D, D, K
- Posición 2: V, V, D
- Posición 3: F, F, V
- Posición 4: (espacio), (espacio), F

**Paso 3: Análisis de frecuencia por grupo**
- Grupo 0: K,K,Z → Frecuencias similares a E,T,A
- Posible desplazamiento: K→E (6), K→T (7), Z→A (25)

**Paso 4: Probar hipótesis**
- Si clave comienza con "CLEVA": verificar consistencia
- Resultado: "HELLO HELLO WORLD"

#### Casos Prácticos
- Cifrado de mensajes diplomáticos en el siglo XIX
- Base para cifrados modernos como AES
- Estudio de criptoanálisis avanzado

---

### 3. Cifrado Atbash

#### Descripción y Funcionamiento

El cifrado Atbash es una sustitución monoalfabética simple que invierte el alfabeto. Es uno de los cifrados más antiguos, mencionado en la Biblia hebrea.

**Mapeo fijo**:
```
A ↔ Z    B ↔ Y    C ↔ X    D ↔ W    E ↔ V
F ↔ U    G ↔ T    H ↔ S    I ↔ R    J ↔ Q
K ↔ P    L ↔ O    M ↔ N
```

**Fórmula**: Para una letra en posición P (0-25):
```
C = 25 - P
```

#### Ejemplo Detallado

**Texto plano**: "HOLA"
**Proceso paso a paso**:

1. H (posición 7) → 25 - 7 = 18 → S
2. O (posición 14) → 25 - 14 = 11 → L
3. L (posición 11) → 25 - 11 = 14 → O
4. A (posición 0) → 25 - 0 = 25 → Z

**Texto cifrado**: "SLOZ"

#### Propiedad Especial
**Simetría**: Atbash es su propia inversa. Cifrar dos veces devuelve el texto original:
- "HOLA" → "SLOZ" → "HOLA"

#### Vulnerabilidades

1. **Simetría perfecta**: Aplicar el cifrado dos veces = texto original
2. **Frecuencias invertidas**: El patrón de frecuencias se invierte
3. **Muy débil**: Fácil de reconocer por su simetría

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "SVOOL DLIOW"

**Paso 1: Reconocimiento**
- El texto parece simétrico o invertido
- Todas las letras están en el rango A-Z

**Paso 2: Aplicar Atbash**
- S→H, V→E, O→L, O→L, L→O, D→W, L→O, I→R, O→L, W→D
- Resultado: "HELLO WORLD"

**Paso 3: Verificación**
- Aplicar Atbash nuevamente: "HELLO WORLD" → "SVOOL DLIOW" ✓

#### Casos Prácticos
- Cifrado hebreo antiguo (siglo VI a.C.)
- Ejemplo educativo de sustitución simple
- Detección automática en criptoanálisis

---

### 4. Cifrado Playfair

#### Descripción y Funcionamiento

El cifrado Playfair es un cifrado digráfico que opera sobre pares de letras usando una matriz 5x5. Fue utilizado por los británicos durante la Primera Guerra Mundial.

**Construcción de la matriz**:
1. La clave se escribe en la matriz, omitiendo letras repetidas
2. Se completan las letras restantes del alfabeto (I=J)
3. La matriz resultante es de 5x5

**Reglas de cifrado**:
1. **Misma fila**: Desplazar a la derecha
2. **Misma columna**: Desplazar hacia abajo
3. **Diferente fila/columna**: Formar rectángulo, intercambiar letras

#### Ejemplo Detallado

**Clave**: "PLAYFAIR"
**Texto plano**: "HELLO" (agregar X si impar: "HELLOX")

**Paso 1: Construir matriz**
```
P L A Y F
A I R B C
D E G H K
M N O Q S
T U V W X
```

**Paso 2: Procesar dígrafo "HE"**
- H está en (2,3), E está en (2,1)
- Misma fila: desplazar derecha: H→K, E→G
- Resultado: "KG"

**Paso 3: Procesar dígrafo "LL"**
- L está en (0,1), L está en (0,1) - misma posición
- Separar con X: "LX"

**Paso 4: Procesar dígrafo "LX"**
- L está en (0,1), X está en (4,4)
- Rectángulo: intercambiar: L↔X, X↔L
- Resultado: "XL"

**Paso 5: Procesar dígrafo "OX"**
- O está en (3,2), X está en (4,4)
- Rectángulo: intercambiar: O↔X, X↔O
- Resultado: "XO"

**Texto cifrado**: "KG XL XO"

#### Vulnerabilidades

1. **Análisis de dígrafo**: Frecuencias de pares de letras
2. **Matriz conocida**: Si se conoce la estructura, es trivial
3. **Reglas fijas**: Comportamiento predecible

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "KX JE YU RE BE"

**Paso 1: Análisis de frecuencias de dígrafo**
- KX=1, JE=1, YU=1, RE=1, BE=1
- En inglés: TH=2.8%, HE=2.3%, IN=2.1%, etc.

**Paso 2: Buscar patrones**
- "BE" podría ser "TH" (común)
- Si B→T, E→H, entonces matriz tiene T y H en misma fila/columna

**Paso 3: Reconstruir matriz**
- Asumir clave "PLAYFAIR" (conocida históricamente)
- Verificar consistencia con el texto cifrado

#### Casos Prácticos
- Comunicación militar británica durante WWI
- Cifrado manual con papel y lápiz
- Estudio de cifrados digráficos

---

### 5. Cifrado Hill

#### Descripción y Funcionamiento

El cifrado Hill es un cifrado polialfabético que utiliza álgebra lineal matricial. Fue uno de los primeros cifrados que utilizaba matrices para el cifrado.

**Funcionamiento**:
1. El texto se divide en bloques del tamaño de la matriz
2. Cada bloque se multiplica por la matriz clave
3. Los resultados se convierten de nuevo a letras

**Fórmula**: Para un vector de texto P y matriz clave K:
```
C = (K × P) mod 26
```

#### Ejemplo Detallado

**Matriz clave 2x2**: [[3, 3], [2, 5]]
**Texto plano**: "HELP"

**Paso 1: Convertir a números**
- H=7, E=4, L=11, P=15

**Paso 2: Multiplicar por matriz**
```
[3 3]   [7]   [3×7 + 3×4]   [21 + 12]   [33]   [33 mod 26]   [7]  → H
[2 5] × [4] = [2×7 + 5×4] = [14 + 20] = [34] = [34 mod 26] = [8] → I

[3 3]   [11]   [3×11 + 3×15]   [33 + 45]   [78]   [78 mod 26]   [0]  → A
[2 5] × [15] = [2×11 + 5×15] = [22 + 75] = [97] = [97 mod 26] = [19] → T
```

**Texto cifrado**: "HIAT"

#### Vulnerabilidades

1. **Análisis de frecuencias**: Para textos largos se pueden encontrar patrones
2. **Ataque de plaintext conocido**: Si se conoce suficiente texto plano
3. **Complejidad computacional**: Matrices grandes son difíciles de romper

#### Ejemplo de Criptoanálisis

**Texto plano conocido**: "HELP"
**Texto cifrado conocido**: "HIAT"
**Matriz sospechada**: 2x2

**Paso 1: Sistema de ecuaciones**
```
3a + 3b ≡ 7  mod 26  (H→H)
2a + 5b ≡ 8  mod 26  (E→I)
3a + 3c ≡ 0  mod 26  (L→A)
2a + 5c ≡ 19 mod 26 (P→T)
```

**Paso 2: Resolver sistema**
- De las ecuaciones 1 y 2: a ≡ 3, b ≡ 3
- Verificar con ecuaciones 3 y 4: ✓

**Matriz clave**: [[3, 3], [2, 5]]

#### Casos Prácticos
- Investigación académica en criptografía
- Base para cifrados modernos como AES
- Aplicaciones matemáticas y de álgebra lineal

---

### 6. Cifrado Autokey

#### Descripción y Funcionamiento

El cifrado Autokey es una variante del Vigenère donde la clave se extiende usando el propio texto plano. Esto crea una clave más larga y potencialmente más segura.

**Algoritmo**:
1. Comenzar con clave inicial
2. Extender la clave con las letras del texto plano
3. Aplicar Vigenère normal

#### Ejemplo Detallado

**Texto plano**: "HELLO"
**Clave inicial**: "KEY"

**Paso 1: Extender clave**
- Clave inicial: K E Y
- Agregar texto plano: K E Y H E L L O
- Clave final: K E Y H E L L O

**Paso 2: Aplicar Vigenère**
```
H + K = (7 + 10) mod 26 = 17 → R
E + E = (4 + 4) mod 26 = 8 → I
L + Y = (11 + 24) mod 26 = 9 → J
L + H = (11 + 7) mod 26 = 18 → S
O + E = (14 + 4) mod 26 = 18 → S
```

**Texto cifrado**: "RIJSS"

#### Vulnerabilidades

1. **Autocorrelación**: El texto plano aparece en la clave
2. **Análisis estadístico**: Propiedades del idioma se mantienen
3. **Longitud de clave**: Puede ser mayor que la clave inicial

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "RIJSS"
**Clave inicial conocida**: "KEY"

**Paso 1: Hipótesis inicial**
- Primera letra: R = H + K = (7 + 10) mod 26 = 17 ✓
- Confirma H como primera letra del texto

**Paso 2: Extender clave**
- Clave actual: K E Y H
- Segunda letra: I = E + E = (4 + 4) mod 26 = 8 ✓
- Confirma E como segunda letra

**Paso 3: Continuar proceso**
- Reconstruir todo el texto plano: "HELLO"

#### Casos Prácticos
- Variante del Vigenère para mayor seguridad
- Estudio de cifrados autorreferenciales
- Criptografía experimental

---

### 7. Cifrado XOR

#### Descripción y Funcionamiento

El cifrado XOR es un cifrado simétrico básico que utiliza la operación XOR bit a bit entre el texto y una clave repetida.

**Funcionamiento**:
1. Convertir texto y clave a valores ASCII o binarios
2. Aplicar XOR bit a bit
3. La clave se repite si es más corta que el texto

**Propiedad**: XOR es su propia inversa: A ⊕ B ⊕ B = A

#### Ejemplo Detallado

**Texto plano**: "HI" (ASCII: 72, 73)
**Clave**: "K" (ASCII: 75)

**Paso 1: Convertir a binario**
- H: 01001000
- I: 01001001
- K: 01001011

**Paso 2: Aplicar XOR**
- H ⊕ K = 01001000 ⊕ 01001011 = 00000011 = 3
- I ⊕ K = 01001001 ⊕ 01001011 = 00000010 = 2

**Texto cifrado**: Caracteres 3 y 2

#### Vulnerabilidades

1. **Clave repetida**: Patrones visibles si la clave es corta
2. **Conocimiento de texto plano**: Revela completamente la clave
3. **Análisis estadístico**: Para claves cortas

#### Ejemplo de Criptoanálisis

**Texto cifrado**: 0x4B 0x4F 0x4D 0x50
**Texto plano conocido**: "TEST"

**Paso 1: Calcular clave**
- T(0x54) ⊕ 0x4B = 0x1F
- E(0x45) ⊕ 0x4F = 0x2A → No consistente
- Posible clave diferente

**Paso 2: Probar otras claves**
- Si clave es "AB": A=0x41, B=0x42
- Verificar consistencia con todo el texto

#### Casos Prácticos
- Cifrado de archivos y comunicaciones básicas
- Base para cifrados de flujo modernos
- Introducción a criptografía simétrica

---

### 8. Transposición por Columnas

#### Descripción y Funcionamiento

La transposición por columnas reordena las letras del texto escribiéndolas en una tabla por filas y leyéndolas por columnas según una clave.

**Algoritmo**:
1. Escribir el texto en filas de ancho = longitud de clave
2. Ordenar las columnas alfabéticamente según la clave
3. Leer las columnas en el orden de la clave ordenada

#### Ejemplo Detallado

**Texto plano**: "ATAQUEALAMANECER"
**Clave**: "CLAVE"

**Paso 1: Crear tabla (5 columnas)**
```
C L A V E
---------
A T A Q U
E A L A M
A N E C E
R _ _ _ _
```

**Paso 2: Ordenar columnas alfabéticamente**
- Orden: A, C, E, L, V (posiciones 2, 0, 4, 1, 3)
- Columnas ordenadas: A, C, E, L, V

**Paso 3: Leer columnas**
- Columna A: A E A R
- Columna C: T A N _
- Columna E: U M C _
- Columna L: T L E _
- Columna V: Q A E _

**Texto cifrado**: "AEARTANUMCETLEQAE"

#### Vulnerabilidades

1. **Análisis de patrones**: Las columnas mantienen propiedades estadísticas
2. **Longitud del mensaje**: Puede revelar información sobre la tabla
3. **Clave alfabética**: El orden de las columnas es predecible

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "AEARTANUMCETLEQAE"
**Longitud clave sospechada**: 5

**Paso 1: Determinar número de filas**
- Longitud texto: 17
- Con 5 columnas: 4 filas (17/5 = 3.4, redondear arriba)

**Paso 2: Probar diferentes órdenes de columnas**
- Hipótesis: columnas ordenadas como A,C,E,L,V
- Reconstruir tabla y leer por filas

**Paso 3: Verificar resultado**
- Si produce texto con sentido: ✓

#### Casos Prácticos
- Cifrado manual simple con papel y lápiz
- Reordenamiento de datos en comunicaciones
- Estudio de técnicas de transposición

---

### 9. Rail Fence (Cifrado en Zigzag)

#### Descripción y Funcionamiento

El cifrado Rail Fence, también conocido como "cifrado en zigzag", escribe el texto en diagonales y luego lo lee por filas.

**Algoritmo**:
1. Imaginar "rieles" (líneas) horizontales
2. Escribir el texto en zigzag a través de los rieles
3. Leer cada riel de izquierda a derecha

#### Ejemplo Detallado

**Texto plano**: "ATAQUE AL AMANECER"
**Número de rieles**: 3

**Paso 1: Escribir en zigzag**
```
Riel 1: A   U   A   N   E
Riel 2:  T Q E L M N C R
Riel 3:   A   A   A   E
```

**Paso 2: Leer por rieles**
- Riel 1: A U A N E
- Riel 2: T Q E L M N C R
- Riel 3: A A A E

**Texto cifrado**: "AUANETQEALMNCRAAAE"

#### Vulnerabilidades

1. **Número de rieles**: Fácil de probar (típicamente 2-10)
2. **Patrones diagonales**: La estructura es visible
3. **Longitud del texto**: Limita las posibilidades

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "AUANETQEALMNCRAAAE"
**Número de rieles sospechado**: 3

**Paso 1: Calcular distribución**
- Para 3 rieles, el patrón se repite cada 4 caracteres
- Riel 1: posiciones 0, 3, 6, 9, 12, 15
- Riel 2: posiciones 1, 2, 5, 7, 8, 11, 13, 14
- Riel 3: posiciones 4, 10, 16

**Paso 2: Reconstruir**
- Colocar letras en sus posiciones de riel
- Leer en orden de escritura

#### Casos Prácticos
- Cifrado romano antiguo (escítala)
- Comunicación militar histórica
- Algoritmos de ruteo en redes

---

### 10. Sustitución Simple (Monoalfabética)

#### Descripción y Funcionamiento

La sustitución simple reemplaza cada letra del alfabeto por otra letra fija, creando un "alfabeto permutado".

**Algoritmo**:
1. Crear un mapeo fijo letra → letra
2. Aplicar el mapeo a cada carácter del texto
3. Mantener espacios y puntuación sin cambios

#### Ejemplo Detallado

**Alfabeto permutado** (clave "CLAVE"):
```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
C L A V E B D F G H I J K M N O P Q R S T U W X Y Z
```

**Texto plano**: "HOLA"

**Paso 1: Aplicar mapeo**
- H → S (H está en posición 7, mapeo es S)
- O → P (O está en posición 14, mapeo es P)
- L → M (L está en posición 11, mapeo es M)
- A → C (A está en posición 0, mapeo es C)

**Texto cifrado**: "SPMC"

#### Vulnerabilidades

1. **Análisis de frecuencia**: El patrón de frecuencias del idioma se mantiene
2. **Letras comunes**: E, T, A, O, I, N aparecen con frecuencia similar
3. **Patrones conocidos**: Dígrafo como "TH", "ER", "ON", "AN"

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "SPMC"

**Paso 1: Análisis de frecuencia**
- S=1, P=1, M=1, C=1 (todas frecuencia 1)
- En español: E=13.7%, A=11.7%, O=8.7%, etc.

**Paso 2: Hipótesis sobre letras comunes**
- Asumir S=E (más común), P=A, M=O, C=S
- Verificar consistencia

**Paso 3: Probar con texto más largo**
- Necesario más contexto para confirmar

#### Casos Prácticos
- Cifrado básico para educación
- Sustitución manual en juegos
- Análisis de frecuencias en lingüística

---

### 11. Permutación General

#### Descripción y Funcionamiento

La permutación general es una transposición más flexible que permite cualquier reordenamiento basado en una clave numérica o alfabética.

**Algoritmo**:
1. Dividir el texto en bloques del tamaño de la clave
2. Para cada bloque, reordenar según la clave
3. Concatenar los bloques resultantes

#### Ejemplo Detallado

**Texto plano**: "ATAQUEAL"
**Clave**: "CLAVE" (orden alfabético: A=2, C=0, E=4, L=1, V=3)

**Paso 1: Dividir en bloques de 5**
- Bloque 1: "ATAQU"
- Bloque 2: "EAL" (rellenar si necesario)

**Paso 2: Reordenar bloque 1**
- Orden: A, C, E, L, V → posiciones 2, 0, 4, 1, 3
- A T A Q U → A(2), T(0), A(4), Q(1), U(3)
- Resultado: "T Q U A A"

**Texto cifrado**: "TQUAA"

#### Vulnerabilidades

1. **Clave determina orden**: Si se conoce el método de ordenamiento
2. **Patrones repetitivos**: Para textos largos con clave corta
3. **Análisis estadístico**: Propiedades del idioma se mantienen

#### Ejemplo de Criptoanálisis

**Texto cifrado**: "TQUAA"
**Clave sospechada**: "CLAVE"

**Paso 1: Determinar tamaño de bloque**
- Probar diferentes tamaños de bloque
- Para tamaño 5: "TQUAA"

**Paso 2: Hipótesis de orden**
- Si orden es A,C,E,L,V → posiciones 2,0,4,1,3
- Inverso: posición 0→2, 1→0, 2→4, 3→1, 4→3

**Paso 3: Despermutar**
- T(0)→A(2), Q(1)→T(0), U(2)→A(4), A(3)→Q(1), A(4)→U(3)
- Resultado: "ATAQU"

#### Casos Prácticos
- Generalización de técnicas de transposición
- Algoritmos de mezcla de datos
- Investigación teórica en criptografía

## Análisis Comparativo

### Fortaleza Relativa
1. **Más fuerte**: Hill, Vigenère (con clave larga), Playfair
2. **Moderada**: Autokey, XOR (con clave buena), Permutación
3. **Débil**: César, Atbash, Sustitución simple
4. **Muy débil**: Rail Fence, Transposición simple

### Facilidad de Implementación
1. **Muy fácil**: César, Atbash, XOR
2. **Fácil**: Sustitución simple, Rail Fence, Transposición
3. **Moderada**: Vigenère, Autokey, Permutación
4. **Difícil**: Playfair, Hill

### Uso Educativo
- **Principiantes**: César, Atbash, Sustitución simple
- **Intermedios**: Vigenère, Rail Fence, Transposición
- **Avanzados**: Playfair, Hill, Autokey

## Conclusiones

Esta librería proporciona una base sólida para el estudio de criptografía clásica. Cada algoritmo ilustra conceptos fundamentales:

- **Sustitución**: Cambio de símbolos (César, Atbash, Sustitución simple)
- **Transposición**: Reordenamiento (Rail Fence, Columnas, Permutación)
- **Polialfabético**: Múltiples alfabetos (Vigenère, Autokey, Hill)
- **Matricial**: Álgebra lineal (Hill)
- **Digráfico**: Pares de letras (Playfair)
- **Simétrico básico**: XOR bit a bit

Los ejemplos de ruptura demuestran por qué estos métodos han sido reemplazados por criptografía moderna basada en teoría de números, curvas elípticas y protocolos de clave pública.

## Recomendaciones

1. **Educación**: Usar para enseñar conceptos básicos de criptografía
2. **Investigación**: Estudiar evolución histórica de la criptografía
3. **No usar en producción**: Todos son vulnerables a ataques computacionales modernos
4. **Extensión**: Base para implementar cifrados híbridos modernos

---

*Este informe ampliado fue generado como parte del Proyecto 1 de Desarrollo de Librerías de Cifrado Clásico.*