# XBlock-Estilos-de-Aprendizaje

Este XBlock fue creado con el fin de obtener el estilo de aprendizaje de los estudiantes de un curso de OpenEDX, para que el profesor conozca a partir de cualquiera de los test disponibles que material del curso debe subir y se ajuste a cada estilo de aprendizaje de los estudiantes.

Para comprender el funcionamiento de este XBlock, es necesario haber visto la guía de [MyXBlock](https://github.com/J4ckDev/MyXblock).

# Contenido
- [Contenido](#contenido)
- [1. Test de Bandler y Grinder](#1-Test-de-Bandler-y-Grinder)
  - [1.1 Sistema de representación Visual](#11-sistema-de-representación-visual)
  - [1.2 Sistema de representación Auditivo](#12-sistema-de-representación-visual)
  - [1.3 Sistema de representación Kinestésico](#13-sistema-de-representación-visual)
- [2. Instalación](#2-Instalación)
- [3. Modo de uso](#3-Modo-de-uso)
- [4. Resultados del test de estilos de aprendizaje de Bandler & Grinder](#4-resultados-del-test-de-estilos-de-aprendizaje-de-bandler--grinder)
  - [4.1 Prerrequisitos](#41-prerrequisitos)
  - [4.2 Posibles Resultados](#42-posibles-resultados)
  - [4.3 Modo de Uso](#3-modo-de-uso)
    - [4.3.1 Vista Docente](#431-vista-docente)
    - [4.3.2 Vista Estudiante](#432-vista-estudiante)
  - [4.4. Gestor de reglas](#44-gestor-de-reglas)
    - [4.4.1 Vista Reglas Maestro](#441-vista-reglas-maestro)
    - [4.4.2 Vista Reglas Estudiante](#442-vista-reglas-estudiante)

<!-- [1. Características](#1-características) -->

# 1. Test de Bandler y Grinder

Este modelo, también llamado Visual-Auditivo-Kinestésico (VAK), toma en cuenta que existen tres grandes sistemas para representar mentalmente la información, el visual, el auditivo y el kinestésico. Estos sistemas se desarrollan más a medida que se utilizan, por lo que un proceso de aprendizaje en específico para una persona puede ser más eficaz en comparación con otro, además que usualmente se utilizan los sistemas de representación de forma desigual, es decir, se potencia uno mientras que otro es infrautilizado. El modelo estima que un 40\% de las personas es visual, un 30\% auditiva y un 30\% kinestésica. La clasificación de los estudiantes es definida por las siguientes características: 

## 1.1 Sistema de representación Visual
Los alumnos visuales aprenden mejor cuando leen o ven la información de alguna manera, en lugar de cuando reciben una explicación oral; tienden a absorber grandes cantidades de información debido a que su forma de pensar está basada en  imágenes, relacionando fácilmente las ideas y conceptos. Además poseen mayor capacidad de abstracción y de planificación.
    
## 1.2 Sistema de representación Auditivo
Los alumnos auditivos aprenden mejor cuando reciben las explicaciones oralmente y cuando expresan esa información a otra persona, pero no pueden equivocarse en alguna palabra porque les cuesta retomar el tema. Este sistema no permite relacionar y elaborar conceptos abstractos con la misma eficacia que el sistema visual, sin embargo, es ordenado y secuencial al momento de recordar. Es fundamental en el aprendizaje de los idiomas y de la música.
    
## 1.3 Sistema de representación Kinestésico
Los alumnos kinestésicos asocian sensaciones y movimientos con su cuerpo al momento de procesar la información, por ejemplo, al momento de aprender un deporte. Este sistema de aprendizaje es lento y requiere más tiempo a comparación de los dos sistemas anteriores pero es más profundo, ya que desarrolla la memoria muscular. Las personas kinestésicas están en constante movimiento y aprenden con la práctica, es decir, realizando laboratorios o proyectos.

# 2. Instalación

Para instalar este XBlock es necesario realizar los siguientes pasos:

1. Descargue este XBlock desde el *Release* o realice un `git clone` al repositorio.
2. Si descargó desde el *Release* descomprima el archivo y cópielo a la carpeta donde tiene el entorno virtual. Sí solo realizó el `git clone`, copie la carpeta donde tiene el entorno virtual.
3. Asegurese de inicializar el entorno virtual y ejecute el comando `pip install -e adaptive_test` para instalar el Xblock en el SDK.
4. Inicie el servidor del XBlock SDK y abra la dirección `http://127.0.0.1:8000/`, si aparece el XBlock fue instalado correctamente.

# 3. Modo de uso

Inicialmente se ingresa al XBlock, en este caso el test por defecto que ve el usuario es el test de Bandler y Grinder.

1. El test consta de 40 preguntas y cada pregunta tiene tres opciones de respuesta, el usuario debe completar el test en su totalidad para poder continuar.

![Inicio_test](https://user-images.githubusercontent.com/74381298/156853820-074a2038-255c-4b0b-87ec-10b5f62cc1da.png)

2. El usuario debe contestar la totalidad de las preguntas, de lo contrario recibirá una alerta en pantalla indicando que no le permite continuar hasta realizar el test.

![alerta-error](https://user-images.githubusercontent.com/74381298/156853840-628cf5a8-66a9-4158-ab50-d1d54a5c3be7.png)

3. El usuario recibe el resultado de su test, y al acceder de nuevo, ya no observará las preguntas del mismo test sino que tendrá el resultado.

# 4. Resultados del test de estilos de aprendizaje de Bandler & Grinder

Para una correcta interpretación de los resultados que arroja el test de Bandler y Grinder implementado, se realiza una representación gráfica de dichos resultados.

## 4.1 Prerrequisitos

Se requiere que al menos un estudiante haya diligenciado por completo el test de Bandler y Grinder y adicionalmente, haya seleccionado la opción “enviar” con el objetivo de presentar el resultado obtenido, y del mismo modo el docente pueda observar los resultados de los estudiantes que han llenado el test.

## 4.2 Posibles Resultados

Además de los tres grandes tipos de dominancia correspondientes a: visual, auditivo y kinestésico se pueden presentar casos en los cuales un estudiante presente el mismo porcentaje en dos tipos. Por lo anterior, existen 6 posibles resultados, presentados a continuación: 

- Visual
- Auditivo
- Kinestésico
- Visual-Auditivo
- Visual-Kinestésico
- Auditivo-Kinestésico

## 4.3 Modo de Uso

### 4.3.1 Vista Docente

Para visualizar los resultados de los estudiantes desde la vista diseñada para el docente, es necesario seleccionar la opción “Vista Studio Analytics”. Esto despliega una nueva interfaz, tal y como se muestra en las siguientes imágenes.  

En esta interfaz, el docente puede visualizar una tabla con el ID del estudiante, el nombre del test que ha diligenciado y el resultado obtenido. Para este caso, se presenta el tipo de dominancia del estudiante y los porcentajes asociados a cada uno de ellos (Visual, Auditivo y Kinestésico).

Para visualizar las gráficas, se debe seleccionar la opción “Mostrar Gráficas”, la cual presenta automáticamente dos gráficas generadas de acuerdo a los resultados obtenidos. En la parte derecha se muestra un gráfico circular, en términos de porcentajes, que clasifica la cantidad de estudiantes que hacen parte de las dominancias. En la parte izquierda se presenta un gráfico de barras, que permite determinar el total de estudiantes pertenecientes a cada dominancia. 

![Tabla de Resultados](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/res_tabla.png)

![Grafica de Resultados](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/res_grafs.png)

### 4.3.2 Vista Estudiante

El estudiante visualiza la interfaz principal que contiene las 40 preguntas correspondientes al test que se ha seleccionado previamente, en este caso es Bandler-Grinder.

Al completar todo el test, para visualizar el resultado obtenido, se debe seleccionar la opción “Enviar”. Esto despliega inmediatamente una interfaz en donde se indican los 3 tipos de dominancia: Visual, Auditiva y Kinestésica, seguido del porcentaje determinado de acuerdo a las respuestas del test, ordenadas en forma descendente.

![Resultado de estudiante](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/res_est1.jpg)

En la parte inferior de la interfaz, se presenta una gráfica de barras complementaria que indica los porcentajes obtenidos de cada una de las tres dominancias (Visual, Auditivo y Kinestésico) en el eje Y y los tipos de dominancia sobre el eje X.

![Grafica de estudiante](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/res_est2.jpg)

Finalmente solo está habilitada la opción “Vista Studio Analytics” que redirige a la vista docente.

## 4.4 Gestor de reglas
Para la implementación de las reglas se hace uso de cohortes, donde se dividirán los estudiantes en grupos pequeños, estos grupos serán conformados según los resultados obtenidos en el test de aprendizaje, de esta forma los estudiantes tendrán un aprendizaje personalizado dependiendo de su estilo de aprendizaje y a su vez tendrán acceso a recursos que se enfoquen a su cohorte asignada, los cuales serán subidos, editados y/o controlados por el maestro.

Al observar los resultados, se podrá acceder a dos vistas diferentes, las cuales son: vista reglas maestro y vista reglas estudiantes.

### 4.4.1 Vista Reglas Maestro

Inicialmente la interfaz consta de la selección del tipo de archivo que se subirá, el usuario, en este caso el maestro, deberá seleccionar una opción para poder continuar. 

![Reglas maestro](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/reg_maes.jpeg)

Continuando se desplegará una interfaz donde el usuario deberá cargar el archivo y seleccionar la cohorte a la cual enviará este, por ultimo presionar al botón subir donde obtendrá un mensaje que dirá “Recurso subido exitosamente”, lo cual indica que se siguieron los pasos correctamente.

![Seleccion maestro](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/selec_maes.jpeg)

Nota: Al seleccionar un tipo de archivo, se le sugerirá una cohorte que más convenga con este, pero el usuario tiene la opción de cambiarla, pero siempre debe seleccionar una dado que el no hacerlo no permitirá la subida del archivo.

### 4.4.2 Vista Reglas Estudiante

En esta interfaz el usuario estudiante observara los resultados obtenidos realizado el test, la cohorte a la que ha sido asignado dado estos resultados y los recursos que se encuentran disponibles para él y donde puede acceder a ellos.

![Reglas estudiante](https://raw.githubusercontent.com/LauraMamian/XBlock-Estilos-de-aprendizaje/grupo3/img/reg_est.jpeg)