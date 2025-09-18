# Cifrado Rail Fence (Zigzag)

## Descripción

El cifrado Rail Fence, también conocido como zigzag, escribe el texto en diagonales imaginarias (rieles) y luego lee las líneas en orden. Es un tipo de transposición.

## Lógica de Funcionamiento

### Cifrado
1. Se imagina un número de "rieles" (líneas diagonales)
2. Se escribe el texto zigzagueando entre los rieles
3. Se lee cada riel de arriba abajo

### Descifrado
- Calcular cuántos caracteres van en cada riel
- Distribuir el texto cifrado en los rieles
- Leer zigzagueando

## Ejemplo

**Mensaje:** "ATAQUE AL AMANECER"  
**Rieles:** 3  

Escritura zigzag:
```
A   A   A   A   E
 T Q E L M N C R
  A   A   M   E
```

Riel 1: A A A A E  
Riel 2: T Q E L M N C R  
Riel 3: A A M E  

Concatenado: "AAAAETQELMNCRAAE"

**Texto cifrado:** "AAAAETQELMNCRAAE"

## Ventajas

- Simple de implementar
- Rompe secuencias lineales

## Vulnerabilidades

- Fácil de detectar patrones
- Solo depende del número de rieles
- Análisis visual puede revelar el patrón

## Implementación en Código

```python
class CifradoRailFence:
    def __init__(self, rieles: int, relleno: str = 'X', alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.rieles = rieles
        self.relleno = relleno

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        if len(texto_limpio) % (2 * (self.rieles - 1)) != 0:
            ciclo = 2 * (self.rieles - 1)
            faltante = (ciclo - (len(texto_limpio) % ciclo)) % ciclo
            texto_limpio += self.relleno * faltante

        rieles = [[] for _ in range(self.rieles)]
        fila = 0
        direccion = 1

        for letra in texto_limpio:
            rieles[fila].append(letra)
            fila += direccion
            if fila == 0 or fila == self.rieles - 1:
                direccion *= -1

        resultado = ""
        for riel in rieles:
            resultado += "".join(riel)
        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        texto_limpio = limpiar_texto(texto_cifrado)
        ciclo = 2 * (self.rieles - 1)
        len_total = len(texto_limpio)
        q, r = divmod(len_total, ciclo)

        longitudes = [0] * self.rieles
        for i in range(self.rieles):
            if i == 0 or i == self.rieles - 1:
                longitudes[i] = q
            else:
                longitudes[i] = 2 * q

        for i in range(r):
            if i < self.rieles:
                longitudes[i] += 1
            else:
                longitudes[2 * (self.rieles - 1) - i] += 1

        rieles_separados = []
        inicio = 0
        for l in longitudes:
            rieles_separados.append(texto_limpio[inicio:inicio + l])
            inicio += l

        resultado = []
        indices = [0] * self.rieles
        fila = 0
        direccion = 1

        for _ in range(len(texto_limpio)):
            resultado.append(rieles_separados[fila][indices[fila]])
            indices[fila] += 1
            fila += direccion
            if fila == 0 or fila == self.rieles - 1:
                direccion *= -1

        return "".join(resultado)
```