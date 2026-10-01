import subprocess
import time

# Sleep for 60 seconds
print("Starting sleep for 60 seconds...")
time.sleep(60)
print("Sleep completed!")

# List current folder items with the Windows dir command
print("Listing current folder items...")
subprocess.run(["cmd", "/c", "dir"], check=False)
