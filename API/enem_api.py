import servicemanager
import socket
import win32event
import win32service
import win32serviceutil
from flask import Flask, url_for, render_template, request
from multiprocessing import Process

#app.run(port='8292', host='0.0.0.0', debug=True)

class EnemAPI (win32serviceutil.ServiceFramework) :
    _svc_name_ = "Enem"
    _svc_display_name_ = "Enem"
    app = Flask(__name__)
    #process = None

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
    
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        #self.process.terminate()
        #self.app = None
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        #sys.exit()

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
    
    def main(self):
        self.ReportServiceStatus(win32service.SERVICE_START)
        self.app.run(port='8292', host='0.0.0.0', debug=True)
        #self.process = Process(target=self.app)
        #self.process.start()
        #self.process.run()
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!<br/><br/>'

    @app.route('/test')
    def test():
        return '<h1>O test foi:</h1><br/><br/><h2>'

    @app.route('/funcionario')
    @app.route('/funcionario/<name>')
    def funcionario(name=None):
        return render_template('funcionario.html', name=name)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(EnemAPI)