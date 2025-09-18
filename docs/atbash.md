# Cifrado Atbash

## Descripción

El cifrado Atbash es un cifrado de sustitución monoalfabética simple donde cada letra se reemplaza por su "opuesta" en el alfabeto. Es simétrico, lo que significa que la misma operación sirve para cifrar y descifrar.

## Lógica de Funcionamiento

### Cifrado/Descifrado
Para un alfabeto de 26 letras (A-Z):
- A ↔ Z
- B ↔ Y
- C ↔ X
- ...
- M ↔ N

La fórmula general es:
`nueva_letra = alfabeto[longitud - 1 - indice_actual]`

Donde `indice_actual` es la posición de la letra en el alfabeto (0 para A, 1 para B, etc.).

## Ejemplo

**Mensaje:** "HOLA MUNDO"  

Proceso:
- H (índice 7) → alfabeto[25 - 7] = alfabeto[18] → S
- O (14) → alfabeto[25 - 14] = alfabeto[11] → L
- L (11) → alfabeto[25 - 11] = alfabeto[14] → O
- A (0) → alfabeto[25 - 0] = alfabeto[25] → Z
- Espacio → Espacio
- M (12) → alfabeto[25 - 12] = alfabeto[13] → N
- U (20) → alfabeto[25 - 20] = alfabeto[5] → F
- N (13) → alfabeto[25 - 13] = alfabeto[12] → M
- D (3) → alfabeto[25 - 3] = alfabeto[22] → W
- O (14) → alfabeto[25 - 14] = alfabeto[11] → L
- Espacio → Espacio
- N (13) → alfabeto[25 - 13] = alfabeto[12] → M
- D (3) → alfabeto[25 - 3] = alfabeto[22] → W
- O (14) → alfabeto[25 - 14] = alfabeto[11] → L

**Texto cifrado:** "SLOZ NFLMW MLW"

## Características

- **Simétrico:** El mismo algoritmo sirve para cifrar y descifrar
- **Fijo:** No requiere clave, siempre funciona igual
- **Simple:** Muy fácil de implementar y recordar

## Vulnerabilidades

- Extremadamente vulnerable (solo una posibilidad)
- Patrón de frecuencia se invierte pero se mantiene
- Fácil de detectar y romper

## Implementación en Código

```python
class CifradoAtbash:
    def __init__(self, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()

    def cifrar(self, texto_plano: str) -> str:
        resultado = ""
        for c in texto_plano:
            indice = self.alfabeto.obtener_indice(c)
            if indice != -1:
                nuevo_indice = self.alfabeto.obtener_longitud() - 1 - indice
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
            else:
                resultado += c
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        # Atbash es simétrico
        return self.cifrar(texto_cifrado)
```