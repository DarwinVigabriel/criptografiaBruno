# 🔐 Librería de Cifrados Clásicos - Interfaz Gráfica

Una interfaz gráfica moderna y completa para realizar todos los cifrados clásicos implementados en la librería.

## 🚀 Cómo usar la interfaz

### Requisitos previos
- Python 3.6 o superior
- Instalar dependencias: `pip install customtkinter numpy`

### Ejecutar la interfaz
```bash
python interfaz_grafica.py
```

## 📋 Características de la interfaz

### 🎨 Diseño moderno
- Tema oscuro/claro con botón de cambio
- Interfaz intuitiva y fácil de usar
- Diseño responsive que se adapta al tamaño de la ventana

### 🔧 Funcionalidades
- **Menú lateral**: Acceso rápido a todos los cifrados disponibles
- **Campos de entrada**: Adaptados a cada cifrado específico
- **Botones de acción**: Cifrar y descifrar (cuando aplica)
- **Área de resultados**: Muestra el resultado del cifrado/descifrado
- **Análisis de frecuencias**: Herramienta adicional para criptoanálisis

## 🔐 Cifrados disponibles

### Cifrados de desplazamiento
- **César**: Desplazamiento fijo del alfabeto
- **Vigenère**: Cifrado polialfabético con clave

### Cifrados de sustitución
- **Atbash**: Sustitución espejo del alfabeto
- **Sustitución Simple**: Sustitución monoalfabética personalizada

### Cifrados mixtos (sustitución + polialfabéticos)
- **Playfair**: Cifrado de bigramas con matriz
- **Hill**: Cifrado matricial
- **Autokey**: Vigenère con autogeneración de clave
- **XOR**: Cifrado por operación XOR

### Cifrados de transposición
- **Transposición de Columnas**: Reordenamiento por columnas
- **Rail Fence (Zigzag)**: Cifrado en zigzag
- **Permutación General**: Reordenamiento personalizado

### 🛠️ Herramientas adicionales
- **Análisis de Frecuencias**: Análisis estadístico de textos cifrados

## 📖 Instrucciones de uso

1. **Seleccionar un cifrado**: Haz clic en cualquier cifrado del menú lateral
2. **Ingresar datos**:
   - Texto a cifrar/descifrar
   - Parámetros específicos (clave, desplazamiento, etc.)
3. **Ejecutar**: Presiona "🔒 Cifrar" o "🔓 Descifrar"
4. **Ver resultado**: El resultado aparecerá en el área inferior

## ⚠️ Notas importantes

- Todos los cifrados incluyen validación de entrada robusta
- Los errores se muestran en ventanas emergentes
- El texto se procesa respetando mayúsculas/minúsculas
- Algunos cifrados requieren claves específicas (ver documentación de cada módulo)

## 🎯 Ventajas de la interfaz gráfica

- **Accesible**: No requiere conocimientos de línea de comandos
- **Visual**: Resultados claros y formateados
- **Interactiva**: Cambio de tema, navegación intuitiva
- **Completa**: Incluye todos los cifrados implementados
- **Robusta**: Manejo de errores y validaciones integradas

## 📁 Estructura del proyecto

```
Criptografia_Bruno/
├── interfaz_grafica.py      # Interfaz gráfica principal
├── main.py                  # Interfaz de línea de comandos
├── utilidades.py            # Funciones auxiliares
├── requirements.txt         # Dependencias
├── CifDesplazamiento/       # Cifrados de desplazamiento
├── CifSustitucion/          # Cifrados de sustitución
├── CifSustMonoPoli/         # Cifrados mixtos
├── CifTransposicion/        # Cifrados de transposición
└── tests/                   # Pruebas unitarias
```

¡Disfruta explorando los cifrados clásicos con esta interfaz moderna y fácil de usar! 🔐✨