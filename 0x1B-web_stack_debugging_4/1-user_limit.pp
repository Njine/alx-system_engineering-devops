#High file opening fix

file { '/etc/security/limits.conf':
  ensure  => present,
  content => template('module_name/limits.conf.erb'),
}

service { 'systemd-logind':
  ensure => running,
  enable => true,
}

# Ensure proper ordering of changes
exec { 'replace-1':
  command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  refreshonly => true,
  path        => ['/bin', '/usr/bin'],
  notify      => Exec['replace-2'],
}

exec { 'replace-2':
  command     => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  refreshonly => true,
  path        => ['/bin', '/usr/bin'],
}

