# Cifrado XOR

## Descripción

El cifrado XOR (OR exclusivo) es un cifrado simétrico simple que utiliza la operación XOR bit a bit entre el texto plano y una clave. Es ampliamente utilizado en criptografía moderna como componente básico de muchos algoritmos.

## Lógica de Funcionamiento

### Cifrado/Descifrado
Dado que XOR es su propia inversa, el mismo algoritmo sirve para cifrar y descifrar.

Para cada carácter:
- Convertir carácter del mensaje a su código ASCII
- Convertir carácter de la clave a su código ASCII
- Aplicar XOR: `resultado = ord(mensaje[i]) XOR ord(clave[i % len(clave)])`
- Convertir resultado de vuelta a carácter

La clave se repite cíclicamente si es más corta que el mensaje.

### Formato de Salida
Para mejorar la legibilidad, el resultado cifrado se codifica en base64, convirtiendo los bytes binarios en una cadena ASCII segura.

## Ejemplo

**Mensaje:** "HOLA" (ASCII: 72, 79, 76, 65)  
**Clave:** "AB" (ASCII: 65, 66)  

Proceso:
- H (72) XOR A (65) = 72 ⊕ 65 = 9
- O (79) XOR B (66) = 79 ⊕ 66 = 109
- L (76) XOR A (65) = 76 ⊕ 65 = 9
- A (65) XOR B (66) = 65 ⊕ 66 = 3

**Bytes cifrados:** `\x09\x6d\x09\x03`  
**Codificado en base64:** `CW0JCw==`

## Características

- **Simétrico:** Misma operación para cifrar y descifrar
- **Rápido:** Operación bit a bit muy eficiente
- **Reversible:** XOR con la misma clave recupera el original
- **Legible:** Resultado cifrado en formato base64

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
import base64

class CifradoXOR:
    def __init__(self, clave: str, alfabeto: Alfabeto = None):
        self.alfabeto = alfabeto or Alfabeto()
        self.clave = clave

    def cifrar(self, texto_plano: str) -> str:
        """Cifra usando XOR bit a bit sobre códigos ASCII"""
        resultado = ""
        indice_clave = 0

        for c in texto_plano:
            # XOR con el código ASCII del carácter
            clave_char = self.clave[indice_clave % len(self.clave)]
            nuevo_codigo = ord(c) ^ ord(clave_char)
            resultado += chr(nuevo_codigo)
            indice_clave += 1

        return resultado

    def descifrar(self, texto_cifrado: str) -> str:
        # XOR es simétrico
        return self.cifrar(texto_cifrado)

# Funciones de conveniencia con salida en base64
def cifrar_xor(texto: str, clave: str) -> str:
    """Cifra y devuelve resultado en base64"""
    xor = CifradoXOR(clave)
    resultado_binario = xor.cifrar(texto)
    return base64.b64encode(resultado_binario.encode('latin-1')).decode('ascii')

def descifrar_xor(texto_cifrado_base64: str, clave: str) -> str:
    """Descifra desde base64"""
    try:
        # Intentar decodificar de base64
        datos_binarios = base64.b64decode(texto_cifrado_base64)
        texto_para_descifrar = datos_binarios.decode('latin-1')
    except:
        # Si no es base64, asumir string binario directo
        texto_para_descifrar = texto_cifrado_base64

    xor = CifradoXOR(clave)
    return xor.descifrar(texto_para_descifrar)
```