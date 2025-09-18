# Cifrado XOR

## Descripción

El cifrado XOR (OR exclusivo) es un cifrado simétrico simple que utiliza la operación XOR bit a bit entre el texto plano y una clave. Es ampliamente utilizado en criptografía moderna como componente básico de muchos algoritmos.

## Lógica de Funcionamiento

### Cifrado/Descifrado
Dado que XOR es su propia inversa, el mismo algoritmo sirve para cifrar y descifrar.

Para cada carácter:
- Convertir carácter del mensaje a su valor ASCII/índice
- Convertir carácter de la clave a su valor ASCII
- Aplicar XOR: `resultado = mensaje XOR clave`
- Convertir resultado de vuelta a carácter

La clave se repite cíclicamente si es más corta que el mensaje.

## Ejemplo

**Mensaje:** "HOLA" (ASCII: 72, 79, 76, 65)  
**Clave:** "AB" (ASCII: 65, 66)  

Proceso:
- H (72) XOR A (65) = 72 ⊕ 65 = 9 → '\t' (tab)
- O (79) XOR B (66) = 79 ⊕ 66 = 109 → 'm'
- L (76) XOR A (65) = 76 ⊕ 65 = 9 → '\t'
- A (65) XOR B (66) = 65 ⊕ 66 = 3 → '\x03'

**Texto cifrado:** "\tm\t\x03"

## Características

- **Simétrico:** Misma operación para cifrar y descifrar
- **Rápido:** Operación bit a bit muy eficiente
- **Reversible:** XOR con la misma clave recupera el original

## Vulnerabilidades

- Vulnerable si la clave se repite (ataque de frecuencia)
- Si se conoce parte del plaintext, se puede recuperar la clave
- No proporciona integridad ni autenticación

## Usos Modernos

- Componente básico de algoritmos como AES
- One-time pad (con clave aleatoria del mismo tamaño)
- Encriptación de streams

## Implementación en Código

```python
class CifradoXOR:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = clave

    def cifrar(self, texto_plano: str) -> str:
        resultado = ""
        indice_clave = 0

        for c in texto_plano:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = ord(self.clave[indice_clave % len(self.clave)])
                nuevo_indice = indice_texto ^ indice_clave_actual
                nuevo_indice %= self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        # XOR es simétrico
        return self.cifrar(texto_cifrado)
```