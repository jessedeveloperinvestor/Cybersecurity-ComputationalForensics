import ctypes
file_oculter=0x02
returnfile=ctypes.windll.kernel32.SetFileAttributesW('ocult.txt', file_oculter)
if returnfile:
	print('File was oculted')
else:
	print('File was not oculted')