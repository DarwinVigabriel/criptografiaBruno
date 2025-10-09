# Cifrado de Sustitución Simple (Monoalfabética)

## Descripción General

El cifrado de **sustitución simple** (también llamado **monoalfabético**) es uno de los métodos criptográficos más antiguos y fundamentales. Consiste en **reemplazar cada letra del alfabeto por otra letra fija**, creando una **permutación completa** del alfabeto.

A diferencia del cifrado César (que solo usa desplazamientos), la sustitución simple permite **cualquier reordenamiento** de las letras, lo que lo hace más flexible pero también más complejo de configurar manualmente.

## Historia y Contexto

### Origen y Desarrollo
- **Antigua Roma**: Posibles usos en comunicaciones secretas
- **Renacimiento**: Desarrollo sistemático de métodos
- **Siglo XVI**: Uso en diplomacia y guerra
- **Arabia Medieval**: Desarrollo de métodos similares

### Importancia Histórica
- **Primer cifrado sistemático**: Más allá de transposiciones simples
- **Base conceptual**: Fundamento para cifrados polialfabéticos
- **Uso práctico**: Suficientemente simple para uso manual
- **Transición**: Puente entre métodos antiguos y modernos

### Terminología
- **Monoalfabético**: Un solo alfabeto de sustitución
- **Permutación**: Reordenamiento completo de letras
- **Clave**: Determina el orden de sustitución
- **Mapeo**: Correspondencia letra → letra cifrada

## Arquitectura del Sistema

### Componentes Principales
1. **Alfabeto base**: Conjunto de caracteres originales
2. **Clave**: Determina la permutación
3. **Mapeo de cifrado**: Diccionario letra → letra cifrada
4. **Mapeo de descifrado**: Diccionario inverso

### Tipos de Configuración
- **Sin clave**: Rotación simple (similar a César)
- **Con clave**: Permutación basada en palabra clave
- **Personalizada**: Mapeo arbitrario definido por usuario

## Algoritmo de Construcción

### Método con Clave
```python
def crear_alfabeto_permutado(clave: str, alfabeto_base: str) -> str:
    # 1. Limpiar clave de duplicados
    clave_limpia = "".join(dict.fromkeys(clave.upper()))

    # 2. Obtener letras restantes en orden
    letras_restantes = "".join(c for c in alfabeto_base if c not in clave_limpia)

    # 3. Concatenar para formar alfabeto permutado
    return clave_limpia + letras_restantes
```

### Método sin Clave (Rotación)
```python
def crear_alfabeto_rotado(alfabeto_base: str, desplazamiento: int = 1) -> str:
    return alfabeto_base[desplazamiento:] + alfabeto_base[:desplazamiento]
```

## Ejemplos Detallados

### Ejemplo 1: Con Clave "CLAVE"
```
Alfabeto original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Clave: "CLAVE"
Clave limpia (sin duplicados): C L A V E

Letras restantes: B D F G H I J K M N O P Q R S T U W X Y Z

Alfabeto permutado: C L A V E B D F G H I J K M N O P Q R S T U W X Y Z

Mapeo resultante:
A→C, B→L, C→A, D→V, E→E, F→B, G→D, H→F, I→G, J→H,
K→I, L→J, M→K, N→M, O→N, P→O, Q→P, R→Q, S→R, T→S,
U→T, V→U, W→V, X→W, Y→X, Z→Y
```

**Mensaje**: "ATAQUE"
**Cifrado**: "CTCQTE"

### Ejemplo 2: Sin Clave (Rotación Simple)
```
Alfabeto original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Alfabeto rotado:  B C D E F G H I J K L M N O P Q R S T U V W X Y Z A

Mapeo: A→B, B→C, C→D, ..., Z→A
```

**Mensaje**: "HELLO"
**Cifrado**: "IFMMP"

### Ejemplo 3: Clave Completa
```
Clave: "ZYXWVUTSRQPONMLKJIHGFEDCBA"
(Alfabeto invertido)

Mensaje: "ABC"
Cifrado: "ZYX"
```

## Análisis Matemático

### Teoría de Permutaciones
- **Espacio de claves**: 26! ≈ 4×10²⁶ posibilidades
- **Grupo simétrico**: S₂₆ (permutaciones de 26 elementos)
- **Composición**: Permutaciones se pueden combinar

### Propiedades Algebraicas
- **Involución**: Algunas permutaciones son su propia inversa
- **Ciclos**: Descomposición en ciclos disjuntos
- **Orden**: Número de aplicaciones para volver al original

## Criptoanálisis - Análisis de Frecuencia

### Vulnerabilidades Fundamentales
- **Frecuencias preservadas**: Cada letra siempre se mapea a la misma
- **Patrones lingüísticos**: Estructura del idioma se mantiene
- **Análisis estadístico**: Comparación con frecuencias esperadas

### Método de Ataque
1. **Contar frecuencias** en el texto cifrado
2. **Comparar** con frecuencias del idioma objetivo
3. **Mapear** letras más frecuentes
4. **Refinar** usando contexto y palabras comunes

### Ejemplo de Criptoanálisis
```
Texto cifrado: "CTCQTE CL CMCNAEAER"
Frecuencias: C=6, E=4, T=3, A=3, Q=2, L=2, M=2, N=2, R=1

Frecuencias esperadas en español:
E=13.7%, A=11.7%, O=8.7%, S=7.9%, R=6.9%, N=6.7%, I=6.2%, etc.

Mapeo tentativo:
C (6) → E (más frecuente)
E (4) → A (segunda más frecuente)
T (3) → O (tercera más frecuente)
...
```

## Análisis de Seguridad

### Fortalezas
- **Espacio de claves grande**: 26! posibilidades teóricas
- **No lineal**: Más complejo que desplazamientos simples
- **Configurable**: Adaptable a diferentes necesidades
- **Determinístico**: Siempre produce mismo resultado

### Debilidades
- **Monoalfabético**: Mapeo fijo vulnerable a análisis estadístico
- **Frecuencias preservadas**: Patrón estadístico del idioma se mantiene
- **Palabras comunes**: "EL", "LA", "DE" siguen siendo detectables
- **Contexto lingüístico**: Estructura gramatical se preserva

### Comparación con Otros Cifrados

| Cifrado | Seguridad | Complejidad | Facilidad de Uso |
|---------|-----------|-------------|------------------|
| César | Muy Baja | Baja | Alta |
| Sustitución Simple | Baja | Media | Media |
| Vigenère | Media | Media | Media |
| Hill | Alta | Alta | Baja |

## Implementación Completa

```python
from typing import Dict, Optional
from collections import OrderedDict

class CifradoSustitucionSimple:
    """
    Implementación de cifrado de sustitución simple (monoalfabética).

    Soporta configuración con clave o sin clave (rotación simple).
    """

    def __init__(self, clave: Optional[str] = None, alfabeto: Optional[Alfabeto] = None):
        """
        Inicializa el cifrado de sustitución simple.

        Args:
            clave: Palabra clave para generar la permutación (opcional)
            alfabeto: Alfabeto personalizado (opcional)
        """
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = clave.upper() if clave else None
        self.mapeo_cifrado = self._crear_mapeo_cifrado()
        self.mapeo_descifrado = {v: k for k, v in self.mapeo_cifrado.items()}

    def _crear_mapeo_cifrado(self) -> Dict[str, str]:
        """
        Crea el mapeo de cifrado basado en la clave o rotación simple.

        Returns:
            Diccionario de mapeo caracter -> caracter_cifrado
        """
        alfabeto_base = self.alfabeto.alfabeto
        mapeo = {}

        if self.clave:
            # Método con clave
            clave_limpia = "".join(OrderedDict.fromkeys(self.clave))
            letras_restantes = "".join(c for c in alfabeto_base if c not in clave_limpia)
            alfabeto_permutado = clave_limpia + letras_restantes
        else:
            # Método sin clave (rotación simple)
            alfabeto_permutado = alfabeto_base[1:] + alfabeto_base[0]

        for original, permutado in zip(alfabeto_base, alfabeto_permutado):
            mapeo[original] = permutado

        return mapeo

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando sustitución simple.

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado
        """
        texto_limpio = limpiar_texto(texto_plano)
        resultado = []

        for caracter in texto_limpio:
            if caracter in self.mapeo_cifrado:
                resultado.append(self.mapeo_cifrado[caracter])
            else:
                resultado.append(caracter)  # Preservar caracteres no alfabéticos

        return "".join(resultado)

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con sustitución simple.

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado
        """
        texto_limpio = limpiar_texto(texto_cifrado)
        resultado = []

        for caracter in texto_limpio:
            if caracter in self.mapeo_descifrado:
                resultado.append(self.mapeo_descifrado[caracter])
            else:
                resultado.append(caracter)  # Preservar caracteres no alfabéticos

        return "".join(resultado)

    def obtener_mapeo(self) -> Dict[str, str]:
        """
        Retorna el mapeo de cifrado actual.

        Returns:
            Diccionario con el mapeo caracter -> caracter_cifrado
        """
        return self.mapeo_cifrado.copy()

# Funciones de conveniencia
def cifrar_sustitucion_simple(texto: str, clave: Optional[str] = None) -> str:
    """Función de conveniencia para cifrar con sustitución simple"""
    cifrado = CifradoSustitucionSimple(clave)
    return cifrado.cifrar(texto)

def descifrar_sustitucion_simple(texto: str, clave: Optional[str] = None) -> str:
    """Función de conveniencia para descifrar sustitución simple"""
    cifrado = CifradoSustitucionSimple(clave)
    return cifrado.descifrar(texto)

# Ejemplos de uso
if __name__ == "__main__":
    mensaje = "HELLO WORLD"

    # Sin clave (rotación simple)
    print("=== Sin clave (rotación) ===")
    simple_rot = CifradoSustitucionSimple()
    cifrado_rot = simple_rot.cifrar(mensaje)
    descifrado_rot = simple_rot.descifrar(cifrado_rot)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado_rot}")
    print(f"Descifrado: {descifrado_rot}")

    # Con clave
    print("\n=== Con clave 'KEY' ===")
    simple_key = CifradoSustitucionSimple("KEY")
    cifrado_key = simple_key.cifrar(mensaje)
    descifrado_key = simple_key.descifrar(cifrado_key)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado_key}")
    print(f"Descifrado: {descifrado_key}")

    # Mostrar mapeo
    print(f"\nMapeo de cifrado: {simple_key.obtener_mapeo()}")
```

## Aplicaciones Modernas

### Uso Educativo
- **Enseñanza de criptografía**: Introducción a conceptos básicos
- **Análisis de frecuencia**: Demostración de vulnerabilidades estadísticas
- **Transición conceptual**: Puente hacia métodos más avanzados

### Uso Práctico Limitado
- **Juegos y acertijos**: Rompecabezas criptográficos
- **Ofuscación simple**: Para casos no críticos
- **Componente de sistemas complejos**: Parte de cifrados híbridos

## Conclusión

El cifrado de sustitución simple representa un **hito importante** en la evolución de la criptografía, demostrando tanto los **límites de los métodos monoalfabéticos** como la necesidad de **enfoques más sofisticados**.

**Contribuciones clave**:
- **Flexibilidad aumentada**: Más opciones que desplazamientos simples
- **Comprensión conceptual**: Base para entender permutaciones
- **Análisis estadístico**: Introducción al criptoanálisis moderno
- **Transición histórica**: Puente entre cifrados antiguos y polialfabéticos

Su estudio es esencial para entender por qué los **cifrados monoalfabéticos son inherentemente vulnerables** y cómo esto llevó al desarrollo de sistemas polialfabéticos más seguros como el Vigenère.