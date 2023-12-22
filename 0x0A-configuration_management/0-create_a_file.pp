# 3-create_file_manifest.pp
# Puppet manifest to create a file '/tmp/school' with specific attributes.

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
