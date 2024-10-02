#!/usr/bin/bash

# TO GIVE APACHE ACCESS TO THE SQLITE DATABASE AND THE MEDIA FOLDER
chown :www-data /blog-app/db.sqlite3
chmod 664 /blog-app/db.sqlite3
chown -R :www-data /blog-app
chmod -R 775 /blog-app

# GIVE ACCESS TO ALL FILES WITHIN THE MEDIA FOLDER
chown -R :www-data /blog-app/media
chmod -R 775 /blog-app/media
chmod -R +x /blog-app/manage.py
chown -R :www-data /blog-app/someProject
chmod -R 775 /blog-app/someProject

# systemctl reload apache2
# service apache2 restart
apache2ctl -D FOREGROUND


cd /blog-app
rm startup.sh
# python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic --no-input && python3 manage.py runserver 0.0.0.0:8000 &