import sys
import shutil
import time

path = sys.argv[1]

# Write your code here...
# Modify the source file or the file in the results directory

# If you modified the CSV file in uploads uncomment this line
shutil.copy(path, 'results/')
time.sleep(10)