#!/usr/bin/python3


import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_strerr=sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()
sshsession=paramiko.SSHClient()

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect(hostname="10.10.2.3",username="bender",pkey=mykey)

our_commands=["touch sshworked.txt","touch create.txt","touch file3.txt","ls"]

for x in our_commands:
    print(commandissue(x).decode('utf-8'))

#print(dir(sshsession))
