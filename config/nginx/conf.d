upstream web {
    server localhost:8000;
}
 
server {
 
    listen 80;
    server_name localhost;
 
    location / {
        proxy_pass http://djangoapp;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
 
    location /static/ {
        alias /staticfiles/;
    }
 
}