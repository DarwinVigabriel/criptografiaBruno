# Librería de Cifrados Clásicos

Esta librería implementa varios algoritmos clásicos de cifrado de sustitución y transposición en Python.

## Algoritmos Implementados

### Cifrados de Sustitución

1. **Cifrado César**
   - Desplazamiento fijo de letras
   - Incluye ataque de fuerza bruta

2. **Cifrado Vigenère**
   - Cifrado polialfabético con clave
   - Análisis de frecuencia básico

3. **Cifrado Atbash**
   - Sustitución simétrica (inversión del alfabeto)

4. **Cifrado Playfair**
   - Cifrado digráfico con matriz 5x5
   - Manejo especial de I/J

5. **Cifrado Hill**
   - Cifrado matricial usando álgebra lineal
   - Matrices invertibles módulo 26

6. **Cifrado Autokey**
   - Variante de Vigenère que usa el texto plano como clave

7. **Cifrado XOR**
   - Cifrado simétrico básico con operaciones XOR
   - Resultados en base64 para legibilidad

### Cifrados de Transposición

8. **Transposición de Columnas**
   - Reordenamiento basado en clave alfabética

9. **Rail Fence (Zigzag)**
   - Cifrado en zigzag con múltiples rieles

## Características

- **Alfabetos personalizables**: Soporte para alfabetos personalizados
- **Análisis de frecuencias**: Herramienta para criptoanálisis básico
- **Interfaz de usuario**: Menú interactivo para todos los cifrados
- **Validación de entrada**: Verificación de parámetros y textos
- **Documentación completa**: Comentarios detallados en español

## Requisitos

- Python 3.6+
- NumPy (para cifrado Hill)

## Instalación

### Requisitos Previos
- **Python 3.6 o superior**
- **pip** (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga el repositorio**
   ```bash
   git clone https://github.com/DarwinVigabriel/criptografiaBruno.git
   cd criptografiaBruno
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

   **O instala manualmente:**
   ```bash
   pip install numpy>=1.19.0
   pip install customtkinter>=5.0.0
   ```

3. **Verifica la instalación**
   ```bash
   python -c "import numpy; import customtkinter; print('Instalación exitosa')"
   ```

4. **Ejecuta el programa**
   ```bash
   python main.py
   ```

### Notas de Instalación

- **Windows**: Si tienes problemas con pip, usa `python -m pip install -r requirements.txt`
- **Linux/macOS**: Puede requerir `sudo` para instalación global: `sudo pip install -r requirements.txt`
- **Entorno virtual** (recomendado):
  ```bash
  python -m venv env
  env\Scripts\activate  # Windows
  source env/bin/activate  # Linux/macOS
  pip install -r requirements.txt
  ```

## Uso

```python
from CifDesplazamiento.cifrado_cesar import cifrar_cesar, descifrar_cesar

# Cifrar un mensaje
mensaje_cifrado = cifrar_cesar("HOLA MUNDO", 3)
print(mensaje_cifrado)  # "KROD PXQGR"

# Descifrar
mensaje_original = descifrar_cesar(mensaje_cifrado, 3)
print(mensaje_original)  # "HOLA MUNDO"
```

## Vulnerabilidades Conocidas

### Cifrado César
- **Fuerza bruta**: Solo 25 posibilidades
- **Análisis de frecuencia**: Patrón de frecuencias se mantiene

### Cifrado Vigenère
- **Análisis de Kasiski**: Repeticiones revelan longitud de clave
- **Análisis de frecuencia**: Cada posición tiene distribución diferente

### Cifrado Playfair
- **Análisis de dígrafo**: Frecuencias de pares de letras
- **Matriz conocida**: Si se conoce la clave, es trivial

### Cifrado Hill
- **Análisis de frecuencias**: Para textos largos
- **Ataque de plaintext conocido**: Si se conoce suficiente texto plano

### Cifrados de Transposición
- **Análisis de patrones**: Columnas mantienen propiedades estadísticas
- **Longitud del mensaje**: Puede revelar información sobre la clave

## Estructura del Proyecto

```
Criptografia_Bruno/
├── __init__.py                    # Paquete Python
├── main.py                        # Programa principal con menú
├── utilidades.py                  # Funciones auxiliares
├── requirements.txt               # Dependencias
├── README.md                      # Documentación
├── CifDesplazamiento/             # Cifrados por desplazamiento
│   ├── __init__.py
│   ├── cifrado_cesar.py           # Cifrado César
│   └── cifrado_vigenere.py        # Cifrado Vigenère
├── CifSustitucion/                # Cifrados de sustitución simple
│   ├── __init__.py
│   └── cifrado_atbash.py          # Cifrado Atbash
├── CifSustMonoPoli/               # Cifrados mono/poli alfabéticos
│   ├── __init__.py
│   ├── cifrado_playfair.py        # Cifrado Playfair
│   ├── cifrado_hill.py            # Cifrado Hill
│   ├── cifrado_autokey.py         # Cifrado Autokey
│   └── cifrado_xor.py             # Cifrado XOR
└── CifTransposicion/              # Cifrados de transposición
    ├── __init__.py
    ├── cifrado_transposicion_columnas.py  # Transposición de columnas
    └── cifrado_rail_fence.py      # Rail Fence
```

## Ejemplos de Uso

### Cifrado César
```python
from CifDesplazamiento.cifrado_cesar import CifradoCesar

cesar = CifradoCesar(3)
mensaje = "ATAQUE AL AMANECER"
cifrado = cesar.cifrar(mensaje)
print(cifrado)  # "DWDTXH DO DPDQHFHU"
```

### Cifrado Vigenère
```python
from CifDesplazamiento.cifrado_vigenere import cifrar_vigenere

resultado = cifrar_vigenere("HOLA", "CLAVE")
print(resultado)  # "JURC"
```

### Análisis de Frecuencias
```python
from utilidades import analizar_frecuencia

texto = "EL RAPIDO ZORRO MARRON SALTA SOBRE EL PEREZOSO PERRO"
frecuencias = analizar_frecuencia(texto)
for letra, freq in sorted(frecuencias.items()):
    print(f"{letra}: {freq}")
```

## Documentación Adicional

Para un análisis detallado de vulnerabilidades, ejemplos de ruptura y casos prácticos de cada algoritmo, consulte:

📄 **[INFORME_AMPLIADO.md](INFORME_AMPLIADO.md)** - Análisis completo con ejemplos de criptoanálisis