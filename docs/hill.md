# Cifrado Hill

## Descripción

El cifrado Hill es un cifrado poligráfico que utiliza álgebra lineal. Fue inventado por Lester S. Hill en 1929. Utiliza una matriz clave para transformar bloques de texto mediante multiplicación matricial.

## Lógica de Funcionamiento

### Cifrado
1. Se divide el texto en bloques del tamaño de la matriz (n x n)
2. Cada bloque se convierte en un vector de números (A=0, B=1, ..., Z=25)
3. Se multiplica el vector por la matriz clave módulo 26
4. Se convierte el resultado de vuelta a letras

### Descifrado
- Se multiplica por la matriz inversa módulo 26

### Requisitos de la Matriz Clave
- Debe ser cuadrada
- Debe ser invertible módulo 26 (determinante coprimo con 26)

## Ejemplo

**Mensaje:** "HOLA MUNDO"  
**Matriz clave 2x2:** [[3, 3], [2, 5]]  

Texto limpio: "HOLAMUNDO" (10 caracteres)  
Bloques: "HO", "LA", "MU", "ND", "O" → agregar relleno "OX"

Convertir a números:
- H=7, O=14 → [7, 14]
- L=11, A=0 → [11, 0]
- M=12, U=20 → [12, 20]
- N=13, D=3 → [13, 3]
- O=14, X=23 → [14, 23]

Multiplicar cada vector por la matriz:
Para [7, 14]:
```
[3, 3]   [7]   [3*7 + 3*14]   [21 + 42]   [63] mod 26 = [11] → L
[2, 5] * [14] = [2*7 + 5*14] = [14 + 70] = [84] mod 26 = [6] → G
```

Resultado: "LG" + ... (continuar para otros bloques)

## Vulnerabilidades

- Vulnerable si se conocen suficientes plaintext-ciphertext
- Análisis de frecuencias en bloques
- Requiere matriz invertible

## Implementación en Código

```python
class CifradoHill:
    def __init__(self, tam_grupo: int, matriz_clave: List[List[int]], relleno: str = 'X', alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.tam_grupo = tam_grupo
        self.relleno = relleno
        self.matriz_clave = np.array(matriz_clave)
        self.matriz_inversa = self._calcular_matriz_inversa()

    def _calcular_matriz_inversa(self) -> np.ndarray:
        det = int(round(np.linalg.det(self.matriz_clave)))
        det_inv = pow(det, -1, self.alfabeto.obtener_longitud())
        matriz_adj = np.round(det * np.linalg.inv(self.matriz_clave)).astype(int)
        return (det_inv * matriz_adj) % self.alfabeto.obtener_longitud()

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        if len(texto_limpio) % self.tam_grupo != 0:
            texto_limpio += self.relleno * (self.tam_grupo - (len(texto_limpio) % self.tam_grupo))

        numeros = [self.alfabeto.obtener_indice(c) for c in texto_limpio]
        grupos = [numeros[i:i + self.tam_grupo] for i in range(0, len(numeros), self.tam_grupo)]

        resultado = ""
        for grupo in grupos:
            grupo_vector = np.array(grupo).reshape((self.tam_grupo, 1))
            cifrado_grupo = np.dot(self.matriz_clave, grupo_vector) % self.alfabeto.obtener_longitud()
            for num in cifrado_grupo.flatten():
                resultado += self.alfabeto.obtener_caracter(int(num))
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        # Similar pero usando matriz_inversa
        texto_limpio = limpiar_texto(texto_cifrado)
        numeros = [self.alfabeto.obtener_indice(c) for c in texto_limpio]
        grupos = [numeros[i:i + self.tam_grupo] for i in range(0, len(numeros), self.tam_grupo)]

        resultado = ""
        for grupo in grupos:
            grupo_vector = np.array(grupo).reshape((self.tam_grupo, 1))
            descifrado_grupo = np.dot(self.matriz_inversa, grupo_vector) % self.alfabeto.obtener_longitud()
            for num in descifrado_grupo.flatten():
                resultado += self.alfabeto.obtener_caracter(int(num))
        return resultado
```