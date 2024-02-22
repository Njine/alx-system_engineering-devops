# Puppet manifest to update Nginx configuration and restart the service

# Manage Nginx configuration file
file { '/etc/default/nginx':
  ensure  => file,
  content => template('module_name/nginx_config.erb'),
  notify  => Exec['nginx_restart'], # Trigger Nginx restart when the file changes
}

# Restart Nginx service
exec { 'nginx_restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true, # Ensure the command runs only when the Nginx configuration changes
}

