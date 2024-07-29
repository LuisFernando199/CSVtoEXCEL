# CSV a XLSX y Viceversa - Convertidor Web

Este proyecto es una aplicación web simple desarrollada con Flask que permite a los usuarios convertir archivos CSV a XLSX y viceversa. La aplicación proporciona una interfaz web para cargar archivos y convertirlos automáticamente.

## Descripción

### Pasos para utilizar la aplicación

1. **Carga de Archivos**:
   - Dirígete a la carpeta de archivos y arrastra un archivo CSV o XLSX.

2. **Cambio de Nombre de Archivo**:
   - Cambia la variable `nombre_archivo` en el código por el nombre de tu archivo.

3. **Ejecución del Código**:
   - Ejecuta las pestañas de código proporcionadas y actualiza la página para ver el resultado.

## Dependencias

Puedes instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto incluye los siguientes archivos:

- `app.py`: El script principal de la aplicación Flask.
- `templates/index.html`: El archivo HTML para la interfaz web.
- `static/styles.css`: El archivo CSS para estilos básicos de la interfaz.


## Uso

1. Clona este repositorio y navega a la carpeta del proyecto.
2. Asegúrate de tener todas las dependencias instaladas.
3. Ejecuta la aplicación Flask:

```bash
python app.py
```

4. Abre tu navegador web y dirígete a `http://localhost:5000`.
5. Carga un archivo CSV o XLSX y haz clic en "Convertir" para obtener el archivo convertido.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.


Con estos pasos y archivos, deberías poder configurar y ejecutar la aplicación web para convertir archivos CSV a XLSX y viceversa fácilmente.
