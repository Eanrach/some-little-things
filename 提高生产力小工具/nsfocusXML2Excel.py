#coding:utf-8

import xml.etree.ElementTree as ET   #解析xml，python3已经默认使用cElementTree
import xlwt     #写excel
import argparse    #运行前参数
import sys
import re

#判断运行时python版本是否小于3.x
if sys.version_info.major < 3:
    print("I need python3.x")

def parsexml(xml,sheet):
    rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
    filecontrol = fileControl()
    content = filecontrol.read_file(xml)
    name = rgx.search(content).group(1)
    tree = ET.parse(xml)
    root = tree.getroot()     #获取根节点
    data = root.find("data")
    report = data.find("report")
    targets = report.find("targets")
    target = targets.findall("target")
    i = 0
    for tar in target:
        i += 1
        ipaddress = tar.find("ip").text
        portTcpRes = ""
        appendix_info = tar.find("appendix_info")
        info = appendix_info.find("info")
        try:
            record_results = info.findall("record_results")
        except:
            pass
        for reco in record_results:
            result = reco.find("result")
            #print(result)
            if not result is None:
                value = result.findall("value")
                if len(value)>2:
                    portNum = value[0].text
                    #print(portNum)
                    serviceName = value[2].text
                    #print(1)
                else:
                    portNum = value[0].text
                    serviceName = value[1].text
                    #print(2)
                if serviceName == 'unknown':
                    serviceName = '未知服务'
                #print(portNum+' portNum')
                #print(serviceName+' serviceName')
                if not serviceName:
                    serviceName = '未知服务'
                if (portNum == 'Windows') or (portNum == 'Linux'):
                    pass
                if int(portNum) > 65535:
                    pass
                else:
                    portTcpRes += portNum + '(' + serviceName + '),'
            #print(ipaddress)
        output(sheet,ipaddress,portTcpRes.strip(','),i)    #写入excel
    return name

#初始化excel
def excelcsh():
    ExcelFile = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet1 = ExcelFile.add_sheet('result')
    #表格第一行
    sheet1.write(0,0,'ip地址')
    sheet1.write(0,1,'开放端口')
    #sheet1.write(0,2,'其他协议端口')
    return ExcelFile,sheet1
def output(sheet,ip,tcpport,num):
    #写入数据
    sheet.write(num,0,ip)
    sheet.write(num,1,tcpport)
    #sheet.write(num,2,otherproto)
    #刷新缓存
    sheet.flush_row_data()


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
        fo = open(filename,'r',encoding='utf-8')
        content = fo.read()
        fo.close()
        return content


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="xml解析")#.decode('utf-8').encode('gbk')
    parser.add_argument('-x',action="store",required=False,dest="xml",type=str,help='nmap result(xml file)')
    #parser.add_argument('-o',action="store",required=False,dest="outfile",type=str,help='outputName',default="excel.xls")
    # parser.add_argument('--file',action="store",required=False,dest="file",type=str,help='Input filename eg:a.txt')
    args = parser.parse_args()
    xml = args.xml
    outpath = xml[0:xml.rfind('\\')+1]
    #outpath = args.outfile
    if xml:
        excelfile,sheet = excelcsh()
        try:
            outpath = outpath + parsexml(xml,sheet) + '.xls'
        except FileExistsError as e:
            print("xml文件不存在")
            print(e)
        excelfile.save(outpath)
        print("文件保存至 %s" % outpath)
    else:
        print('Error args')
        print('eg: python3 pythonXml.py -x nmap.xml')
