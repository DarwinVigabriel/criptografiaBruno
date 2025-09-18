# Cifrado Playfair

## Descripción

El cifrado Playfair es un cifrado digráfico que utiliza una matriz 5x5 generada a partir de una clave. Fue utilizado por los británicos en la Primera Guerra Mundial. Procesa el texto en pares de letras (dígrafos).

## Lógica de Funcionamiento

### Construcción de la Matriz
1. Se crea una matriz 5x5 con la clave (sin duplicados) seguida de las letras restantes del alfabeto
2. Se omite J o se combina con I

### Preparación del Texto
1. Se limpia el texto
2. Se divide en dígrafos
3. Si un dígrafo tiene letras repetidas, se inserta X entre ellas
4. Si queda un carácter solo, se añade X

### Reglas de Cifrado
Para cada dígrafo (f1,c1) y (f2,c2):
- **Misma fila:** Se desplaza a la derecha: (f1, c1+1), (f2, c2+1)
- **Misma columna:** Se desplaza abajo: (f1+1, c1), (f2+1, c2)
- **Rectángulo:** Se intercambian columnas: (f1, c2), (f2, c1)

### Descifrado
Reglas inversas:
- Misma fila: desplazar izquierda
- Misma columna: desplazar arriba
- Rectángulo: mismo intercambio

## Ejemplo

**Mensaje:** "HOLA MUNDO"  
**Clave:** "CLAVE"  

Matriz generada:
```
C L A V E
B D F G H
I K M N O
P Q R S T
U W X Y Z
```

Preparación: "HO LA MU ND OX" (agregado X al final)

Cifrado:
- HO: H(1,4), O(2,4) → misma columna → I(2,4), U(3,4) → IU
- LA: L(0,1), A(0,2) → misma fila → A(0,2), V(0,3) → AV
- MU: M(2,2), U(4,0) → rectángulo → X(4,2), K(2,0) → XK
- ND: N(2,3), D(1,1) → rectángulo → F(1,3), L(2,1) → FL
- OX: O(2,4), X(4,2) → rectángulo → Y(4,4), M(2,2) → YM

**Texto cifrado:** "IUAVXKFLYM"

## Vulnerabilidades

- Requiere conocer la clave para reconstruir la matriz
- Vulnerable a análisis de frecuencia de dígrafos
- Más seguro que métodos monoalfabéticos

## Implementación en Código

```python
class CifradoPlayfair:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = limpiar_texto(clave)
        self.matriz = self._construir_matriz()

    def _construir_matriz(self) -> List[List[str]]:
        matriz = [['' for _ in range(5)] for _ in range(5)]
        usados = set()
        clave_limpia = ""
        for c in self.clave:
            if self.alfabeto.contiene_caracter(c) and c not in usados:
                usados.add(c)
                clave_limpia += c

        for i in range(self.alfabeto.obtener_longitud()):
            c = self.alfabeto.obtener_caracter(i)
            if c not in usados:
                clave_limpia += c
                usados.add(c)

        indice = 0
        for fila in range(5):
            for col in range(5):
                if indice < len(clave_limpia):
                    matriz[fila][col] = clave_limpia[indice]
                    indice += 1
        return matriz

    def _preparar_texto(self, texto: str) -> str:
        texto_limpio = limpiar_texto(texto)
        preparado = ""
        i = 0
        while i < len(texto_limpio):
            c1 = texto_limpio[i]
            i += 1
            c2 = texto_limpio[i] if i < len(texto_limpio) else 'X'
            preparado += c1
            if c1 == c2:
                preparado += 'X'
                i -= 1
            else:
                preparado += c2
                i += 1
        if len(preparado) % 2 != 0:
            preparado += 'X'
        return preparado

    def cifrar(self, texto_plano: str) -> str:
        preparado = self._preparar_texto(texto_plano)
        resultado = ""
        for i in range(0, len(preparado), 2):
            digrafo = preparado[i:i+2]
            resultado += self._cifrar_digrafo(digrafo)
        return resultado

    def _cifrar_digrafo(self, digrafo: str) -> str:
        f1, c1 = self._encontrar_posicion(digrafo[0])
        f2, c2 = self._encontrar_posicion(digrafo[1])
        if f1 == f2:
            return self.matriz[f1][(c1 + 1) % 5] + self.matriz[f2][(c2 + 1) % 5]
        elif c1 == c2:
            return self.matriz[(f1 + 1) % 5][c1] + self.matriz[(f2 + 1) % 5][c2]
        else:
            return self.matriz[f1][c2] + self.matriz[f2][c1]
```