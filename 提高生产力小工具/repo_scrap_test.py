import sys
import re
import threading


class tryToScrap:
    def __init__(self,threadnum):
        self.threadlock = threading.Semaphore(threadnum)

    def cook_content(self, readfilename, writefilename):
        filecontrol = fileControl()
        content = filecontrol.get_file_content(readfilename)
        ip_html = []
        result = re.finditer(r"(host)(\/)((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])(\.)(html)",content)
        for i in result:
            ip_html.append(i.group())
        for i in range(len(ip_html)):
            threading.Thread(target=self.cook_content_and_save,args=(ip_html[i],writefilename,i,str(len(ip_html)))).start()


    def cook_content_and_save(self,ip_html,writefilename,i,total_len):
        self.threadlock.acquire()
        filecontrol = fileControl()
        ip_html_content = filecontrol.get_file_content(ip_html)
        port_with_tag_result = re.finditer(r"(<)(tr)( )(class)(=)(\".*?\")(>)(\s+)(<)(td)(>)(\s+)(\d+)(\s+)(<\/td>)(\s+)(<)(td)(>)(\s+)(udp|tcp)",ip_html_content)
        port_with_tag = []
        ports = []
        ip = re.finditer(
            r"(<)(td)(>)((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])(<\/td>)",
            ip_html_content)
        ip_cooked = ''
        for l in ip:
            ip_cooked = l.group()
        ip = re.finditer(r"((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])",ip_cooked)
        for l in ip:
            ip_cooked = l.group()
        for k in port_with_tag_result:
            port_with_tag.append(k.group())
        for k in range(len(port_with_tag)):
            port_with_tag_location = re.finditer(r"(\d+)", port_with_tag[k])
            for l in port_with_tag_location:
                ports.append(l.group())
        for j in range(len(ports)):
            self.save_url_to_file(writefilename,ip_cooked+':'+ports[j]+'\n')
        print('completed: ' + str(i+1) + ' ip total: ' + total_len)
        self.threadlock.release()


    def save_url_to_file(self,writefilename,content):
        filecontrol = fileControl()
        content = 'http://' + content
        filecontrol.write_file(writefilename,content)

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

    def get_file_content(self,filename):
        fo = open(filename, "r", encoding='utf-8')
        content = str(fo.read())
        fo.close()
        return  content

if __name__ == "__main__":
#
#     if len(sys.argv) < 4 :
#         print(
#             '''put me in to repo_dir and command me, then give me thread number:
# \trepo_scrap.py readfilename writefilename num
# for example:
# \trepo_scrap.py index.html result.txt 20''')
#     else:
#         threadnum = int(sys.argv[3])
#         readfilename = sys.argv[1]
#         writefilename = sys.argv[2]
#         trytoScrap = tryToScrap(threadnum)
#         trytoScrap.cook_content(readfilename, writefilename)

    try:
        threadnum = int(sys.argv[3])
        readfilename = sys.argv[1]
        writefilename = sys.argv[2]
        trytoScrap = tryToScrap(threadnum)
        trytoScrap.cook_content(readfilename, writefilename)
    except:
        print(
'''put me in to repo_dir and command me, then give me thread number:
\trepo_scrap.py readfilename writefilename num
for example:
\trepo_scrap.py index.html result.txt 20''')