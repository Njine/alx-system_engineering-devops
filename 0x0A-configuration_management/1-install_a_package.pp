# 1-install_a_package.pp

# Install Flask version 2.1.0 using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify the user about the installation
notify { 'Flask installed successfully':
  require => Package['Flask'],
}
