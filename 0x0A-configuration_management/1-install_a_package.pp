#installing a puppet-lint package using Puppet

package { 'puppet-lint':
ensure   => '2.1.1',
provider => 'gem',
}
