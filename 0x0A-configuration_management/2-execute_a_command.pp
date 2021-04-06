#creating a manifest that kills a process named killmenow using exec and pkill

exec { 'pkill':
ensure  => 'stopped',
command => 'pkill -f killmenow',
}
