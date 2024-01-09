$hostname = 'your_hostname' # Replace with the actual hostname

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('your_module/nginx.conf.erb'), # Use a template for configuration
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}


# Add the following to your Puppet module in 'templates/nginx.conf.erb':

# include "/etc/nginx/sites-enabled/*;";
# add_header X-Served-By "<%= @_hostname %>";

