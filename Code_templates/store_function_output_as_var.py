  
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import string
#here we start the target with command args
app = Application(backend="win32").start("E:\\nthDcareR\\server\\c_bin\\jade.exe path=E:\\nthDcareR\\Server\\c_system ini=E:\\nthDcareR\\Server\\c_bin\\nthDcareR.ini server=multiuser schema=JadeMonitorSchema  appServer=XXXX  app=RPSManager")
#give enough time for startup before selecting from menu
time.sleep(5)
def L337():
    a = app.windows()
    return (list(a))
b = (str(L337()[0]))
b = b.replace('hwndwrapper.DialogWrapper - ', '')
b = b.replace(', Jade:form', '')
print(b)
