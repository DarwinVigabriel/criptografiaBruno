# Cifrado César

## Descripción

El cifrado César es uno de los métodos de cifrado más antiguos y simples. Fue utilizado por Julio César para comunicaciones secretas. Consiste en desplazar cada letra del alfabeto un número fijo de posiciones hacia adelante o hacia atrás.

## Lógica de Funcionamiento

### Cifrado
Para cifrar un mensaje con un desplazamiento `d`:
1. Para cada carácter `c` en el mensaje:
   - Si `c` es una letra del alfabeto, encontrar su índice `i` (A=0, B=1, ..., Z=25)
   - Calcular el nuevo índice: `nuevo_i = (i + d) mod 26`
   - Obtener la nueva letra correspondiente al índice `nuevo_i`
   - Si `c` no es una letra, mantenerlo sin cambios

### Descifrado
Para descifrar, se realiza el proceso inverso:
- `nuevo_i = (i - d) mod 26`

### Ataque de Fuerza Bruta
Dado que solo hay 25 desplazamientos posibles (1-25, ya que 0 no cambia nada), se puede probar cada uno hasta encontrar el mensaje legible.

## Ejemplo

**Mensaje original:** "HOLA MUNDO"  
**Desplazamiento:** 3  

Proceso de cifrado:
- H (índice 7) → (7 + 3) mod 26 = 10 → K
- O (14) → (14 + 3) mod 26 = 17 → R
- L (11) → (11 + 3) mod 26 = 14 → O
- A (0) → (0 + 3) mod 26 = 3 → D
- Espacio → Espacio
- M (12) → (12 + 3) mod 26 = 15 → P
- U (20) → (20 + 3) mod 26 = 23 → X
- N (13) → (13 + 3) mod 26 = 16 → Q
- D (3) → (3 + 3) mod 26 = 6 → G
- O (14) → (14 + 3) mod 26 = 17 → R

**Texto cifrado:** "KROD PXQG R"

## Vulnerabilidades

- Muy vulnerable a ataques de fuerza bruta (solo 25 posibilidades)
- Patrón de frecuencia de letras se mantiene
- No oculta la estructura del lenguaje

## Implementación en Código

```python
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
        resultado = ""
        desplazamiento_inverso = self.alfabeto.obtener_longitud() - self.desplazamiento
        for c in texto_cifrado:
            indice = self.alfabeto.obtener_indice(c)
            if indice != -1:
                nuevo_indice = (indice + desplazamiento_inverso) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c
        return resultado
```