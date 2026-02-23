# 📚 Glosario Técnico y de Negocio: Dropshipping Data Analyzer

## 1. ⚙️ Comandos de Terminal y Entorno (En orden de uso)

* **`mkdir dropshipping_data_analyzer`**
    * **Qué hace:** Crea un nuevo directorio (carpeta) con el nombre especificado. ("mkdir" viene de *make directory*).
    * **Por qué lo usamos:** Para crear el contenedor principal de todo nuestro proyecto desde la terminal.
* **`cd dropshipping_data_analyzer`**
    * **Qué hace:** Cambia tu ubicación actual en la terminal hacia esa carpeta. ("cd" viene de *change directory*).
    * **Por qué lo usamos:** Para entrar a la carpeta y empezar a trabajar dentro de ella.
* **`code .`**
    * **Qué hace:** Abre Visual Studio Code directamente en la carpeta donde te encuentras ubicado (representada por el punto `.`).
    * **Por qué lo usamos:** Es el atajo profesional para iniciar el editor de código sin tener que buscar la carpeta en los menús.
* **`python -m venv venv`**
    * **Qué hace:** Le pide a Python que ejecute su módulo de entornos virtuales (`-m venv`) para crear una carpeta llamada `venv`.
    * **Por qué lo usamos:** Para crear una "burbuja" aislada donde instalaremos librerías, evitando que interfieran con otras herramientas de la computadora.
* **`.\venv\Scripts\activate` (Windows)**
    * **Qué hace:** Ejecuta el script de activación del entorno virtual.
    * **Por qué lo usamos:** Le dice a la terminal que, a partir de ese momento, cualquier instalación (como pandas) o ejecución de Python debe hacerse dentro de la "burbuja". Se confirma al ver `(venv)` al inicio de la línea.
* **`mkdir src`, `mkdir data`, `mkdir notebooks`**
    * **Qué hace:** Crea múltiples subcarpetas.
    * **Por qué lo usamos:** Para establecer la arquitectura estándar de un proyecto de Data Science (código fuente en `src`, datos en `data`, pruebas en `notebooks`).
* **`pip install pandas`**
    * **Qué hace:** Usa el instalador de paquetes de Python (PIP) para descargar e instalar la librería Pandas desde internet.
    * **Por qué lo usamos:** Necesitábamos las herramientas de Pandas para manipular tablas de datos (DataFrames) y calcular el Score Ganador.
* **`python main.py`**
    * **Qué hace:** Le dice al intérprete de Python que lea y ejecute todas las instrucciones dentro del archivo `main.py`.
    * **Por qué lo usamos:** Para arrancar nuestro motor de análisis, generar los datos falsos y ver los resultados en pantalla.

## 2. 🛡️ Comandos de Git (Control de Versiones)

* **`git init`**
    * **Qué hace:** Inicializa un repositorio de Git oculto en tu carpeta.
    * **Por qué lo usamos:** Es el primer paso para decirle a Git que empiece a vigilar los cambios en este proyecto.
* **`git config --global user.name "Tu Nombre"`** y **`git config --global user.email "tu@correo.com"`**
    * **Qué hace:** Registra tu identidad en el sistema Git de tu computadora.
    * **Por qué lo usamos:** Git exige saber quién es el autor de cada línea de código por motivos de seguridad y trabajo en equipo. Al usar `--global`, solo se hace una vez en la vida.
* **`git add <archivo>` o `git add .`**
    * **Qué hace:** Prepara (o "sube al escenario") los archivos modificados para el próximo guardado. El punto `.` significa "todos los archivos que no estén bloqueados por el .gitignore".
    * **Por qué lo usamos:** Le indica a Git exactamente qué partes de nuestro trabajo queremos incluir en la próxima "fotografía" del historial.
* **`git commit -m "mensaje"`**
    * **Qué hace:** Toma la "fotografía" definitiva de los archivos preparados y la guarda en el historial con una etiqueta descriptiva.
    * **Por qué lo usamos:** Para crear puntos de control seguros a los que podamos regresar si algo se rompe en el futuro.
* **`git status`**
    * **Qué hace:** Muestra un reporte en tiempo real de qué archivos han cambiado, cuáles están preparados para un commit y cuáles están siendo ignorados.
    * **Por qué lo usamos:** Para verificar que nuestro escudo (`.gitignore`) estuviera funcionando y que no fuéramos a subir archivos pesados por accidente.
* **`git commit --amend -m "nuevo mensaje"`**
    * **Qué hace:** Modifica el último commit realizado en lugar de crear uno nuevo.
    * **Por qué lo usamos:** Para corregir un error en el mensaje anterior y dejar el historial con un formato profesional (ej. usando prefijos como `refactor:` o `feat:`).

## 3. 🧠 Conceptos Generales

* **Import Circular:** Un error que ocurre cuando el "Archivo A" intenta llamar al "Archivo B", pero el "Archivo B" también está intentando llamar al "Archivo A" al mismo tiempo, creando un bucle infinito que bloquea el programa.
* **Data Sintética / Datos Dummy:** Datos falsos generados por computadora (usando la librería `random`) para probar que un programa matemático funciona antes de conectarlo a datos reales del mundo.
* **ROAS (Return On Ad Spend):** Retorno de Inversión Publicitaria. Si gastas $1 en Facebook Ads y vendes $5, tu ROAS es 5. Es la métrica más importante del marketing digital.
* **Score Ganador:** Una fórmula matemática personalizada creada en este proyecto. Pondera diferentes variables (ventas, ROAS, tendencias) para dar una calificación del 1 al 100 y decidir si un producto vale la pena.
