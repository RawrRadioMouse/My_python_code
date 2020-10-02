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
