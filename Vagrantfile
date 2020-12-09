 # -*- mode: ruby -*-
# vi: set ft=ruby :

# set default values
ansible_roles_path = '/data/roles'

Vagrant.configure('2') do |config|

  # configure vagrant-proxyconf plugin
  # If proxy is configured via ENV variables
  # then we configure vagrant to use proxy
  unless ENV['http_proxy'].nil?
  config.proxy.enabled  = true
    # set values from environmental variables
  config.proxy.http     = ENV['http_proxy']
  config.proxy.https    = ENV['http_proxy']
  config.proxy.no_proxy = ENV['no_proxy']
  end

  config.vm.network 'forwarded_port', guest: 80, host: 8080
  config.ssh.insert_key = false

  config.vm.synced_folder '.',
                          '/vagrant',
                          mount_options: ['dmode=775,fmode=644']
  config.vm.box = 'bento/centos-7.8'

  config.vm.provision "Set permissions to #{ansible_roles_path}",
                      type: :shell,
                      inline: "mkdir -vp #{ansible_roles_path} ;
                               chmod o+w #{ansible_roles_path}"

  config.vm.box_download_insecure = true
  config.vm.provision 'ansible_local' do |ansible|
    ansible.install_mode = "pip"
    ansible.galaxy_roles_path = ansible_roles_path
    ansible.galaxy_role_file = "/vagrant/requirements.yml"
    ansible.playbook = "/vagrant/provision_me.yml"
    ansible.version = "2.9.15"
    ansible.verbose = 'v'
  end

  config.vm.provider 'virtualbox' do |v|
#    v.memory = 2048
# My PC RAM = 4 GB
v.memory = 1024

  end
end
