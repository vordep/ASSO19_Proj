# -*- mode: ruby -*-
# vi: set ft=ruby :
BOX_BASE = "ubuntu/xenial64"
BOX_CPU_COUNT = "1" 
BOX_EXEC_CAP = "30"
BOX_RAM_MB = "1024"

SOAP_PORT = "5000"
REST_PORT = "5001"
MQTT_PORT = "1883"
#AMQP_PORT

Vagrant.configure("2") do |config|
  #Server
  config.vm.define :server do |server|

    #Base box for the VM
    server.vm.box = BOX_BASE

    #Virtual box configs
    server.vm.provider "virtualbox" do |vb|
      vb.memory = BOX_RAM_MB
      vb.cpus = BOX_CPU_COUNT
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", BOX_EXEC_CAP]
      vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
    end

    #Synced folder
    server.vm.synced_folder "./Server", "/vagrant"

    server.vm.provision "shell", path: "setup.sh"

    server.vm.network :private_network, ip: "192.168.56.105"

  end 
  
  #Client
  config.vm.define :client do |client|

    #Base box for the VM
    client.vm.box = BOX_BASE

    #Virtual box configs
    client.vm.provider "virtualbox" do |vb|
      vb.memory = BOX_RAM_MB
      vb.cpus = BOX_CPU_COUNT
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", BOX_EXEC_CAP]
      vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
    end

    client.vm.synced_folder "./Client", "/vagrant"
    client.vm.network :private_network, ip: "192.168.56.104"
    client.vm.provision "shell", path: "setup.sh"

  end 
end
