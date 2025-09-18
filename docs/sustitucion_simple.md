# Cifrado de Sustitución Simple (Monoalfabética)

## Descripción

El cifrado de sustitución simple reemplaza cada letra del alfabeto por otra letra fija, creando un alfabeto permutado. A diferencia del César, cualquier permutación es posible, no solo desplazamientos.

## Lógica de Funcionamiento

### Creación del Alfabeto Permutado
1. Si se proporciona una clave, se usa para crear la permutación:
   - La clave se limpia de duplicados
   - Se añade al principio del alfabeto
   - Se completan las letras restantes en orden
2. Si no hay clave, se usa una rotación simple

### Cifrado
Cada letra del mensaje se reemplaza según el mapeo creado.

### Descifrado
Se usa el mapeo inverso.

## Ejemplo

**Mensaje:** "ATAQUE AL AMANECER"  
**Clave:** "CLAVE"  

Alfabeto original: ABCDEFGHIJKLMNOPQRSTUVWXYZ  
Clave limpia (sin duplicados): CLAVE  
Letras restantes: BDFGHIJKLMNOPQRS TUWXYZ  
Alfabeto permutado: CLAVEBDFGHIJKLMNOPQRS TUWXYZ  

Mapeo:
- A → C
- B → L
- C → A
- D → V
- E → E
- F → B
- etc.

Proceso de cifrado:
- A → C
- T → T (pos 19 → pos 19 en permutado)
- A → C
- Q → Q
- U → U
- E → E
- Espacio → Espacio
- A → C
- L → L
- Espacio → Espacio
- A → C
- M → M
- A → C
- N → N
- E → E
- C → A
- E → E
- R → R

**Texto cifrado:** "CTCQUE CL CMCNAEAER"

## Vulnerabilidades

- Patrón de frecuencia de letras se mantiene
- Análisis de frecuencia puede romperlo
- Más seguro que César pero aún vulnerable

## Implementación en Código

```python
class CifradoSustitucionSimple:
    def __init__(self, clave: Optional[str] = None, alfabeto: Optional[Alfabeto] = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = clave.upper() if clave else None
        self.mapeo_cifrado = self._crear_mapeo_cifrado()
        self.mapeo_descifrado = {v: k for k, v in self.mapeo_cifrado.items()}

    def _crear_mapeo_cifrado(self) -> Dict[str, str]:
        alfabeto_base = self.alfabeto.alfabeto
        mapeo = {}

        if self.clave:
            clave_limpia = "".join(dict.fromkeys(self.clave))
            letras_restantes = "".join(c for c in alfabeto_base if c not in clave_limpia)
            alfabeto_permutado = clave_limpia + letras_restantes
        else:
            alfabeto_permutado = alfabeto_base[1:] + alfabeto_base[0]

        for i, caracter in enumerate(alfabeto_base):
            mapeo[caracter] = alfabeto_permutado[i]

        return mapeo

    def cifrar(self, texto_plano: str) -> str:
        texto_limpio = limpiar_texto(texto_plano)
        resultado = []
        for caracter in texto_limpio:
            if caracter in self.mapeo_cifrado:
                resultado.append(self.mapeo_cifrado[caracter])
            else:
                resultado.append(caracter)
        return "".join(resultado)

    def descifrar(self, texto_cifrado: str) -> str:
        texto_limpio = limpiar_texto(texto_cifrado)
        resultado = []
        for caracter in texto_limpio:
            if caracter in self.mapeo_descifrado:
                resultado.append(self.mapeo_descifrado[caracter])
            else:
                resultado.append(caracter)
        return "".join(resultado)
```