# Puppet manifest to replace PHP config files

# Define an exec resource to replace the PHP config files
exec { 'replace_php_config':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}

