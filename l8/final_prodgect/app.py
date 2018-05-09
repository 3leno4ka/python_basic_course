from utils import *
import random
import csv

def generate_dict():
    return {"Name": get_full_name(), "Phone": get_phone(), "Exp_date": get_exp_date(), "Card": get_cc()}

for i in range(0, 100):
    print(generate_dict())
