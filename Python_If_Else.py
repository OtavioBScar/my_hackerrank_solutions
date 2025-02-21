import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n >= 1 and n <= 100):     
        if (n % 2 == 0):
            if(n >= 6 and n <= 20):
                print("Weird")
            else:
                print("Not Weird")
        else:
            print("Weird")
    else:
        print("n deve estar entre 1 e 100") 