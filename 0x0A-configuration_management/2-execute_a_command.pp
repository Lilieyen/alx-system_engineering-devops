#creating a manifest that kills a process named killmenow using exec and pkill

exec { 'killmenow':
ensure  => 'stopped',
command => 'pkill',
}
