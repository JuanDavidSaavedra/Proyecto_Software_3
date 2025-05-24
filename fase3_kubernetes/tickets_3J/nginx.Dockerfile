# nginx.Dockerfile
FROM nginx:alpine

# Quitar config por defecto
RUN rm /etc/nginx/conf.d/default.conf

# Copiar el nuevo config
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Copiar archivos estáticos y media
COPY staticfiles/ /usr/share/nginx/html/static/
COPY media/ /usr/share/nginx/html/media/
