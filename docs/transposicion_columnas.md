# Cifrado por Transposición de Columnas

## Descripción

El cifrado por transposición de columnas reorganiza el texto escribiéndolo en una matriz por filas y leyéndolo por columnas en un orden determinado por una clave.

## Lógica de Funcionamiento

### Cifrado
1. Escribir el mensaje en una matriz con tantas columnas como letras tenga la clave
2. Rellenar con caracteres de relleno si es necesario
3. Ordenar las columnas según el orden alfabético de la clave
4. Leer las columnas en el orden de la clave permutada

### Descifrado
- Reconstruir la matriz cifrada
- Reordenar las columnas a su posición original
- Leer por filas

## Ejemplo

**Mensaje:** "ATAQUE AL AMANECER"  
**Clave:** "CLAVE" (orden: C=2, L=4, A=0, V=5, E=1)  

Matriz (relleno con X):
```
A T A Q U
E A L A M
A N E C E
R X X X X
```

Orden de columnas: A(0), E(1), C(2), L(4), V(5) → posiciones 2,4,0,1,3

Lectura por columnas en orden: Col2, Col4, Col0, Col1, Col3

**Texto cifrado:** "AEAQX TAAUE LMRNX AECEX"

## Ventajas

- Rompe la estructura del lenguaje
- Más difícil de analizar por frecuencia que sustituciones

## Vulnerabilidades

- Columnas mantienen frecuencias verticales
- Si se conoce la clave, trivial de romper
- Análisis de frecuencia en columnas puede ayudar

## Implementación en Código

```python
class CifradoTransposicionColumnas:
    def __init__(self, clave: str, relleno: str = 'X', alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = limpiar_texto(clave)
        self.relleno = relleno
        self.orden_columnas = ordenar_columnas(self.clave)

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        num_columnas = len(self.clave)
        faltante = (num_columnas - (len(texto_limpio) % num_columnas)) % num_columnas
        texto_relleno = texto_limpio + self.relleno * faltante

        num_filas = len(texto_relleno) // num_columnas
        matriz = []
        for i in range(0, len(texto_relleno), num_columnas):
            fila = texto_relleno[i:i + num_columnas]
            matriz.append(fila)

        matriz_ordenada = []
        for fila in matriz:
            fila_ordenada = [fila[i] for i in self.orden_columnas]
            matriz_ordenada.append(fila_ordenada)

        resultado = ""
        for col in range(num_columnas):
            for fila in matriz_ordenada:
                resultado += fila[col]
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        texto_limpio = limpiar_texto(texto_cifrado)
        num_columnas = len(self.clave)
        len_cifrado = len(texto_limpio)
        num_filas = len_cifrado // num_columnas

        matriz_cifrada = []
        for i in range(0, len_cifrado, num_filas):
            columna = texto_cifrado[i:i + num_filas]
            matriz_cifrada.append(columna)

        matriz_original = [None] * num_columnas
        for pos_original, pos_cifrada in enumerate(self.orden_columnas):
            matriz_original[pos_cifrada] = matriz_cifrada[pos_original]

        resultado = ""
        for fila in range(num_filas):
            for col in range(num_columnas):
                resultado += matriz_original[col][fila]

        if self.relleno:
            resultado = resultado.rstrip(self.relleno)
        return resultado
```