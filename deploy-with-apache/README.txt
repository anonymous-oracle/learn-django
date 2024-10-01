SINCE NGINX WILL BE RUNNING MANUALLY EDIT THE /etc/apache2/ports.conf AND /etc/apache2/sites-available/000-default.conf ACCORDINGLY FOR APACHE SERVER ON THE CONTAINER
FOR DIGEST AUTH 
CHECK FOR EITHER /etc/httpd OR /etc/apache2
CHECK WHETHER /etc/apache2/mods-available/auth_digest.load EXISTS
COPY THE FILE TO /etc/apache2/mods-enabled/auth_digest.load

IN THE /etc/apache2/apache2.conf FILE ADD THE FOLLOWING LINES


# <Location /admin>
# AuthType Digest # TYPE OF AUTHENTICATION TO USE, HERE IT IS DIGEST BASED AUTHENTICATION
# AuthName "learn-nginx" # NAME OF THE AUTHENTICATION REALM, NAMED AFTER THE LEARN-NGINX MODULE
# AuthDigestDomain /admin/ # SPECIFIES THE DOMAIN FOR WHICH THE AUTHENTICATION IS VALID, CREDENTIALS ARE ONLY VALID FOR THIS ROUTE
# AuthDigestProvider file # SPECIFIES THE PROVIDER FOR THE AUTHENTICATION, HERE IT IS FILE BASED
# AuthUserFile /etc/apache2/.htdigest # SPECIFIES THE FILE CONTAINING THE USER CREDENTIALS 
# Require valid-user # SPECIFIES THAT ONLY USERS PRESENT IN THE AUTHUSERFILE ARE ALLOWED TO ACCESS THE ROUTE
# </Location>

<Location /admin>
AuthType Digest 
AuthName "learn-nginx"
AuthDigestDomain /admin/ 
AuthDigestProvider file
AuthUserFile /etc/apache2/.htdigest
Require valid-user
</Location>

# CREATE THE .HTDIGEST FILE WITH LEARN-NGINX AS THE REALM AND ADMIN AS THE USER BEING ADDED FIRST
# htdigest -c .htdigest learn-nginx admin

IN /etc/apache2/sites-enabled DIRECTORY ADD A .conf FILE BY REFERRING THE APACHE2 DOCUMENTATION WHERE A ROUTE SPECIFIC .html FILE IS PRESENT