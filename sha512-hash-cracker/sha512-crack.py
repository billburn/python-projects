#!/usr/bin/env python3
#Author: Bill Burn

import click
from pwn import *
import sys

click.clear()

if len(sys.argv) !=2:
    print("Invalid number of arguments")
    print(">> {} <sha512hash>".format(sys.argv[0]))

wanted_hash = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with log.progress("Attempting to crack: {}".format(wanted_hash)) as p:
    with open(password_file, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha512sumhex(password)
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            if password_hash == wanted_hash:
                p.success("\nPassword found after {} attempts! \nThe password is: '{}' \nThe password hash is: '{}'".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1
        p.failure("Password was not found")