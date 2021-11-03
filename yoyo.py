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
  
    s.enter(1, 1, upsh, (s,))

def upsh(sc):
    with open('/root/Desktop/rebase/upsh.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/upsh.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, card, (s,))

def card(sc):
    with open('/root/Desktop/rebase/card.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/card.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, fbnb, (s,))

def fbnb(sc):
    with open('/root/Desktop/rebase/fbnb.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/fbnb.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, elon, (s,))

def elon(sc):
    with open('/root/Desktop/rebase/elon.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/elon.json', 'w') as file:
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
  
    s.enter(1, 1, grezilla, (s,))

def grezilla(sc):
    with open('/root/Desktop/rebase/grezilla.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/grezilla.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, infx, (s,))


def infx(sc):
    with open('/root/Desktop/rebase/infx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/infx.json', 'w') as file:
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
  
    s.enter(1, 1, risen, (s,))


def risen(sc):
    with open('/root/Desktop/rebase/risen.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/risen.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, commit, (s,))
    

def commit(sc):
    subprocess.call(['/root/Desktop/rebase/autocommit.sh'])
  
    s.enter(1800, 1, apollo, (s,))
    
s.enter(1, 1, apollo, (s,))
s.run()

