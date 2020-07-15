from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import threading

class FtpServer:

    authorizer = DummyAuthorizer()
    authorizer.add_user('dummyuser', 'dummypass', '/tmp', perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    SRV = ThreadedFTPServer(('0.0.0.0',2121), handler)

    def _run_server(self):
        self.SRV.serve_forever()

    def start(self):
        self.srv = threading.Thread(target=self._run_server)
        self.srv._stop = threading.Event()
        self.srv.deamon = True
        self.srv.start()

    def stop(self):
        self.SRV.close_all()

