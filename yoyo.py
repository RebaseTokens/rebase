import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)
def apollo(sc):
    with open('/root/Desktop/rebase/apollo.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/apollo.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, axie, (s,))

def axie(sc):
    with open('/root/Desktop/rebase/axie.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/axie.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, bitup, (s,))

def bitup(sc):
    with open('/root/Desktop/rebase/bitup.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/bitup.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, blowup, (s,))

def blowup(sc):
    with open('/root/Desktop/rebase/blowup.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/blowup.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, fbnb, (s,))

def fbnb(sc):
    with open('/root/Desktop/rebase/fbnb.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/fbnb.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, flokg, (s,))

def flokg(sc):
    with open('/root/Desktop/rebase/flokg.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/flokg.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, floki, (s,))

def floki(sc):
    with open('/root/Desktop/rebase/floki.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/floki.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, fomobaby, (s,))

def fomobaby(sc):
    with open('/root/Desktop/rebase/fomobaby.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/fomobaby.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, greenm, (s,))

def greenm(sc):
    with open('/root/Desktop/rebase/greenm.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/greenm.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, grv, (s,))

def grv(sc):
    with open('/root/Desktop/rebase/grv.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/grv.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, infx, (s,))

def infx(sc):
    with open('/root/Desktop/rebase/infx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/infx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, lond, (s,))

def lond(sc):
    with open('/root/Desktop/rebase/lond.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/lond.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, pulsar, (s,))

def pulsar(sc):
    with open('/root/Desktop/rebase/pulsar.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/pulsar.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, shibn, (s,))

def shibn(sc):
    with open('/root/Desktop/rebase/shibn.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/shibn.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, shibx, (s,))

def shibx(sc):
    with open('/root/Desktop/rebase/shibx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/shibx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, squid, (s,))

def squid(sc):
    with open('/root/Desktop/rebase/squid.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/squid.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, upcake, (s,))

def upcake(sc):
    with open('/root/Desktop/rebase/upcake.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/upcake.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, wei, (s,))

def wei(sc):
    with open('/root/Desktop/rebase/wei.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/wei.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, commit, (s,))

def commit(sc):
    subprocess.call(['/root/Desktop/rebase/autocommit.sh'])
  
    s.enter(1800, 1, apollo, (s,))
    
s.enter(1, 1, apollo, (s,))
s.run()

