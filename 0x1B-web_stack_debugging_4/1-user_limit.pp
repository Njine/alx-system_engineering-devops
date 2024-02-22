# Puppet manifest to fix the problem of a high number of files opened

# Replace the 'nofile' limit with 50000
exec { 'replace_nofile_1':
  command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path     => '/bin:/usr/bin',
  before   => Exec['replace_nofile_2'],
}

# Replace the 'nofile' limit with 40000
exec { 'replace_nofile_2':
  command  => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path     => '/bin:/usr/bin',
}

