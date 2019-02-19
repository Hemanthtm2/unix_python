#!/usr/bin/python

class Server(object):
      def __init__(self,ip,hostname):
          self.ip=ip
          self.hostname=hostname
      def set_ip(self,ip):
          self.ip=ip
      def set_hostname(self,hostname):
          sel.hostname=hostname 

      def ping(self,ipaddr):
          print("Pinging %s from %s (%s)" %(ipaddr,self.ip,self.hostname))

if __name__=='__main__':
   server=Server('192.168.56.102','server1')
   server.ping('192.168.31.14')
          
