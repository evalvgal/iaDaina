# 🏫 IA-Daina: Generador de Suport Escolar (Offline)

Aplicació educativa interactiva desenvolupada en **Python** i **Pygame (`pygame-ce`)** dissenyada específicament per a entorns escolars i pissarres digitals tàctils. Funciona de manera 100% autònoma (*offline*) i compta amb una arquitectura Model-Vista (MVC) modular dividida per etapes educatives (Infantil, Primària, ESO i Batxillerat).

---

## 📂 Estructura del Projecte

El projecte està organitzat sota una estructura neta i modular seguint el patró MVC:

```text
iaDaina/
├── Batxillerat/
│   ├── __init__.py
│   └── exercicisBatxillerat.py
├── ESO/
│   ├── __init__.py
│   └── exercicisESO.py
├── Infantil/
│   ├── Dibuix/
│   │   ├── __init__.py
│   │   ├── dibuix.py
│   │   └── grafics_dibuix.py
│   ├── __init__.py
│   └── exercicisInfantil.py
├── Primaria/
│   ├── __init__.py
│   └── exercicisPrimaria.py
├── esquemaiaDaina.py
├── grafics_iaDaina.py
├── iaReglesDaina.py
├── iaDaina.py
├── iaReglesDaina.py
└── README.md
```

### 🧸 Educació Infantil

- **Infantil/Dibuix/**: Aplicació interactiva de dibuix lliure amb animació procedimental intel·ligent. Classifica automàticament els traços (onades, personatges caminant com lletres/figures amb rebot i pas sincronitzat, mans que saluden o figures geomètriques) i els dóna vida amb partícules. Està composta per `dibuix.py` i `grafics_dibuix.py`.
- **Infantil/exercicisInfantil.py**: Generació d'exercicis de comptatge d'objectes i reconeixement de formes.

### 🎒 Educació Primària

- **Primaria/exercicisPrimaria.py**: Activitats d'aritmètica bàsica (sumes, restes, multiplicacions) i ortografia/diacritics en català.

### 📐 Educació Secundària Obligatòria (ESO)

- **ESO/exercicisESO.py**: Problemes de física (MRU), resolució d'equacions de primer grau i anàlisi sintàctica.

### 🎓 Batxillerat

- **Batxillerat/exercicisBatxillerat.py**: Càlcul de derivades mitjançant regles de potència i estequiometria química.

---

## ⚙️ Requisits del Sistema i Instal·lació

Abans de començar, necessites tenir instal·lat **Python** al teu ordinador.

### 1. Instal·lació de Python

### 🪟 Windows Installation

1. Ves a la web oficial de [Python](https://www.python.org/downloads/) i descarrega l'última versió recomanada.
2. Durant la instal·lació, **marca obligatòriament la casella** *"Add Python to PATH"* abans de clicar a *Install Now*.

#### 🍎 macOS Installation

1. Pots instal·lar Python des del web oficial o mitjançant [Homebrew](https://brew.sh/):

   ```bash
   brew install python
   ```

---

### 2. Instal·lació de la llibreria Pygame

Un cop tinguis Python instal·lat, obre la teva terminal i instal·la la versió compatible de Pygame (`pygame-ce`):

### 🪟 Windows (System Installation)

```cmd
pip install pygame-ce
```

#### 🍎 macOS

```bash
pip3 install pygame-ce
```

---

## ▶️ Com executar l'aplicació

Per posar en marxa el programa complet en mode d'escriptori a pantalla completa:

1. Situa't amb la terminal dins de la carpeta arrel del projecte (`iaDaina`).
2. Executa el fitxer principal del controlador:

### 🪟 Windows

```cmd
python iaDaina.py
```

#### 🍎 macOS / Linux

```bash
python3 iaDaina.py
```

> **Dreceres de teclat importants:**

> - **F11**: Alterna entre el mode de pantalla completa i el mode finestra.
> - **ESC**: Tanca completament l'aplicació des de qualsevol pantalla.

---

## 📦 Generació d'Executables (.exe / .app)

Si vols convertir el programa en un fitxer executable independent (perquè s'obri fent doble clic sense necessitat de tenir Python instal·lat), pots emprar **PyInstaller**.

### 1. Instal·lar PyInstaller

- **Windows:**

  ```cmd
  pip install pyinstaller
  ```

- **macOS:**

  ```bash
  pip3 install pyinstaller
  ```

---

### 2. Crear l'executable

Situa't a la carpeta arrel del projecte i executa la comanda següent:

```bash
pyinstaller --noconsole --onefile iaDaina.py
```

> **Nota:** L'opció `--noconsole` amaga la finestra negra de la terminal de comandes, i `--onefile` empaqueta tot el projecte (incloent subcarpetes i recursos) en un únic fitxer executable autònom ubicat a la carpeta **`dist/`**.
