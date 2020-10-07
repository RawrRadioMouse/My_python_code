import win32api, win32con, win32gui, time, subprocess,sys
from pywinauto.application import Application



app = string.lower(sys.argv[1])
ServiceName = string.lower(sys.argv[2]) #Audiosrv
State = string.lower(sys.argv[3])

CareSYS  = Application(backend="uia").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=10.2.66.203  app=RPSManager")

CCIS = Application(backend="uia").start("E:\\nthDccisR1\\server\\c_bin\\jade.exe path=E:\\nthDccisR1\\Server\\c_system ini=E:\\nthDccisR1\\Server\\c_bin\\nthDccisR1.ini app=RPSManager schema=JadeMonitorSchema server=multiuser")

CCIS1 = Application(backend="uia").start("E:\\nthDccisR\\server\\c_bin\\jade.exe path=E:\\nthDccisR\\Server\\c_system ini=E:\\nthDccisR\\Server\\c_bin\\nthDccisR.ini app=RPSManager schema=JadeMonitorSchema server=mu")

PCIS  = Application(backend="uia").start("E:\\nthDpcisR\\server\\c_bin\\jade.exe path=E:\\nthDpcisR\\Server\\c_system ini=E:\\nthDpcisR\\Server\\c_bin\\nthDpcisR.ini app=RPSManager schema=JadeMonitorSchema server=multiuser appServer=10.2.66.203  app=RPSManager")

CareSYS  = Application(backend="uia").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=10.2.66.203  app=RPSManager")

CareSYS  = Application(backend="uia").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=10.2.66.203  app=RPSManager")

WindowName

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


CareSYS = win32gui.FindWindow (None, 'Jade RPS Manager [RPS Database : nthDcareR_AP01-DEV;RelationalMappingSchema::RelationalSchemaMappings]') #b

class BringDown:
    def SoftStop(hwnd, ServiceName)
        win32api.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_KEYMENU,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RIGHT,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RIGHT,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_DOWN,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_DOWN,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN,0)
        time.sleep(2)
    def HardStop(ServiceName)
        subprocess.run('sc config '+ ServiceName +' start=demand')
        time.sleep(1)
        subprocess.run('sc stop '+ ServiceName)

class BringUp:
    def SoftStart(hwnd, ServiceName)
        win32api.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_KEYMENU,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RIGHT,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RIGHT,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_DOWN,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_DOWN,0)
        time.sleep(0.5)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN,0)

    def HardStart(ServiceName)
        subprocess.run('sc start '+ ServiceName)

if state="down"
    BringDown(hwnd, ServiceName)
if state="up"
    BringUp(hwnd, ServiceName)
