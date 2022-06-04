import os
import glob

os.system('export GOOGLE_APPLICATION_CREDENTIALS=/home/tree4843/key.json')

file_list = glob.glob('*')
len(file_list)

for i in file_list:
    file_path= i
    os.system("gupload --to 1lehUa5ocP96RmZZALpH8kUqrHVq2Mc8v --file "+ file_path+ " " + file_path)