# Proyecto Integrador Unidad 1: Formulario con Flet y Control de Versiones con Git Bash

En el desarrollo del presente proyecto integrador correspondiente a la Unidad 1, se llevó a cabo la implementación de una aplicación de registro de estudiantes utilizando la librería Flet, la cual permite construir interfaces gráficas modernas empleando el lenguaje de programación Python y ejecutarlas directamente en un navegador web sin necesidad de desarrollar código frontend tradicional (HTML, CSS o JavaScript).

Adicionalmente, se utilizó Git Bash como herramienta de control de versiones, lo que permitió gestionar de manera eficiente el código fuente del proyecto, registrar cambios, mantener un historial de versiones y facilitar la entrega mediante un repositorio remoto. Esta combinación de tecnologías permitió simular un flujo de trabajo real utilizado en entornos de desarrollo profesional.

## 1. Entorno de Desarrollo y Ejecución

Para el desarrollo del proyecto se utilizó el editor de código Visual Studio Code, el cual proporcionó un entorno cómodo, organizado y eficiente para escribir, depurar y ejecutar el código.

La ejecución del programa se realizó mediante la terminal de Git Bash, donde previamente se configuró un entorno virtual (.venv). Este entorno virtual es importante, ya que permite aislar las dependencias del proyecto, evitando conflictos con otras librerías instaladas en el sistema.

El proceso general de ejecución fue el siguiente:
<img width="930" height="263" alt="image" src="https://github.com/user-attachments/assets/f26f53cd-130c-49ad-94e1-cc44a52342f1" />

 
1.	Activación del entorno virtual.
2.	Instalación de la librería Flet.
3.	Ejecución del programa mediante el comando:

<img width="856" height="76" alt="image" src="https://github.com/user-attachments/assets/1a3772e3-d83b-4d9e-b03e-f8af57bd0947" />



Este comando permite levantar la aplicación en un servidor local, generando automáticamente una dirección tipo localhost, la cual se abre en el navegador para visualizar la interfaz gráfica.

Este proceso demuestra la integración entre herramientas de desarrollo, ejecución en entorno web y administración de dependencias, aspectos fundamentales en el desarrollo moderno de software.

## 2. Descripción General del Funcionamiento del Sistema

El sistema desarrollado consiste en un formulario digital de registro de estudiantes, cuyo propósito es capturar, validar y mostrar información ingresada por el usuario de manera estructurada.

El diseño del formulario fue pensado para ser intuitivo, visualmente organizado y fácil de usar. Para ello, se implementaron diferentes tipos de controles que mejoran la interacción con el usuario.

Datos que captura la aplicación:
  -	Nombre: Campo de texto libre para ingresar el nombre del estudiante.
  -	Número de control: Identificador único del alumno.
  -	Correo electrónico: Campo que incluye validación básica de formato.
  -	Carrera: Seleccionada mediante un menú desplegable (Dropdown).
  -	Semestre: También mediante Dropdown, generado dinámicamente.
  -	Género: Seleccionado a través de botones tipo RadioGroup.

Cada uno de estos elementos cumple una función específica dentro del formulario, asegurando una captura de datos estructurada y evitando ambigüedades.


## 3. Estructura y Diseño de la Interfaz
Uno de los aspectos más importantes del proyecto fue el diseño de la interfaz gráfica. Se configuró un estilo visual limpio y profesional utilizando:
 
<img width="863" height="136" alt="image" src="https://github.com/user-attachments/assets/8afced56-e4c0-46c1-87be-43ff5f7092f0" />

  -	Color de fondo claro (#FDFBE3)
  -	Contenedor con fondo diferenciado (#EFE6C8)
  -	Bordes redondeados para mejorar la estética
  -	Distribución centrada en pantalla
El formulario se organizó mediante estructuras como:
  -	Column (Columna): para acomodar los elementos verticalmente
  -	Row (Fila): para colocar los Dropdown en la misma línea
  -	Container: para agrupar y estilizar el formulario completo
Este tipo de organización mejora la legibilidad del diseño y facilita futuras modificaciones.

## 4. Análisis Detallado del Código
El código fue estructurado en bloques funcionales para mejorar su comprensión y mantenimiento.

### A. Configuración Inicial
Se define el comportamiento general de la página:
  -	Título de la aplicación
  -	Color de fondo
  -	Tema visual
  -	Alineación de los elementos
Esto permite que la interfaz tenga una presentación consistente y profesional desde el inicio.



### B. Creación de Controles
Cada campo del formulario se construye utilizando componentes de Flet.
#### Campos de texto (TextField)
Se utilizan para capturar datos libres como nombre, número de control y correo electrónico. Se personalizan con:
  -	Etiquetas descriptivas
  -	Colores de borde
  -	Tamaño uniforme
####  Dropdown (Listas desplegables)
Se implementaron dos Dropdown:
  -	Carrera: con opciones predefinidas
  -	Semestre: generado dinámicamente con la instrucción:

<img width="873" height="89" alt="image" src="https://github.com/user-attachments/assets/3eb0c506-5947-4c67-b841-75b17fc4ce14" />



Este enfoque evita repetir código y demuestra el uso de programación eficiente mediante listas por comprensión.
 <img width="917" height="487" alt="image" src="https://github.com/user-attachments/assets/3ab5ea44-c811-4890-b18e-3129f64bd4ca" />




#### RadioGroup (Selección de género)
Este control permite seleccionar únicamente una opción entre varias. Es ideal para datos categóricos como el género, donde solo se permite una elección.


<img width="418" height="466" alt="image" src="https://github.com/user-attachments/assets/d2b94115-958b-41a4-9350-611f75f53c1e" />

<img width="395" height="482" alt="image" src="https://github.com/user-attachments/assets/e3ea617a-721d-40cf-8274-fa82f77db9a1" />





### C. Lógica del Sistema (Función enviar_click)
Esta función representa el núcleo del sistema, ya que controla todo el flujo de validación y procesamiento de datos.

## 1. Validación de campos vacíos
Se verifica que todos los campos contengan información. Esta validación es fundamental para evitar registros incompletos.
Se utiliza un condicional if que verifica si el valor de algún campo es nulo o vacío. Si falta algún dato, se muestra un mensaje de advertencia en rojo.
 <img width="875" height="114" alt="image" src="https://github.com/user-attachments/assets/f3525c53-2117-4e89-a43e-2126e3af4c1c" />

Si algún campo está vacío:
  -	Se muestra un mensaje de advertencia
  -	El mensaje aparece en color rojo
  -	Se detiene el proceso de envío
 

<img width="898" height="477" alt="image" src="https://github.com/user-attachments/assets/792797ee-08b9-45ac-9997-c7b7a42a361f" />

## 2. Validación del correo electrónico
Se implementa una validación básica que verifica la presencia del símbolo @.
Aunque es una validación simple, cumple con el objetivo de evitar errores comunes en la captura de correos electrónicos.

 <img width="900" height="478" alt="image" src="https://github.com/user-attachments/assets/721b7dbb-a3cf-4b12-934a-444fdb3b3645" />






## 3. Confirmación de registro exitoso
Si todas las validaciones se cumplen:
  -	Se genera un mensaje con todos los datos capturados
  -	Se muestra en color verde
  -	Se confirma visualmente el éxito del registro
Se utiliza el formato f-string, lo cual permite insertar variables dentro del texto de forma clara y eficiente.
 
<img width="918" height="488" alt="image" src="https://github.com/user-attachments/assets/f9cb575c-ee50-460b-88a7-e0e02304990e" />


## 4. Limpieza del formulario
Después de un registro exitoso:
  -	Todos los campos se reinician
  -	Los Dropdown se restablecen
  -	El RadioGroup se limpia
Esto permite ingresar nuevos datos sin necesidad de recargar la aplicación.




## 5. Actualización de la interfaz
El método:

<img width="849" height="87" alt="image" src="https://github.com/user-attachments/assets/a0453060-ecb3-47db-b1df-8fec1cd0f1f1" />


es esencial, ya que refleja todos los cambios realizados en la interfaz gráfica.

#### D. Botón de Envío
El botón tipo ElevatedButton actúa como disparador del evento principal. Al hacer clic, ejecuta la función enviar_click, conectando así la interfaz con la lógica del programa.

<img width="634" height="81" alt="image" src="https://github.com/user-attachments/assets/272641d1-3850-424b-b884-fc272bbecd01" />



## 5. Experiencia del Usuario y Retroalimentación Visual
Un aspecto importante del proyecto fue mejorar la interacción con el usuario mediante retroalimentación inmediata:
  -	Mensajes en rojo: indican errores o datos faltantes
  -	Mensajes en verde: confirman acciones exitosas
  -	Limpieza automática: mejora la fluidez del uso
Aunque en este proyecto los resultados se muestran dentro del mismo formulario mediante un control Text, también se podría implementar una ventana modal (AlertDialog) para mostrar los datos de forma emergente, lo cual representaría una mejora adicional en la experiencia del usuario.

## 6. Control de Versiones con Git Bash
El uso de Git Bash permitió:
  -	Inicializar el repositorio (git init)
  -	Registrar cambios (git add, git commit)
  -	Subir el proyecto a GitHub (git push)
Esto garantiza un respaldo del proyecto y facilita su entrega mediante una URL pública.

##  7. Conclusión
Este proyecto integrador permitió aplicar de manera práctica diversos conceptos fundamentales del desarrollo de software, tales como:

  -	Creación de interfaces gráficas con Python
  -	Uso de componentes interactivos
  -	Validación de datos
  - Manejo de eventos
  -	Organización del código
  -	Uso de control de versiones
  
Además, se logró desarrollar una aplicación funcional, clara y estructurada, que simula un sistema real de registro de estudiantes. La implementación de validaciones y controles interactivos mejora significativamente la calidad del software y la experiencia del usuario.
En conclusión, este proyecto representa una base sólida para el desarrollo de aplicaciones más complejas, integrando tanto aspectos técnicos como buenas prácticas de desarrollo.

