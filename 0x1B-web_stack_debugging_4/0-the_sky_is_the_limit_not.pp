# Puppet manifest to fix the problem of a high number of files opened

# Replace the 'nofile' limit with 50000
augeas { 'nofile_50000':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set *[@*="root" and @type="hard"]/nofile "50000"',
    'set *[@*="root" and @type="soft"]/nofile "50000"',
  ],
}

# Replace the 'nofile' limit with 40000
augeas { 'nofile_40000':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set *[@*="root" and @type="hard"]/nofile "40000"',
    'set *[@*="root" and @type="soft"]/nofile "40000"',
  ],
}

