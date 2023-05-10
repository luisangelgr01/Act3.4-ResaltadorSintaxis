# Resaltador de sintaxis utilizando Python (RE y Flask)

### Instrucciones para generar aplicación web y cómo usarla

1. Descargar el archivo "app.py" y el "sample.txt" localmente.
2. Guardar ambos archivos en una nueva misma carpeta.
3. Crear un Envirnment con .venv (ambiente virtual) para el programa de Python.  
    3.1 Esto se puede realizar abriendo la carpeta desde Visual Studio Code, abrir desde ahi la ventana de "Command Palette" (en Mac se abre
    presionando Command+Shift+p). Después selecciona "Pyhton: Create Environment...", y finalmente seleccionando ".venv" (esto deberia de
    crear una carpeta llamada ".venv" dentro de la carpeta en la que se esta trabajando con más componentes dentro). Esto deberia ser 
    posible si Python fue instaldo correctamente en Visual Studio Code.
4. Instalar la libreria de Flask en la carpeta donde se encuentra el archivo "app.py".  
    4.1 Esto se puede lograr abriendo una terminal nueva con la dirección de la carpeta de donde se esta trabajando. En la terminal correr 
    el siguiente comando: "python -m pip install flask".
5. Una vez se tenga esto preparado, ya es posible correr el programa de Python "app.py". Sin embargo, puedes en este momento dejar preparado el archivo de texto "sample.txt" modificado y guardado con las lineas de código que se desee analizar y resaltar la sintaxis, usando las convenciones de Python. Una vez se tenga el texto por analizar, se guarda dónde está.
6. Correr, ahora sí, el programa de "app.py"
7. Abrir un navegador e ingresar a la siguiente dirección del localhost: "http://127.0.0.1:5000/generate_html_css". Esto generara un archivo de html llamado "output.html".
8. Después, dentro del navegador ingresar a esta tra dirección del localhost: "http://127.0.0.1:5000/view_html_css". Esto abrira la página html donde se visualiza el resaltador de sintaxis.  
    8.1 Alternativamente, una vez se haya generado el archivo de "output.html", es posible abrirlo directamente con el navegador desde la 
    carpeta donde esta guardado sin la necesidad del localhost (donde esta corriendo la aplicación web)
9. Si se requiere analizar otro texto y resaltar sintaxis de otras líneas de código de Python, se tiene que reescribir y guardar el archivo de "sample.txt" con esas otras líneas por resaltar, después se tiene que volver a generar el html corriendo la función, la cual está definida en el "app.py" que se puede acceder cuando la aplicación esta corriendo correctamente e ingresando a la dirección web con extensión "/generate_html_css", o si simplemente se corre esta función por separado en cualquier archivo de python separado. Así se genera un nuevo archivo html con el resaltador del texto deseado. Este archivo puede ser abierto desde un navegador como se cualquier navegador como se explico en el paso 8.1.
10. Si la aplicación de Flask (el archivo "app.py") sigue corriendo, se puede detener desde la terminal ingresando CTRL+C. Para volver a correrla solo hace falta realizar de nuevo los pasos 5 al 9
