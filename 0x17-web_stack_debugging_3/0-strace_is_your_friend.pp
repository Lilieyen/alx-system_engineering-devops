# fix issue of Apache returning a 500 error

exec { 'fix misprint error':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
