class fileControl:
    
    def __init__(self):
        import platform
        import os
        self.os = os
        self.sysstr = platform.system()

    def mk_file(self, filename):
        os = self.os
        sysstr = self.sysstr
        if(sysstr =="Windows"):
            os.system(r"type nul>{}".format(filename))
        elif(sysstr == "Linux"):
            os.system(r"touch {}".format(filename))

    def if_file(self, filename):
        os = self.os
        if not os.path.exists(filename):
            self.mk_file(filename)
        else:
            pass

    def write_file(self, filename,content):
        self.if_file(filename)
        fo = open(filename,'a+')
        fo.write(content)
        fo.close()
        
    def read_file(self,filename):
        fo = open(filename,'r')
        content = fo.read()
        fo.close()
        return content

if __name__ == "__main__":

    fileControl().write_file('1.txt','222222')

