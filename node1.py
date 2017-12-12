import threading
import socket
#Node 1

class chatroom(threading.Thread):
	def __init__(self,hostip,sendport):
		#threading.Thread.__init__(self)
		self.hostip=hostip
		self.sendport=sendport
		self.listenport=12346

	def sendmessage(self):
		while True:
			
			text=input()
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect(('127.0.0.1',self.sendport))
			s.send(bytes(text,'utf-8'))
			s.close()


	def receivemessage(self):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(('',self.listenport))
		s.listen(4)
		while True:

			c,addr=s.accept()
			msg=c.recv(1024)
			print('Friend says : {}'.format(msg.decode('utf-8')))
			c.close()


	def run(self):
			threading.Thread( target= self.receivemessage,args=()).start()
			self.sendmessage()


if __name__ == '__main__':
	chat=chatroom('127.0.0.1',12345)
	chat.run()



