#creating a manifest that kills a process named killmenow using exec and pkill

exec { 'killmenow':
command  => 'pkill -f killmenow',
provider => 'shell',
}
