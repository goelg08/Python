import subprocess
pl = subprocess.Popen(['ps', '-V', '0'], stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))