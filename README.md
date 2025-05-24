# Proyecto Final: Análisis de Desempeño con JMeter

![1698533386883](https://github.com/user-attachments/assets/e4c1d884-cd16-4ff3-86c7-cfdc6e934b52)

## Curso: Principios & Prácticas De Desarrollo De Software Orientado A Objetos - C1
## Instructor: Gabriel Rodrigo Pedraza Ferreira
## Universidad Industrial de Santander

## Integrantes:
- Sergio Nelson Alberto Gómez Gil - 2214106
- Juan Pablo Ávila Quitián - 2214107
- Juan David Saavedra González - 2214111

## Introducción
Este proyecto final se centra en el análisis empírico del comportamiento de una aplicación bajo distintos escenarios de despliegue, utilizando Docker Compose y Kubernetes.
Nosotros como estudiantes desplegaremos una aplicación en configuraciones que varían desde un único contenedor hasta clústeres de Kubernetes con diferentes niveles de escalabilidad (número de réplicas y nodos).

El objetivo principal es observar y cuantificar métricas de rendimiento clave, como el tiempo medio de respuesta y el throughput, bajo diferentes cargas, para luego analizar cómo el entorno de despliegue impacta en la aplicación y extraer conclusiones sobre su escalabilidad y eficiencia.

## Pasos para ejecutar el Proyecto

# 1. Para la primera fase, nos ubicamos en la carpeta tickets_3J y, una vez dentro, ejecutamos el siguiente comando:

docker-compose up

# 2. la segunda fase, nos ubicamos en la carpeta fase2_kubernetes y luego a tickets_3J, una vez dentro, ejecutamos el siguiente comando:

microk8s kubectl apply -f k8s-fase2.yaml

# 3. Para la tercera fase, nos ubicamos en la carpeta fase3_kubernetes y luego a tickets_3J, una vez dentro, ejecutamos el siguiente comando:

microk8s kubectl apply -f k8s-fase3.yaml

# 4. Para mirar los puertos expuestos para visualizar la aplicación desplegada en el navegador, usa el siguiente comando:

Para fase 2:
microk8s kubectl get svc -n tickets3j-namespace-fase2

Para fase 3:
microk8s kubectl get svc -n tickets3j-namespace

# 5. En la fase 1, para el bonus opcional, ejecuto lo siguiente estando dentro de la carpeta tickets_3J:

docker-compose down --> En caso de que esté levantado

docker-compose up -d

Para ver la memoria usada por contenedor: 
container_memory_usage_bytes y le damos a Execute
