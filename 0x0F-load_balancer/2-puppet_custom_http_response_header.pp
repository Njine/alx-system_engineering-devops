# Installs Nginx server with custom HTTP header

exec { 'update':
  command => 'sudo apt-get -y update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('your_module/nginx.conf.erb'), # Make sure to replace with the correct template path
  notify  => Exec['add_header'],
}

exec { 'add_header':
  command => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
  require     => Package['nginx'],
  notify      => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  refreshonly => true,
  subscribe   => Exec['add_header'],
}

