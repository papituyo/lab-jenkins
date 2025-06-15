import subprocess

def listar_directorio():
    subprocess.run(["cmd", "/c", "dir"], shell=False)
