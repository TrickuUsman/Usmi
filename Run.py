import os, platform
os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    print("NOT UPLOADED YET BE PATIENT.... ")

elif bit == '32bit':

    from USMI import fia

    fia()
