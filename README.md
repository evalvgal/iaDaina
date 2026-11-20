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
