# Cifrado Vigenère

## Descripción

El cifrado Vigenère es un método de cifrado polialfabético que utiliza una palabra clave para determinar diferentes desplazamientos César para cada letra del mensaje. Es más seguro que el César simple porque rompe los patrones de frecuencia.

## Lógica de Funcionamiento

### Cifrado
1. Se tiene una clave `K = k1 k2 ... kn`
2. Para el mensaje `M = m1 m2 ... mm`:
   - Se extiende la clave para que coincida con la longitud del mensaje: `K' = k1 k2 ... kn k1 k2 ...`
   - Para cada posición `i`: `c_i = (m_i + k'_i) mod 26`

### Descifrado
- `m_i = (c_i - k'_i) mod 26`

### Ataque por Análisis de Frecuencia
Más complejo que el César, requiere determinar la longitud de la clave primero (usando índices de coincidencia o análisis de Kasiski), luego tratar cada grupo como un César separado.

## Ejemplo

**Mensaje:** "ATAQUE AL AMANECER"  
**Clave:** "CLAVE"  

Primero, limpiar el mensaje: "ATAQUEALAMANECER"  
Extender clave: "CLAVEC LAVEC LAVEC L" (se repite hasta cubrir el mensaje)

Proceso:
- A (0) + C (2) = (0+2) mod 26 = 2 → C
- T (19) + L (11) = (19+11) mod 26 = 4 → E
- A (0) + A (0) = (0+0) mod 26 = 0 → A
- Q (16) + V (21) = (16+21) mod 26 = 11 → L
- U (20) + E (4) = (20+4) mod 26 = 24 → Y
- E (4) + C (2) = (4+2) mod 26 = 6 → G
- A (0) + L (11) = (0+11) mod 26 = 11 → L
- L (11) + A (0) = (11+0) mod 26 = 11 → L
- A (0) + V (21) = (0+21) mod 26 = 21 → V
- M (12) + E (4) = (12+4) mod 26 = 16 → Q
- A (0) + C (2) = (0+2) mod 26 = 2 → C
- N (13) + L (11) = (13+11) mod 26 = 24 → Y
- E (4) + A (0) = (4+0) mod 26 = 4 → E
- C (2) + V (21) = (2+21) mod 26 = 23 → X
- E (4) + E (4) = (4+4) mod 26 = 8 → I
- R (17) + C (2) = (17+2) mod 26 = 19 → T

**Texto cifrado:** "CEALYGLLVQCYEXIT"

## Vulnerabilidades

- Vulnerable si se conoce la longitud de la clave
- Análisis de Kasiski puede determinar la longitud
- Una vez conocida la longitud, cada subtexto es un César

## Implementación en Código

```python
class CifradoVigenere:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = limpiar_texto(clave)

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        resultado = ""
        clave_extendida = ""
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1

        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_texto = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_texto + indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        # Similar pero restando
        texto_limpio = limpiar_texto(texto_cifrado)
        resultado = ""
        clave_extendida = ""
        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1

        indice_clave = 0
        for c in texto_limpio:
            if self.alfabeto.contiene_caracter(c):
                indice_cifrado = self.alfabeto.obtener_indice(c)
                indice_clave_actual = self.alfabeto.obtener_indice(clave_extendida[indice_clave])
                nuevo_indice = (indice_cifrado - indice_clave_actual) % self.alfabeto.obtener_longitud()
                resultado += self.alfabeto.obtener_caracter(nuevo_indice)
                indice_clave += 1
            else:
                resultado += c
        return resultado
```