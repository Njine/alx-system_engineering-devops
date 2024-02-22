# Puppet manifest to update Nginx configuration and restart the service

# Manage Nginx configuration file
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }

