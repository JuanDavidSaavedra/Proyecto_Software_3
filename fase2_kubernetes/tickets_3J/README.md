# Guía rápida: Conservar tus datos en Docker (para tickets_3J)

## 🚫 Evitar perder datos

Para que **no se borren los datos** (eventos, usuarios, imágenes, etc.) al apagar tu proyecto:

### ✅ Usa este comando:
```bash
docker-compose down
```
Este comando **detiene los contenedores**, pero **conserva los volúmenes** (la base de datos y archivos).

---

### ❌ NUNCA uses esto si no quieres perder datos:
```bash
docker-compose down -v
```
Esto **borra también los volúmenes**. Es decir: **todos los datos se eliminan** (base de datos, media, etc.).

---

## 🚀 Para volver a levantar el proyecto
```bash
docker-compose up -d
```
Esto volverá a iniciar todo con los datos anteriores intactos (si usaste `down` sin `-v`).

---

## 🤔 ¿Y si ya usaste `-v` por error?
Tus datos se perdieron. Lo ideal es:
- Hacer un **backup** de la base de datos.
- Guardar tus **archivos media/static** si son importantes.

---

## 📅 Recomendación:
Antes de usar `docker-compose down -v`, asegúrate de que **realmente quieres borrar todo**. Si solo quieres reiniciar o reconstruir, usa:
```bash
docker-compose down && docker-compose up -d --build
```

---

**Proyecto:** `tickets_3J`

**Autor:** *(Tu nombre o grupo)*
