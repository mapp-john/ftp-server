# ftp-server
FTP Server class, that can be started/stopped


##Example


```python
>>> from ftp_server import FtpServer
>>> FTP = FtpServer()
>>> FTP.start()
[I 2020-07-15 17:17:48] concurrency model: multi-thread
[I 2020-07-15 17:17:48] masquerade (NAT) address: None
[I 2020-07-15 17:17:48] passive ports: None
>>> FTP.stop()
```


### When the ```stop()``` function is called, the Thread will print an Exception to STDOUT, but this will not impact the code calling the function
```Python
>>> Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/threading.py", line 926, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/johnmapp/TEMP/ftp_server.py", line 17, in _run_server
    self.SRV.serve_forever()
  File "/usr/local/lib/python3.7/site-packages/pyftpdlib/servers.py", line 478, in serve_forever
    self.ioloop.loop(timeout, blocking)
  File "/usr/local/lib/python3.7/site-packages/pyftpdlib/ioloop.py", line 343, in loop
    poll(timeout)
  File "/usr/local/lib/python3.7/site-packages/pyftpdlib/ioloop.py", line 709, in poll
    timeout)
OSError: [Errno 9] Bad file descriptor


>>> 
>>> 
```
