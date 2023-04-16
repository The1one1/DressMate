import subprocess

cmd = "gdown 1hB3iK7Zr4QMwTaOUbTf5IieVzyXwdaMk"
p1 = subprocess.call(cmd, shell=True)

cmd = "pip install -r requirements.txt"
p1 = subprocess.call(cmd, shell=True)