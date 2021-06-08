# -*- coding: utf-8 -*-

# Do simple calculation

---
This script perform simple calculations.
---

import argparse

parser =  argparse.ArgumentParser()
parser.parse_args()
x = 10
y = 5
z = x + y 

print(z)