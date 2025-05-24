# 📊 Proyecto Final: Análisis de Desempeño con JMeter

![Análisis de Desempeño](https://github.com/user-attachments/assets/e4c1d884-cd16-4ff3-86c7-cfdc6e934b52)

## 🎓 Curso

**Principios & Prácticas de Desarrollo de Software Orientado a Objetos - C1**

**Instructor:** Gabriel Rodrigo Pedraza Ferreira

**Universidad Industrial de Santander**

## 👥 Integrantes

* Sergio Nelson Alberto Gómez Gil - *2214106*
* Juan Pablo Ávila Quitián - *2214107*
* Juan David Saavedra González - *2214111*

---

## 🧾 Introducción

Este proyecto tiene como objetivo realizar un **análisis empírico del comportamiento de una aplicación** bajo distintos entornos de despliegue, utilizando **Docker Compose** y **Kubernetes**.

Se desplegará una misma aplicación en diferentes configuraciones:

* Un contenedor simple
* Clústeres Kubernetes con distintos niveles de escalabilidad (réplicas y nodos)

### 🎯 Objetivo

Observar y cuantificar **métricas de rendimiento clave**, como:

* Tiempo medio de respuesta
* Throughput

Estas métricas se analizarán bajo diferentes cargas para evaluar cómo el entorno de despliegue afecta el desempeño, escalabilidad y eficiencia de la aplicación.

---

## 🚀 Instrucciones de Ejecución

### 🔹 Fase 1 - Docker Compose

1. Ir a la carpeta `tickets_3J`:

   ```bash
   cd tickets_3J
   docker-compose up
   ```

### 🔹 Fase 2 - Kubernetes (microk8s)

1. Ir a la carpeta `fase2_kubernetes/tickets_3J`:

   ```bash
   cd fase2_kubernetes/tickets_3J
   microk8s kubectl apply -f k8s-fase2.yaml
   ```

### 🔹 Fase 3 - Kubernetes Escalable (microk8s)

1. Ir a la carpeta `fase3_kubernetes/tickets_3J`:

   ```bash
   cd fase3_kubernetes/tickets_3J
   microk8s kubectl apply -f k8s-fase3.yaml
   ```

---

## 🌐 Visualización en el Navegador

Para obtener los puertos expuestos y acceder a la aplicación:

* **Fase 2**:

  ```bash
  microk8s kubectl get svc -n tickets3j-namespace-fase2
  ```

* **Fase 3**:

  ```bash
  microk8s kubectl get svc -n tickets3j-namespace
  ```

---

## 🛠️ Bonus Opcional (Fase 1)

1. Ir a la carpeta `tickets_3J`:

   ```bash
   cd tickets_3J
   docker-compose down  # Solo si ya está en ejecución
   docker-compose up -d
   ```

2. Para monitorear el uso de memoria por contenedor (vía Prometheus o herramienta similar), utilizar:

   ```
   container_memory_usage_bytes
   ```

   Luego, haz clic en **Execute** para visualizar los resultados.

---

## 📁 Estructura del Proyecto

```
├── fase1_docker_compose/
│   └── tickets_3J/
├── fase2_kubernetes/
│   └── tickets_3J/
│       └── k8s-fase2.yaml
├── fase3_kubernetes/
│   └── tickets_3J/
│       └── k8s-fase3.yaml
└── README.md
```
