import customtkinter as ctk
from tkinter import messagebox, scrolledtext
import sys
import os

# Agregar el directorio actual al path para importar los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar todos los cifrados
from CifDesplazamiento.cifrado_cesar import cifrar_cesar, descifrar_cesar
from CifDesplazamiento.cifrado_vigenere import cifrar_vigenere, descifrar_vigenere
from CifSustitucion.cifrado_atbash import cifrar_atbash, descifrar_atbash
from CifSustitucion.cifrado_sustitucion_simple import cifrar_sustitucion_simple, descifrar_sustitucion_simple
from CifSustMonoPoli.cifrado_playfair import cifrar_playfair, descifrar_playfair
from CifSustMonoPoli.cifrado_hill import cifrar_hill, descifrar_hill
from CifSustMonoPoli.cifrado_autokey import cifrar_autokey, descifrar_autokey
from CifSustMonoPoli.cifrado_xor import cifrar_xor, descifrar_xor
from CifTransposicion.cifrado_transposicion_columnas import cifrar_transposicion_columnas, descifrar_transposicion_columnas
from CifTransposicion.cifrado_rail_fence import cifrar_rail_fence, descifrar_rail_fence
from CifTransposicion.cifrado_permutacion_general import cifrar_permutacion_general, descifrar_permutacion_general
from utilidades import analizar_frecuencia


class InterfazCifrados(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Librería de Cifrados Clásicos")
        self.geometry("1200x800")
        self.resizable(True, True)

        # Configurar tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Crear el layout principal
        self.crear_layout()

        # Crear las pestañas de cifrados
        self.crear_pestanas()

        # Configurar el menú lateral
        self.crear_menu_lateral()

    def crear_layout(self):
        """Crear el layout principal de la aplicación"""
        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Título
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="🔐 Librería de Cifrados Clásicos",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Frame para el contenido (menú lateral + área principal)
        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def crear_menu_lateral(self):
        """Crear el menú lateral con los cifrados disponibles"""
        # Frame del menú lateral
        self.sidebar_frame = ctk.CTkScrollableFrame(
            self.content_frame,
            width=250,
            height=600
        )
        self.sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

        # Título del menú
        menu_title = ctk.CTkLabel(
            self.sidebar_frame,
            text="Cifrados Disponibles",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        menu_title.pack(pady=(10, 20))

        # Botones del menú
        self.cifrados = {
            "César": self.mostrar_cesar,
            "Vigenère": self.mostrar_vigenere,
            "Atbash": self.mostrar_atbash,
            "Sustitución Simple": self.mostrar_sustitucion_simple,
            "Playfair": self.mostrar_playfair,
            "Hill": self.mostrar_hill,
            "Autokey": self.mostrar_autokey,
            "XOR": self.mostrar_xor,
            "Transposición Columnas": self.mostrar_transposicion_columnas,
            "Rail Fence": self.mostrar_rail_fence,
            "Permutación General": self.mostrar_permutacion_general,
            "Análisis de Frecuencias": self.mostrar_analisis_frecuencias
        }

        for nombre, funcion in self.cifrados.items():
            btn = ctk.CTkButton(
                self.sidebar_frame,
                text=nombre,
                command=funcion,
                height=40,
                font=ctk.CTkFont(size=12)
            )
            btn.pack(pady=2, padx=10, fill="x")

        # Botón de cambio de tema
        self.theme_button = ctk.CTkButton(
            self.sidebar_frame,
            text="🌙 Modo Oscuro",
            command=self.cambiar_tema,
            height=35
        )
        self.theme_button.pack(pady=(20, 10), padx=10, fill="x")

    def crear_pestanas(self):
        """Crear el área principal donde se mostrarán los cifrados"""
        self.main_area = ctk.CTkFrame(self.content_frame)
        self.main_area.pack(side="right", fill="both", expand=True)

        # Mensaje de bienvenida
        self.bienvenida_label = ctk.CTkLabel(
            self.main_area,
            text="👋 ¡Bienvenido a la Librería de Cifrados Clásicos!\n\n"
                 "Selecciona un cifrado del menú lateral para comenzar.",
            font=ctk.CTkFont(size=16),
            wraplength=400
        )
        self.bienvenida_label.pack(expand=True)

    def limpiar_area_principal(self):
        """Limpiar el área principal para mostrar un nuevo cifrado"""
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def crear_interfaz_cifrado(self, titulo, campos_entrada, funcion_cifrar, funcion_descifrar=None):
        """Crear la interfaz genérica para un cifrado"""
        self.limpiar_area_principal()

        # Título del cifrado
        title_label = ctk.CTkLabel(
            self.main_area,
            text=f"🔐 {titulo}",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=(20, 10))

        # Frame para los controles
        controls_frame = ctk.CTkFrame(self.main_area)
        controls_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Campos de entrada
        entradas = {}
        row = 0

        for campo, config in campos_entrada.items():
            label = ctk.CTkLabel(controls_frame, text=config["label"])
            label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

            if config["tipo"] == "entry":
                entrada = ctk.CTkEntry(controls_frame, width=300)
                entrada.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
            elif config["tipo"] == "text":
                entrada = ctk.CTkTextbox(controls_frame, width=400, height=100)
                entrada.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
            elif config["tipo"] == "option":
                entrada = ctk.CTkOptionMenu(controls_frame, values=config["valores"])
                entrada.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
            elif config["tipo"] == "spinbox":
                entrada = ctk.CTkOptionMenu(controls_frame, values=config["valores"])
                entrada.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

            entradas[campo] = entrada
            row += 1

        # Frame para botones
        buttons_frame = ctk.CTkFrame(controls_frame)
        buttons_frame.grid(row=row, column=0, columnspan=2, pady=20)

        # Botón cifrar
        cifrar_btn = ctk.CTkButton(
            buttons_frame,
            text="🔒 Cifrar",
            command=lambda: self.ejecutar_cifrado(funcion_cifrar, entradas, "cifrar"),
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40
        )
        cifrar_btn.pack(side="left", padx=10)

        # Botón descifrar (si está disponible)
        if funcion_descifrar:
            descifrar_btn = ctk.CTkButton(
                buttons_frame,
                text="🔓 Descifrar",
                command=lambda: self.ejecutar_cifrado(funcion_descifrar, entradas, "descifrar"),
                font=ctk.CTkFont(size=14, weight="bold"),
                height=40
            )
            descifrar_btn.pack(side="left", padx=10)

        # Área de resultados
        resultado_label = ctk.CTkLabel(controls_frame, text="Resultado:")
        resultado_label.grid(row=row+1, column=0, sticky="w", padx=10, pady=(20, 5))

        self.resultado_text = scrolledtext.ScrolledText(
            controls_frame,
            width=60,
            height=8,
            font=("Consolas", 10),
            bg="#2b2b2b",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.resultado_text.grid(row=row+2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Configurar grid
        controls_frame.grid_columnconfigure(1, weight=1)

        return entradas

    def ejecutar_cifrado(self, funcion, entradas, tipo):
        """Ejecutar el cifrado y mostrar el resultado"""
        try:
            # Obtener los valores de las entradas
            args = []
            for campo, entrada in entradas.items():
                if isinstance(entrada, ctk.CTkEntry):
                    valor = entrada.get()
                    # Convertir números si es necesario, pero no para campos de "clave"
                    if campo != "clave":
                        try:
                            if valor.isdigit():
                                valor = int(valor)
                        except:
                            pass
                    args.append(valor)
                elif isinstance(entrada, ctk.CTkTextbox):
                    args.append(entrada.get("1.0", "end-1c"))
                elif isinstance(entrada, ctk.CTkOptionMenu):
                    valor = entrada.get()
                    # Convertir números si es necesario, pero no para campos de "metodo"
                    if campo != "metodo":
                        try:
                            if valor.isdigit():
                                valor = int(valor)
                        except:
                            pass
                    args.append(valor)

            # Ejecutar la función
            resultado = funcion(*args)

            # Mostrar resultado
            self.resultado_text.delete("1.0", "end")
            self.resultado_text.insert("1.0", f"✅ {tipo.title()} exitoso:\n\n{resultado}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al {tipo}: {str(e)}")
            self.resultado_text.delete("1.0", "end")
            self.resultado_text.insert("1.0", f"❌ Error: {str(e)}")

    def cambiar_tema(self):
        """Cambiar entre modo oscuro y claro"""
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
            self.theme_button.configure(text="☀️ Modo Claro")
        else:
            ctk.set_appearance_mode("Dark")
            self.theme_button.configure(text="🌙 Modo Oscuro")

    # Métodos para mostrar cada cifrado
    def mostrar_cesar(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "desplazamiento": {"label": "Desplazamiento (1-25):", "tipo": "option", "valores": [str(i) for i in range(1, 26)]}
        }
        self.crear_interfaz_cifrado("Cifrado César", campos, cifrar_cesar, descifrar_cesar)

    def mostrar_vigenere(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Cifrado Vigenère", campos, cifrar_vigenere, descifrar_vigenere)

    def mostrar_atbash(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"}
        }
        self.crear_interfaz_cifrado("Cifrado Atbash", campos, cifrar_atbash, descifrar_atbash)

    def mostrar_sustitucion_simple(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave (opcional):", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Sustitución Simple", campos, cifrar_sustitucion_simple, descifrar_sustitucion_simple)

    def mostrar_playfair(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Cifrado Playfair", campos, cifrar_playfair, descifrar_playfair)

    def mostrar_hill(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "tam_grupo": {"label": "Tamaño del grupo:", "tipo": "option", "valores": ["2", "3"]},
            "matriz": {"label": "Matriz (ej: [[3,3],[2,5]]):", "tipo": "entry"}
        }

        def cifrar_hill_wrapper(texto, tam_grupo, matriz_str):
            try:
                # Parsear la matriz
                matriz = eval(matriz_str)
                return cifrar_hill(texto, int(tam_grupo), matriz)
            except Exception as e:
                raise ValueError(f"Error en la matriz: {e}")

        def descifrar_hill_wrapper(texto, tam_grupo, matriz_str):
            try:
                matriz = eval(matriz_str)
                return descifrar_hill(texto, int(tam_grupo), matriz)
            except Exception as e:
                raise ValueError(f"Error en la matriz: {e}")

        self.crear_interfaz_cifrado("Cifrado Hill", campos, cifrar_hill_wrapper, descifrar_hill_wrapper)

    def mostrar_autokey(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Cifrado Autokey", campos, cifrar_autokey, descifrar_autokey)

    def mostrar_xor(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Cifrado XOR", campos, cifrar_xor, descifrar_xor)

    def mostrar_transposicion_columnas(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"}
        }
        self.crear_interfaz_cifrado("Transposición de Columnas", campos, cifrar_transposicion_columnas, descifrar_transposicion_columnas)

    def mostrar_rail_fence(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "rieles": {"label": "Número de rieles:", "tipo": "option", "valores": ["2", "3", "4", "5"]}
        }
        self.crear_interfaz_cifrado("Rail Fence (Zigzag)", campos, cifrar_rail_fence, descifrar_rail_fence)

    def mostrar_permutacion_general(self):
        campos = {
            "texto": {"label": "Texto:", "tipo": "text"},
            "clave": {"label": "Clave:", "tipo": "entry"},
            "metodo": {"label": "Método:", "tipo": "option", "valores": ["alfabetico", "numerico"]}
        }
        self.crear_interfaz_cifrado("Permutación General", campos, cifrar_permutacion_general, descifrar_permutacion_general)

    def mostrar_analisis_frecuencias(self):
        """Mostrar la interfaz de análisis de frecuencias"""
        self.limpiar_area_principal()

        title_label = ctk.CTkLabel(
            self.main_area,
            text="📊 Análisis de Frecuencias",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=(20, 10))

        controls_frame = ctk.CTkFrame(self.main_area)
        controls_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Campo de texto
        texto_label = ctk.CTkLabel(controls_frame, text="Texto a analizar:")
        texto_label.pack(pady=(10, 5))

        texto_entry = ctk.CTkTextbox(controls_frame, width=500, height=150)
        texto_entry.pack(pady=5)

        # Botón analizar
        analizar_btn = ctk.CTkButton(
            controls_frame,
            text="🔍 Analizar Frecuencias",
            command=lambda: self.analizar_frecuencias(texto_entry.get("1.0", "end-1c")),
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40
        )
        analizar_btn.pack(pady=20)

        # Área de resultados
        resultado_label = ctk.CTkLabel(controls_frame, text="Resultados del análisis:")
        resultado_label.pack(pady=(20, 5))

        self.analisis_text = scrolledtext.ScrolledText(
            controls_frame,
            width=60,
            height=15,
            font=("Consolas", 10),
            bg="#2b2b2b",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.analisis_text.pack(pady=5, padx=10)

    def analizar_frecuencias(self, texto):
        """Analizar las frecuencias del texto"""
        try:
            frecuencias = analizar_frecuencia(texto)
            resultado = "FRECUENCIAS DE CARACTERES:\n\n"

            # Ordenar por frecuencia descendente
            sorted_freq = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

            for caracter, frecuencia in sorted_freq:
                porcentaje = (frecuencia / len(texto)) * 100 if len(texto) > 0 else 0
                resultado += f"'{caracter}': {frecuencia} ({porcentaje:.2f}%)\n"

            self.analisis_text.delete("1.0", "end")
            self.analisis_text.insert("1.0", resultado)

        except Exception as e:
            messagebox.showerror("Error", f"Error en el análisis: {str(e)}")


if __name__ == "__main__":
    app = InterfazCifrados()
    app.mainloop()