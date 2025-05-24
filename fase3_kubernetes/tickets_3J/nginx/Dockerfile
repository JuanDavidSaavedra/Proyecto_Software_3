FROM nginx:alpine

# Elimina el archivo por defecto de configuración
RUN rm /etc/nginx/conf.d/default.conf

# Copia tu configuración personalizada
COPY nginx.conf /etc/nginx/conf.d
COPY staticfiles/ /usr/share/nginx/html/static/
COPY media/ /usr/share/nginx/html/media/


# Crea carpetas para archivos estáticos y media
RUN mkdir -p /usr/share/nginx/html/static /usr/share/nginx/html/media

# Expone el puerto 80
EXPOSE 80
