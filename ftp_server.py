from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import threading,random




########################
# Random Password Generator
# Returns 14 character string
#
def Random_String(num=14):
    Random_Str = ''
    while len(Random_Str) < num:
        char = 'abcdefghijklmnopqrstuvwxyz'
        CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        NUM = '1234567890'

        Random_Str += random.choice(char)
        Random_Str += random.choice(NUM)
        Random_Str += random.choice(CHAR)

    return Random_Str

########################
# FTP Server Class
# Dir = str()
#   Ex: '/tmp'
# Port = int()
#   Ex: 2121
class FtpServer(object):
    # Create Random Username and Password
    def __init__(self,Dir='/tmp',Port=2121):
        self.Dir = Dir
        self.Port = Port
        self.user = Random_String()
        self.Pass = Random_String()
        self.authorizer = DummyAuthorizer()
        self.authorizer.add_user(self.user, self.Pass, self.Dir, perm='elradfmw')
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer

        self.SRV = ThreadedFTPServer(('0.0.0.0',self.Port), self.handler)

    def _run_server(self):
        self.SRV.serve_forever()

    def start(self):
        self.srv = threading.Thread(target=self._run_server)
        self.srv._stop = threading.Event()
        self.srv.deamon = True
        self.srv.start()

    def stop(self):
        self.SRV.close_all()














