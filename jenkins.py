#!/usr/bin/python3
import os

# Author: Nadine
# Date: 10/26/2022

# Jenkins installtion script.

print("bigening jenkins installation")

os.system('sudo yum install java-11-openjdk-devel -y')

os.system('curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo')

os.system('sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key')

os.system('sudo yum install jenkins -y')

os.system('sudo systemctl start jenkins')

os.system('sudo systemctl status jenkins')
os.system('sudo systemctl enable jenkins')
os.system('sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp')
os.system('sudo firewall-cmd --reload')

print("end of jenkins installation")