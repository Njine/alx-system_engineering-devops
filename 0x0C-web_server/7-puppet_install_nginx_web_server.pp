exec { 'install_nginx':
  command => 'sudo apt-get -y update && sudo apt-get -y install nginx',
  path    => '/usr/bin:/usr/sbin:/bin',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.nginx-debian.html index.html index.htm;
    location /redirect_me {
        rewrite ^/redirect_me https://github.com/luischaparroc permanent;
    }
}",
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/www/html/index.nginx-debian.html', '/etc/nginx/sites-available/default'],
}
