import subprocess

def vulnerable():
    subprocess.call("ls", shell=True)
