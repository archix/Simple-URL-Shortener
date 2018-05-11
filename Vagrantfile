# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

ENV["LC_ALL"] = "en_US.UTF-8"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--memory", "512"]
  end

  config.vm.box = "ubuntu/xenial64"


  # Sharing this folder to /home/vagrant/app
  config.vm.synced_folder ".", "/home/vagrant/app", create:true
  config.vm.provision :shell, :path => "setup_vagrant.sh"
  config.vm.network :private_network, ip: "192.168.55.56"
  config.vm.network :forwarded_port, guest: 5000, host: 5000

end