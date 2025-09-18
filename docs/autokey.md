# Cifrado Autokey

## Descripción

El cifrado Autokey es una variante del Vigenère donde la clave se extiende automáticamente usando el texto plano mismo. Esto hace que sea más resistente a ataques de frecuencia que el Vigenère estándar.

## Lógica de Funcionamiento

### Cifrado
1. Se tiene una clave inicial K
2. Para el mensaje M = m1 m2 ... mn:
   - La clave extendida comienza con K
   - Para cada mi, se cifra usando el siguiente carácter de la clave extendida
   - Después de cifrar mi, se añade mi a la clave extendida

### Descifrado
- Se reconstruye la clave extendida usando los caracteres descifrados

## Ejemplo

**Mensaje:** "ATAQUE"  
**Clave inicial:** "CLAVE"  

Clave extendida inicial: "CLAVE"  

Cifrado:
- A (0) + C (2) = 2 → C, clave extendida: "CLAVEA"
- T (19) + L (11) = 3 → D, clave extendida: "CLAVEAD"
- A (0) + A (0) = 0 → A, clave extendida: "CLAVEADA"
- Q (16) + V (21) = 11 → L, clave extendida: "CLAVEADAL"
- U (20) + E (4) = 24 → Y, clave extendida: "CLAVEADALY"
- E (4) + C (2) = 6 → G, clave extendida: "CLAVEADALYG"

**Texto cifrado:** "CDALYG"

## Ventajas sobre Vigenère

- La clave crece con el mensaje
- Más difícil de romper por análisis de frecuencia
- No hay repetición periódica de la clave

## Vulnerabilidades

- Si se conoce el inicio del mensaje, se puede reconstruir la clave
- Análisis de Kasiski aún puede determinar la longitud de la clave inicial
- Más seguro que Vigenère pero aún criptoanalizable

## Implementación en Código

```python
class CifradoAutokey:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = limpiar_texto(clave)

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        resultado = ""
        clave_extendida = self.clave
        indice_clave = 0

        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_texto + indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                clave_extendida += c  # Agregar el carácter original
                indice_clave += 1
            else:
                resultado += c
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        texto_limpio = limpiar_texto(texto_cifrado)
        resultado = ""
        clave_extendida = self.clave
        indice_clave = 0

        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_cifrado = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_cifrado - indice_clave_actual) % self.alfabeto.obtener_longitud()
                caracter_original = self.alfabeto.obtener_caracter(nuevo_indice)
                resultado += caracter_original
                clave_extendida += caracter_original  # Agregar el carácter descifrado
                indice_clave += 1
            else:
                resultado += c
        return resultado
```