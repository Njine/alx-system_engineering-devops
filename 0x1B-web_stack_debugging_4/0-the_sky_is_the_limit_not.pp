# Puppet manifest to update Nginx configuration and restart the service
# 
# Description:
# This manifest updates the configuration file '/etc/default/nginx' by replacing occurrences of "15" with "1000"
# and then restarts the Nginx service.
# Compatibility: Ubuntu 14.04 LTS, Puppet v3.4

file { '/etc/default/nginx':
  ensure  => file,
  content => template('module_name/nginx_config.erb'),
  notify  => Exec['nginx_restart'],
}

exec { 'nginx_restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}

