#creating a manifest that kills a process named killmenow using exec and pkill

exec { 'pkill':
command  => 'pkill -f killmenow',
provider => 'shell',
}
