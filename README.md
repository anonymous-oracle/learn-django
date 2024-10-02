# learn-django
trying out django

workaround for LoginView view class is to add a small 'POST' form in the navbar section

TO ENABLE THE SITE ON DJANGO APP
sudo a2ensite django-blog-app

TO DISABLE DEFAULT APACHE CONF
sudo a2dissite 000-default.conf

TO GIVE APACHE ACCESS TO THE SQLITE DATABASE AND THE MEDIA FOLDER
sudo chown :www-data django-blog-app/db.sqlite3
sudo chmod 664 django-blog-app/db.sqlite3
sudo chown :www-data django-blog-app
sudo chmod 775 django-blog-app

GIVE ACCESS TO ALL FILES WITHIN THE MEDIA FOLDER
sudo chown -R :www-data django-blog-app/media
sudo chmod -R 775 django-blog-app/media

apg IS A COMMAND-LINE UTILITY FOR GENERATING STRONG, RANDOM PASSWORDS. YOU CAN INSTALL IT ON MOST LINUX DISTRIBUTIONS. HERE’S AN EXAMPLE:
apg -l 32

OR

openssl rand -base64 -hex 32

SETUP APACHE SERVER USING THIS LINK
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/modwsgi/

SETUP NGINX SERVER USING THIS LINK
https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html