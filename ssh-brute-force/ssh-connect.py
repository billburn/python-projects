#!/usr/bin/env python3
#Author: Bill Burn

import click
import paramiko

click.clear()

host = '192.168.10.13'
username = 'user1'
password = 'P@ssw0rd123'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
stdin, stdout, stderr = client.exec_command("df -h")
print(stdout.read().decode())
client.close()