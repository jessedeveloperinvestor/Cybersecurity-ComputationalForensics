from ftplib import *
url='ibiblio.org'
ftp=FTP('ftp.'+url)
print(ftp.getwelcome())
user=input('Insert the username: ')
password=input('Insert the password: ')
ftp.login(user,password)
print('Current using directory: ', ftp.pwd())
ftp.cwd('pub')
print('Current directory: ', ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()