import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)

def axie(sc):
    with open('/root/Desktop/rebase/axie.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')
    

    with open('/root/Desktop/rebase/axie.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, mars, (s,))

def mars(sc):
    with open('/root/Desktop/rebase/mars.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/mars.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, chfx, (s,))

def chfx(sc):
    with open('/root/Desktop/rebase/chfx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/chfx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, flokx, (s,))

def flokx(sc):
    with open('/root/Desktop/rebase/flokx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/flokx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, elon, (s,))

def elon(sc):
    with open('/root/Desktop/rebase/elon.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/elon.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, huskyx, (s,))

def huskyx(sc):
    print('Half')
    with open('/root/Desktop/rebase/huskyx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/huskyx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, fomobaby, (s,))

def fomobaby(sc):
    with open('/root/Desktop/rebase/fomobaby.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/fomobaby.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, prince, (s,))

def prince(sc):
    with open('/root/Desktop/rebase/prince.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/prince.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, infx, (s,))


def infx(sc):
    with open('/root/Desktop/rebase/infx.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/infx.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, pulsar, (s,))


def pulsar(sc):
    with open('/root/Desktop/rebase/pulsar.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/pulsar.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, squid, (s,))



def squid(sc):
    with open('/root/Desktop/rebase/squid.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/squid.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, zillam, (s,))

def zillam(sc):
    with open('/root/Desktop/rebase/zillam.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/zillam.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, avaxup, (s,))


def avaxup(sc):
    with open('/root/Desktop/rebase/avaxup.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/avaxup.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, uplink, (s,))
    

def uplink(sc):
    with open('/root/Desktop/rebase/uplink.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/uplink.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, gfloki, (s,))


def gfloki(sc):
    with open('/root/Desktop/rebase/gfloki.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/gfloki.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, efinu, (s,))


def efinu(sc):
    with open('/root/Desktop/rebase/efinu.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/rebase/efinu.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, commit, (s,))
    

def commit(sc):
    print('Commit')
    subprocess.call(['/root/Desktop/rebase/autocommit.sh'])
  
    s.enter(30, 1, axie, (s,))
    
s.enter(1, 1, axie, (s,))
s.run()
