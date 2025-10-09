# Cifrado Atbash

## Descripción General

El **cifrado Atbash** es uno de los cifrados de sustitución más antiguos conocidos, datando del siglo VI a.C. Su nombre proviene del hebreo y significa "secreto" o "oculto". Es un cifrado de sustitución monoalfabética simple donde cada letra se reemplaza por su "opuesta" en el alfabeto.

A diferencia de otros cifrados que requieren claves o algoritmos complejos, Atbash es **determinístico y simétrico**: la misma operación sirve tanto para cifrar como para descifrar.

## Historia y Contexto

### Origen y Desarrollo
- **Siglo VI a.C.**: Aparece en la Biblia hebrea (Jeremías 25:26, 51:41)
- **Usado por los hebreos**: Para escribir nombres sagrados y textos religiosos
- **Época medieval**: Empleado en textos cabalísticos y alquímicos
- **Renacimiento**: Redescubierto y estudiado por criptógrafos europeos

### Importancia Histórica
- **Primer cifrado documentado**: Uno de los métodos de cifrado más antiguos
- **Simbolismo**: La inversión del alfabeto tenía significado místico
- **Influencia**: Base para el desarrollo de cifrados de sustitución más complejos
- **Supervivencia**: Todavía se usa en juegos y acertijos modernos

### Terminología
- **Monoalfabético**: Usa un solo alfabeto de sustitución
- **Simétrico**: Mismo algoritmo para cifrar y descifrar
- **Involutivo**: Aplicar dos veces devuelve el texto original
- **Lineal**: Mapeo uno-a-uno entre letras

## Lógica Matemática

### Definición Formal

Para un alfabeto Σ de tamaño n, el cifrado Atbash se define como:

**C(x) = (n-1) - x**

Donde:
- x es la posición de la letra en el alfabeto (0-indexed)
- n es el tamaño del alfabeto
- C(x) es la posición de la letra cifrada

### Propiedades Matemáticas

1. **Involutiva**: C(C(x)) = x (aplicar dos veces = identidad)
2. **Bijectiva**: Cada letra se mapea a exactamente una letra diferente
3. **Simétrica**: C = C⁻¹ (cifrado = descifrado)
4. **Lineal**: Preserva el orden relativo (pero invertido)

### Tabla de Sustitución

Para alfabeto A-Z (26 letras):

| Original | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z |
|----------|---------------------------------------------------|
| Atbash   | Z Y X W V U T S R Q P O N M L K J I H G F E D C B A |

### Fórmula General

Para cualquier alfabeto ordenado:
```
posición_cifrada = (longitud_alfabeto - 1) - posición_original
```

## Algoritmo Detallado

### Implementación Básica
```python
def atbash_caracter(caracter, alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Aplica Atbash a un solo caracter"""
    if caracter.upper() not in alfabeto:
        return caracter  # Mantener no-letras

    indice = alfabeto.index(caracter.upper())
    indice_atbash = len(alfabeto) - 1 - indice
    resultado = alfabeto[indice_atbash]

    # Mantener caso original
    return resultado.lower() if caracter.islower() else resultado
```

### Cifrado/Descifrado Completo
```python
def cifrar_atbash(texto):
    """Cifra o descifra usando Atbash (son equivalentes)"""
    resultado = ""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for caracter in texto:
        if caracter.isalpha():
            # Encontrar posición en alfabeto
            indice = ord(caracter.upper()) - ord('A')
            # Calcular posición Atbash
            indice_atbash = 25 - indice
            # Obtener nueva letra
            nueva_letra = chr(indice_atbash + ord('A'))

            # Mantener caso
            if caracter.islower():
                nueva_letra = nueva_letra.lower()

            resultado += nueva_letra
        else:
            resultado += caracter  # Mantener no-letras

    return resultado
```

## Ejemplos Detallados

### Ejemplo 1: Texto Simple
```
Mensaje:     "HELLO"
Proceso:
H(7)  → 25-7 = 18 → S
E(4)  → 25-4 = 21 → V
L(11) → 25-11 = 14 → O
L(11) → 25-11 = 14 → O
O(14) → 25-14 = 11 → L

Resultado: "SVOOL"
```

### Ejemplo 2: Frase Completa
```
Mensaje:     "THE QUICK BROWN FOX"
Resultado:   "GSV JFRXP YILDM ULC"
```

### Ejemplo 3: Con Números y Símbolos
```
Mensaje:     "HELLO123!"
Resultado:   "SVOOL123!"
```
*(Los números y símbolos se mantienen sin cambios)*

### Ejemplo 4: Aplicación Doble (Verificación de Simetría)
```
Mensaje original: "ABC"
Primera aplicación: "ZYX"
Segunda aplicación: "ABC" (regresa al original)
```

### Ejemplo 5: Texto en Español
```
Mensaje:     "HOLA MUNDO"
Resultado:   "SLOZ NFLMW"
```

### Ejemplo 6: Nombre Sagrado (Uso Histórico)
```
Texto hebreo: "YHWH" (nombre de Dios)
Atbash:       "SLSH"
```
*(En la cábala, esto tenía significado místico)*

## Análisis de Frecuencia

### Patrón Original vs Atbash

**Texto en inglés normal:**
- E (12.7%), T (9.1%), A (8.2%), O (7.5%), I (7.0%)
- Frecuencia decrece gradualmente

**Texto con Atbash:**
- V (12.7%), G (9.1%), Z (8.2%), L (7.5%), R (7.0%)
- Mismo patrón pero con letras "opuestas"

### Preservación de Patrones
- **Frecuencias relativas**: Se mantienen idénticas
- **Patrones de digramas**: Se invierten pero se preservan
- **Longitud de palabras**: Sin cambios
- **Puntuación**: Sin cambios

## Criptoanálisis (Ataques)

### Análisis de Frecuencia
**Método**: Identificar las letras más frecuentes en el texto cifrado
- En inglés: V, G, Z, L, R (equivalentes a E, T, A, O, I)
- En español: S, H, A, O, R (equivalentes a H, S, Z, L, I)

**Ejemplo**:
```
Texto cifrado: "SVOOL"
Frecuencias: S(1), V(1), O(2), L(2)
→ O y L son las más frecuentes
→ Probablemente cifran E y A (las más frecuentes en inglés)
→ O = E, L = A
→ Verificar: S(7) ↔ E(4)? No
→ L(11) ↔ A(0)? 25-11=14=O, pero A debería ser Z
```

### Ataque por Fuerza Bruta
**Complejidad**: Solo 1 posibilidad (determinístico)
**Tiempo**: Instantáneo

### Ataque por Conocimiento del Idioma
**Método**: Usar palabras comunes y estructura de oración
```
Texto cifrado: "SVOOL"
Posibles palabras: "HELLO", "WORLD", etc.
Aplicar Atbash: "HELLO" → "SVOOL" ✓
```

## Variantes y Extensiones

### Atbash Numérico
```
Dígitos: 0 1 2 3 4 5 6 7 8 9
Atbash:  9 8 7 6 5 4 3 2 1 0
```

### Atbash por Palabras
- Invertir orden de palabras en una oración
- Combinado con Atbash de letras

### Atbash Rotativo
- Rotar alfabeto en lugar de invertir
- Más general que el Atbash puro

### Atbash en Otros Sistemas
- **Alfabeto hebreo**: Álef ↔ Tav, Bet ↔ Shin, etc.
- **Alfabeto griego**: Alfa ↔ Omega, Beta ↔ Psi, etc.
- **Sistemas numéricos**: 1 ↔ 9, 2 ↔ 8, etc.

## Análisis de Seguridad

### Fortalezas
- **Simplicidad**: Muy fácil de recordar e implementar
- **Sin clave**: No hay problemas de distribución de claves
- **Rápido**: Operación O(n) lineal
- **Reversible**: Siempre se puede descifrar

### Debilidades
- **Completamente inseguro**: Solo una posibilidad
- **Patrones preservados**: Frecuencias y estructuras se mantienen
- **Fácil de detectar**: Patrón de frecuencia invertido es característico
- **Sin aleatoriedad**: Determinístico y predecible

### Comparación de Seguridad

| Método | Seguridad | Velocidad | Complejidad |
|--------|-----------|-----------|-------------|
| Atbash | Muy Baja | Muy Alta | Muy Baja |
| César | Baja | Muy Alta | Baja |
| Vigenère | Media | Alta | Media |
| AES | Muy Alta | Alta | Alta |

## Aplicaciones Modernas

### Usos Legítimos
- **Juegos y acertijos**: Rompecabezas, juegos de palabras
- **Ofuscación simple**: Para texto que no necesita alta seguridad
- **Educación**: Enseñar conceptos básicos de criptografía
- **Arte y literatura**: Efectos estilísticos

### Usos en Seguridad
- **Capa adicional**: Combinado con otros cifrados
- **Autenticación**: Verificación de integridad simple
- **Hashing básico**: Para checksums no criptográficos

## Implementación Completa

```python
class CifradoAtbash:
    """
    Implementación del cifrado Atbash.
    Es simétrico: cifrar y descifrar usan el mismo método.
    """

    def __init__(self, alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        """
        Inicializa el cifrado Atbash.

        Args:
            alfabeto: Cadena con los caracteres del alfabeto (default: A-Z)
        """
        self.alfabeto = alfabeto.upper()
        self.longitud = len(alfabeto)

        # Crear tabla de traducción
        self.tabla_traduccion = {}
        for i, caracter in enumerate(self.alfabeto):
            indice_opuesto = self.longitud - 1 - i
            caracter_opuesto = self.alfabeto[indice_opuesto]
            self.tabla_traduccion[caracter] = caracter_opuesto

    def _traducir_caracter(self, caracter: str) -> str:
        """
        Traduce un caracter usando Atbash.

        Args:
            caracter: Caracter a traducir

        Returns:
            Caracter traducido o el mismo si no está en el alfabeto
        """
        if caracter.isalpha():
            # Convertir a mayúscula para buscar en tabla
            mayuscula = caracter.upper()
            if mayuscula in self.tabla_traduccion:
                traducido = self.tabla_traduccion[mayuscula]
                # Mantener caso original
                return traducido.lower() if caracter.islower() else traducido

        return caracter  # Mantener no-letras sin cambios

    def cifrar(self, texto_plano: str) -> str:
        """
        Cifra un texto usando Atbash.
        (Es equivalente a descifrar)

        Args:
            texto_plano: Texto a cifrar

        Returns:
            Texto cifrado
        """
        return "".join(self._traducir_caracter(c) for c in texto_plano)

    def descifrar(self, texto_cifrado: str) -> str:
        """
        Descifra un texto cifrado con Atbash.
        (Es equivalente a cifrar)

        Args:
            texto_cifrado: Texto a descifrar

        Returns:
            Texto descifrado
        """
        # Atbash es simétrico
        return self.cifrar(texto_cifrado)

    def es_simetrico(self) -> bool:
        """
        Verifica que el cifrado sea simétrico.

        Returns:
            True (Atbash siempre es simétrico)
        """
        return True

    def analizar_frecuencia(self, texto: str) -> dict:
        """
        Analiza la frecuencia de letras en un texto.

        Args:
            texto: Texto a analizar

        Returns:
            Diccionario con frecuencias de cada letra
        """
        frecuencias = {}
        total_letras = 0

        for caracter in texto.upper():
            if caracter in self.alfabeto:
                frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
                total_letras += 1

        # Convertir a porcentajes
        if total_letras > 0:
            for letra in frecuencias:
                frecuencias[letra] = (frecuencias[letra] / total_letras) * 100

        return frecuencias

# Funciones de conveniencia
def cifrar_atbash(texto: str, alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> str:
    """Función de conveniencia para cifrar con Atbash"""
    atbash = CifradoAtbash(alfabeto)
    return atbash.cifrar(texto)

def descifrar_atbash(texto: str, alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> str:
    """Función de conveniencia para descifrar con Atbash"""
    atbash = CifradoAtbash(alfabeto)
    return atbash.descifrar(texto)

# Ejemplo de uso y demostración
if __name__ == "__main__":
    # Ejemplo básico
    mensaje = "HELLO WORLD"
    print(f"Mensaje original: {mensaje}")

    cifrado = cifrar_atbash(mensaje)
    print(f"Texto cifrado: {cifrado}")

    descifrado = descifrar_atbash(cifrado)
    print(f"Texto descifrado: {descifrado}")

    # Verificar simetría
    print(f"¿Es simétrico? {cifrado == descifrar_atbash(mensaje)}")

    # Análisis de frecuencia
    atbash = CifradoAtbash()
    freq_original = atbash.analizar_frecuencia(mensaje)
    freq_cifrado = atbash.analizar_frecuencia(cifrado)

    print(f"\nFrecuencia original: {freq_original}")
    print(f"Frecuencia cifrado: {freq_cifrado}")

    # Demostración de involución
    doble_cifrado = cifrar_atbash(cifrar_atbash(mensaje))
    print(f"\nDoble cifrado (debe ser igual al original): {doble_cifrado}")
    print(f"¿Es igual al original? {doble_cifrado == mensaje}")
```

## Conclusión

El cifrado Atbash, aunque extremadamente simple e inseguro por estándares modernos, representa un hito importante en la historia de la criptografía:

- **Simbolismo matemático**: La inversión perfecta del alfabeto
- **Simetría elegante**: Una función que es su propia inversa
- **Base conceptual**: Fundamento para entender cifrados de sustitución
- **Valor educativo**: Excelente para enseñar conceptos básicos

Aunque nunca debe usarse para seguridad real, Atbash continúa siendo relevante en educación, juegos y como componente de sistemas de cifrado más complejos.