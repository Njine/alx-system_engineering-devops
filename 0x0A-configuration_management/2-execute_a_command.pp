# 2-execute_a_command.pp
# Puppet manifest to define an exec resource to terminate the process using pkill.

# Define the exec resource to kill the process using pkill
exec { 'killmenow':
  command => 'pkill killmenow',
  # Ensure that the process is killed only if it exists
  onlyif  => 'pgrep killmenow',
}

# Notify the user about the process termination
notify { 'Process "killmenow" terminated successfully':
  require => Exec['killmenow'],
}
