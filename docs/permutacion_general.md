# Cifrado de Permutación General

## Descripción

El cifrado de permutación general reorganiza los caracteres del mensaje según un orden determinado por una clave. Es una forma generalizada de transposición.

## Lógica de Funcionamiento

### Métodos de Orden
- **Alfabético:** Ordena las letras de la clave alfabéticamente
- **Numérico:** Trata la clave como números

### Cifrado
1. Dividir el texto en bloques del tamaño de la clave
2. Para cada bloque, reordenar según la permutación
3. Concatenar los bloques permutados

### Descifrado
- Aplicar la permutación inversa

## Ejemplo

**Mensaje:** "ATAQUEALAMANECER"  
**Clave:** "CLAVE"  
**Método:** Alfabético  

Orden de permutación: C(2), L(4), A(0), V(5), E(1) → [2,4,0,1,3]

Bloques de 5:
- "ATAQU" → reordenar: pos2=A, pos4=U, pos0=A, pos1=T, pos3=Q → "AUATQ"
- "EALAM" → "MAAEA"
- "ANECE" → "EACEN"
- "R" → no permutar

**Texto cifrado:** "AUATQMAAEAEACENR"

## Características

- Flexible según la clave
- Puede usar diferentes métodos de ordenamiento
- Generalización de otros cifrados de transposición

## Implementación en Código

```python
class CifradoPermutacionGeneral:
    def __init__(self, clave: str, metodo: str = "alfabetico"):
        self.clave = clave.upper()
        self.metodo = metodo
        self.orden_permutacion = self._calcular_orden_permutacion()

    def _calcular_orden_permutacion(self) -> List[int]:
        if self.metodo == "numerico":
            try:
                indices = [int(c) - 1 for c in self.clave if c.isdigit()]
                if len(indices) < len(self.clave):
                    indices_alfabetico = ordenar_columnas(self.clave)
                    indices.extend(indices_alfabetico[len(indices):])
                return indices[:len(self.clave)]
            except ValueError:
                return ordenar_columnas(self.clave)
        else:
            return ordenar_columnas(self.clave)

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)

        if len(texto_limpio) < len(self.clave):
            return texto_limpio

        bloques_cifrados = []

        for i in range(0, len(texto_limpio), len(self.clave)):
            bloque = texto_limpio[i:i + len(self.clave)]

            if len(bloque) < len(self.clave):
                bloques_cifrados.append(bloque)
                continue

            bloque_permutado = [''] * len(bloque)
            for j, pos in enumerate(self.orden_permutacion):
                if j < len(bloque):
                    bloque_permutado[pos] = bloque[j]

            bloques_cifrados.append(''.join(bloque_permutado))

        return ''.join(bloques_cifrados)

    def descifrar(self, texto_cifrado: str) -> str:
        texto_limpio = limpiar_texto(texto_cifrado)

        if len(texto_limpio) < len(self.clave):
            return texto_limpio

        bloques_descifrados = []

        for i in range(0, len(texto_limpio), len(self.clave)):
            bloque = texto_limpio[i:i + len(self.clave)]

            if len(bloque) < len(self.clave):
                bloques_descifrados.append(bloque)
                continue

            bloque_original = [''] * len(bloque)
            for j, pos in enumerate(self.orden_permutacion):
                if j < len(bloque):
                    bloque_original[j] = bloque[pos]

            bloques_descifrados.append(''.join(bloque_original))

        return ''.join(bloques_descifrados)
```