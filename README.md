# XBlock Estilos de Aprendizaje

Este XBlock fue creado con el fin de obtener el estilo de aprendizaje de los estudiantes de un curso de OpenEDX, para que el profesor conozca a partir de cualquiera de los test disponibles que material del curso debe subir y se ajuste a cada estilo de aprendizaje de los estudiantes.

Para comprender el funcionamiento de este XBlock, es necesario haber visto la guía de [MyXBlock](https://github.com/J4ckDev/MyXblock).

# Contenido

- [1. Test de Bandler y Grinder](##1.-Test-de-Bandler-y-Grinder)
  - 1.1 Sistema de representación Visual
  - 1.2 Sistema de representación Auditivo
  - 1.3 Sistema de representación Kinestésico
- [2. Funciones](#2.-Funciones)
- [3. Instalación](#3.-Instalación)
- [4. Modo de uso](#4.-Modo-de-uso)

<!-- [1. Características](#1-características) -->

# 1. Test de Bandler y Grinder

Este modelo, también llamado Visual-Auditivo-Kinestésico (VAK), toma en cuenta que existen tres grandes sistemas para representar mentalmente la información, el visual, el auditivo y el kinestésico. Estos sistemas se desarrollan más a medida que se utilizan, por lo que un proceso de aprendizaje en específico para una persona puede ser más eficaz en comparación con otro, además que usualmente se utilizan los sistemas de representación de forma desigual, es decir, se potencia uno mientras que otro es infrautilizado. El modelo estima que un 40\% de las personas es visual, un 30\% auditiva y un 30\% kinestésica. La clasificación de los estudiantes es definida por las siguientes características: 

## 1.1 Sistema de representación Visual
Los alumnos visuales aprenden mejor cuando leen o ven la información de alguna manera, en lugar de cuando reciben una explicación oral; tienden a absorber grandes cantidades de información debido a que su forma de pensar está basada en  imágenes, relacionando fácilmente las ideas y conceptos. Además poseen mayor capacidad de abstracción y de planificación.
    
## 1.2 Sistema de representación Auditivo
Los alumnos auditivos aprenden mejor cuando reciben las explicaciones oralmente y cuando expresan esa información a otra persona, pero no pueden equivocarse en alguna palabra porque les cuesta retomar el tema. Este sistema no permite relacionar y elaborar conceptos abstractos con la misma eficacia que el sistema visual, sin embargo, es ordenado y secuencial al momento de recordar. Es fundamental en el aprendizaje de los idiomas y de la música.
    
## 1.3 Sistema de representación Kinestésico
Los alumnos kinestésicos asocian sensaciones y movimientos con su cuerpo al momento de procesar la información, por ejemplo, al momento de aprender un deporte. Este sistema de aprendizaje es lento y requiere más tiempo a comparación de los dos sistemas anteriores pero es más profundo, ya que desarrolla la memoria muscular. Las personas kinestésicas están en constante movimiento y aprenden con la práctica, es decir, realizando laboratorios o proyectos.

# 2. Funciones

####

# 3. Instalación

Para instalar este XBlock es necesario realizar los siguientes pasos:

1. Descargue este XBlock desde el *Release* o realice un `git clone` al repositorio.
2. Si descargó desde el *Release* descomprima el archivo y cópielo a la carpeta donde tiene el entorno virtual. Sí solo realizó el `git clone`, copie la carpeta donde tiene el entorno virtual.
3. Asegurese de inicializar el entorno virtual y ejecute el comando `pip install -e adaptive_test` para instalar el Xblock en el SDK.
4. Inicie el servidor del XBlock SDK y abra la dirección `http://127.0.0.1:8000/`, si aparece el XBlock fue instalado correctamente.

# 4. Modo de uso

Inicialmente se ingresa al XBlock, en este caso el test por defecto que ve el usuario es el test de Bandler y Grinder.

1. El test consta de 40 preguntas y cada pregunta tiene tres opciones de respuesta, el usuario debe completar el test en su totalidad para poder continuar.

![Inicio_test](https://user-images.githubusercontent.com/74381298/156853820-074a2038-255c-4b0b-87ec-10b5f62cc1da.png)

2. El usuario debe contestar la totalidad de las preguntas, de lo contrario recibirá una alerta en pantalla indicando que no le permite continuar hasta realizar el test.

![alerta-error](https://user-images.githubusercontent.com/74381298/156853840-628cf5a8-66a9-4158-ab50-d1d54a5c3be7.png)

3. El usuario recibe el resultado de su test, y al acceder de nuevo, ya no observará las preguntas del mismo test sino que tendrá el resultado.

![result](https://user-images.githubusercontent.com/74381298/156853871-a2e04839-7dd0-4dd0-a430-2130b879d291.png)

