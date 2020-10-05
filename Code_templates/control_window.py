import win32api, win32con, win32gui, win32ui, win32service, os, time, subprocess
#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
#https://stackoverflow.com/questions/12996985/send-some-keys-to-inactive-window-with-python
#https://stackoverflow.com/questions/21917965/send-keys-to-a-inactive-window-in-python
#http://timgolden.me.uk/pywin32-docs/win32api.html
def f_click(pycwnd):
    x=300
    y=300
    lParam = y <<15 | x
    pycwnd.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam);
    pycwnd.SendMessage(win32con.WM_LBUTTONUP, 0, lParam);

def get_whndl():
    subprocess.Popen("notepad.exe")
    time.sleep(3)
    whndl = win32gui.FindWindowEx(0, 0, None, 'Untitled - Notepad')
    return whndl

def make_pycwnd(hwnd):       
    PyCWnd = win32ui.CreateWindowFromHandle(hwnd)
    return PyCWnd

def send_input_hax(pycwnd, msg):
    f_click(pycwnd)
    for c in msg:
        if c == "\n":
            pycwnd.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            pycwnd.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            #pycwnd.SendMessage(win32con.VK_MENU, 0)
            time.sleep(2)
            pycwnd.PostMessage(win32con.WM_CHAR, 0x12, 0)
    pycwnd.UpdateWindow()

whndl = get_whndl()

def callback(hwnd, hwnds):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        hwnds[win32gui.GetClassName(hwnd)] = hwnd
    return True
hwnds = {}
win32gui.EnumChildWindows(whndl, callback, hwnds)
whndl = hwnds['Edit']

pycwnd = make_pycwnd(whndl)
msg = "r"
send_input_hax(pycwnd,msg)



from pywinauto.application import Application
from pywinauto import keyboard
from pywinauto.keyboard import SendKeys 
import pywinauto
import win32api, win32con, win32gui, win32ui, win32service, os, time
from pywinauto import win32defines
import win32gui
import time
import string

app = Application(backend="uia").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=10.2.66.203  app=RPSManager")


while not app.windows():
    time.sleep(1)
time.sleep(5)
def L337():
    a = app.windows()
    return (list(a))
b = (str(L337()[0]))
b = b.replace('hwndwrapper.DialogWrapper - ', '')
b = b.replace("uiawrapper.UIAWrapper - '", '')
b = b.replace("', Dialog", '')
b = b.replace(', Jade:form', '')
print(b)

if app.window(title=b).exists():
    dlg_spec = app.window(title=b)
    dlg_spec.send_chars()
    #print(app.dlg.Edit.menu())
    #app.dlg.Edit.send_chars()
    print(app.System)
    #app.dlg.sendchars()
    #send_chars()
    #app.dlg.wrapper_object().menu_select('Menu')
    #app.dlg.edit.send_message()
    print (app.windows())
    print(dlg_spec)
    print("*"*10)
    #dlg_spec.maximize()
    print("*"*10)
    print(dlg_spec.is_active())
    print("*"*10)
    print(dlg_spec.titlebar.friendly_class_name())
    #print(app.window(title=b).Menu.get_properties())
    #print(app.window(title=b).System.items())
    #print(dlg_spec.edit.get_properties())
    #dlg_spec.send_keystrokes('{VK_MENU}rp')

    time.sleep(1)
    #app.window(title=b).print_control_identifiers()
    app.window(title=b).draw_outline()
    #app.window(title=b).TitleBar.select()
    #app.window(title="Edit").draw_outline()
    #app.window(title=b).edit.send_keys()
    #app.window(title=b).send_message()



dlg_spec=app.window(title=b)
dlg_spec
dlg_spec.wrapper_object()


#app.Dialog.child_window(title=b+tabName+"RPS",class_name='RibbonPageHeaderControl').select()
#app.window(title=b)

