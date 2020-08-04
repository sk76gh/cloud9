#logger class
from config import Config


class Logger:
    
    PRINTERRORS='ERROR'
    PRINTWARNS='WARN'
    PRINTINFO='INFO'
    PRINTDEBUG='DEBUG'
    loggerlist=dict()
    
    def __init__(self,loggerlist=Config.loggerlist):
        self.loggerlist=loggerlist
    
    def error(self, errormessage):
        if self.PRINTERRORS in self.loggerlist.keys():
            print 'error : ',errormessage
        
    def warn(self,warnmessage):
        if self.PRINTWARNS in self.loggerlist.keys():
            print 'warn : ',warnmessage
        
    def info(self,infomessage):
        if self.PRINTINFO in self.loggerlist.keys():
            print 'info : ',infomessage
        
    def debug(self,infomessage):
        if self.PRINTDEBUG in self.loggerlist.keys():
            print 'debug : ',infomessage