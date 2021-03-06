# __XFTPD__
## _As a network automation engineer, do you get frustrated at not having instant access to an SFTP/FTP server when you need it most?!_
# Well look no further!
## _Simple, Secure, and Randomized..._
## Right at your fingertips, and ready for API integrations, you have come to the right Python Module!
# XFTPD Server
## SFTP and FTP server Class that can be started and stopped programmatically
## With randomized username, password, RSA keys
## Ideal for on-demand SFTP and FTP and file transfers

## SFTP Example
```python
>>> from xftpd import sftp_server
>>> SFTP = sftp_server('/tmp',2222)
>>> SFTP.level = 'DEBUG'
>>> SFTP.start()
>>> print(SFTP.Addr)
10.8.2.5
>>> print(SFTP.User)
w7Kg0Fo4Xp6Xo9C
>>> print(SFTP.Pass)
k2Ea0Ko4Rz6Gz3Z
>>>
>>> SFTP.stop()
>>>
```

## Example connecting to SFTP server
```bash
[root@CentOS]# sftp -P 2222 w7Kg0Fo4Xp6Xo9C@10.8.2.5
The authenticity of host '[10.8.2.5]:2222 ([10.8.2.5]:2222)' can't be established.
RSA key fingerprint is SHA256:khgoV/GQIShUf4KWr2ZqvpI68KMUFRsedwx4E0hWgi0.
RSA key fingerprint is MD5:d2:45:1b:d8:44:66:5f:66:b9:5e:8d:33:fb:01:0b:b1.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[10.8.2.5]:2222' (RSA) to the list of known hosts.
w7Kg0Fo4Xp6Xo9C@10.8.2.5's password:
Connected to 10.8.2.5.
sftp> dir
new.py                       test.py
sftp> bye
[root@CentOS]#
```

## FTP Example
```python
Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from xftpd import ftp_server
>>> FTP = ftp_server('/tmp')
>>> FTP.start()
[I 2020-07-15 21:14:48] concurrency model: multi-thread
[I 2020-07-15 21:14:48] masquerade (NAT) address: None
[I 2020-07-15 21:14:48] passive ports: None
>>> print(SFTP.Addr)
10.8.2.5
>>> print(FTP.User)
h0Dy0Yq9Ks0Dm3T
>>> print(FTP.Pass)
m5Sg2Yk5Mk8Fa4K
>>>
>>> FTP.stop()
>>>
```

