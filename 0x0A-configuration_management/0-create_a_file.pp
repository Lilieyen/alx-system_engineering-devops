# create a file in /tmp using puppet

file { [ '/tmp/holberton' ]:
    ensure  => directory,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
    path    => /tmp/holberton,
}
