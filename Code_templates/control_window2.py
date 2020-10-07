import win32api, win32con, win32gui
from pywinauto.application import Application
from subprocess import Popen
from sys import argv
from time import sleep
from win32gui import FindWindow
from win32api import PostMessage


app = string.lower(sys.argv[1])
ServiceName = string.lower(sys.argv[2]) #Audiosrv
State = string.lower(sys.argv[3])


if app == caresys
    open = Application(backend="uia").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=10.2.66.203  app=RPSManager")

    window = ('Jade RPS Manager [RPS Database : nthDcareR_AP01-DEV;RelationalMappingSchema::RelationalSchemaMappings]')

if app == cws
    open = Application(backend="uia").start("E:\\nthDccisR1\\server\\c_bin\\jade.exe path=E:\\nthDccisR1\\Server\\c_system ini=E:\\nthDccisR1\\Server\\c_bin\\nthDccisR1.ini app=RPSManager schema=JadeMonitorSchema server=multiuser")

    window = <WINDOW_NAME>

if app == ccis
    open   = Application(backend="uia").start("E:\\nthDpcisR\\server\\c_bin\\jade.exe path=E:\\nthDpcisR\\Server\\c_system ini=E:\\nthDpcisR\\Server\\c_bin\\nthDpcisR.ini app=RPSManager schema=JadeMonitorSchema server=multiuser appServer=10.2.66.203  app=RPSManager")

    window = <WINDOW_NAME>

if app == ccis1
    open   = Application(backend="uia").start("E:\\nthDpcisR\\server\\c_bin\\jade.exe path=E:\\nthDpcisR\\Server\\c_system ini=E:\\nthDpcisR\\Server\\c_bin\\nthDpcisR.ini app=RPSManager schema=JadeMonitorSchema server=multiuser appServer=10.2.66.203  app=RPSManager")

    window = <WINDOW_NAME>

if app == pcis
    open   = Application(backend="uia").start("E:\\nthDpcisR\\server\\c_bin\\jade.exe path=E:\\nthDpcisR\\Server\\c_system ini=E:\\nthDpcisR\\Server\\c_bin\\nthDpcisR.ini app=RPSManager schema=JadeMonitorSchema server=multiuser appServer=10.2.66.203  app=RPSManager")

    window = <WINDOW_NAME>

if app == pcis1
    open   = Application(backend="uia").start("E:\\nthDpcisR\\server\\c_bin\\jade.exe path=E:\\nthDpcisR\\Server\\c_system ini=E:\\nthDpcisR\\Server\\c_bin\\nthDpcisR.ini app=RPSManager schema=JadeMonitorSchema server=multiuser appServer=10.2.66.203  app=RPSManager")

    window = <WINDOW_NAME>

######################################################
#***Use this code to eumerate strict window name for to use for declaring hwnd -
#***the code will work to declare hwnd ONLY when ran from desktop, not as scheduled task
#
#def FindWindowTitle():
#    a = app.windows()
#    return (list(a))
#b = (str(L337()[0]))
#b = b.replace('hwndwrapper.DialogWrapper - ', '')
#b = b.replace("uiawrapper.UIAWrapper - '", '')
#b = b.replace("', Dialog", '')
#b = b.replace(', Jade:form', '')
#print(b)
#
#***Use below line to adjust what is replaced
#app.window(title=b).print_control_identifiers()
######################################################

time.sleep(3)


hwnd = win32gui.FindWindow (None, window) #b

class BringDown:
    def __init__(self)
        self.SoftStop
            win32api.PostMessage(self, win32con.WM_SYSCOMMAND, win32con.SC_KEYMENU,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_RIGHT,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_RIGHT,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_DOWN,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_DOWN,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_RETURN,0)
            time.sleep(2)
        self.HardStop
            subprocess.run('sc config '+ ServiceName +' start=demand')
            time.sleep(1)
            subprocess.run('sc stop '+ ServiceName)


class BringUp:
    def __init__(self)
        self.SoftStart
            win32api.PostMessage(self, win32con.WM_SYSCOMMAND, win32con.SC_KEYMENU,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_RIGHT,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_RIGHT,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_DOWN,0)
            time.sleep(0.5)
            win32api.PostMessage(self, win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
            win32api.PostMessage(self, win32con.WM_KEYUP, win32con.VK_RETURN,0)

        self.HardStart
            subprocess.run('sc start '+ ServiceName)

if state="down"
    hwnd.SoftStop()
    time.sleep(1)
    hwnd.HardStop()

if state="up"
    hwnd.SoftStart
    time.sleep(1)
    hwnd.HardStart()
