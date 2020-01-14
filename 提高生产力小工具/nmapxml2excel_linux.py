#coding:utf-8

import xml.etree.ElementTree as ET   #解析xml，python3已经默认使用cElementTree
import xlwt     #写excel
import argparse    #运行前参数
import sys

#判断运行时python版本是否小于3.x
if sys.version_info.major < 3:
    print("I need python3.x")

def parsexml(xml,sheet):
    tree = ET.parse(xml)
    root = tree.getroot()     #获取根节点
    hosts = root.findall("host")
    i = 0   #写入excel的计数器
    for host in hosts:
        i += 1
        portTcpRes = ""
        portOtherRes = ""
        ip = host.find("address")
        ipaddress = ip.attrib.get('addr')
        # print("ip地址:"+ ipaddress)
        ports = host.find("ports").findall("port")
        #获取系统版本的扫描结果
        os = host.find("os")
        try:
            osmatch = os.find("osmatch")
            osname = osmatch.attrib.get("name")
            accuracy = osmatch.attrib.get("accuracy")
        except Exception as e:
            osname = ""
            accuracy = ""
        # print(ports)
        for portT in list(ports):
            service = portT.find("service")
            protocol = portT.attrib.get('protocol')
            #获取nmap结果中service信息
            #serviceName = service.attrib.get('name')
            try:
                print(service.attrib['name'])
                serviceName = service.attrib['name']
            except:
                a = 1
            #product = service.attrib['product']
            #if product:
            #    serviceName = serviceName + ':' + product   #将SERVICE和VERSION组合一起
            #获取端口号
            portNum = portT.attrib.get('portid')
            if protocol == 'tcp':
                portTcpRes += portNum + '(' + serviceName + '),'
            else:           #其他协议
                portOtherRes += portNum + '(' + serviceName + '),'
        output(sheet,ipaddress,portTcpRes.strip(','),portOtherRes.strip(','),i,osname,accuracy+"%")    #写入excel
        # print(portTcpRes.strip(','))
        # print('------------------------')
#初始化excel
def excelcsh():
    ExcelFile = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet1 = ExcelFile.add_sheet('nmap结果')
    #表格第一行
    sheet1.write(0,0,'ip地址')
    sheet1.write(0,1,'TCP端口')
    sheet1.write(0,2,'其他协议端口')
    sheet1.write(0,3,'系统版本')
    sheet1.write(0,4,'系统扫描精准度')
    return ExcelFile,sheet1
def output(sheet,ip,tcpport,otherproto,num,osversion,accuracy):
    #写入数据
    sheet.write(num,0,ip)
    sheet.write(num,1,tcpport)
    sheet.write(num,2,otherproto)
    sheet.write(num,3,osversion)
    sheet.write(num,4,accuracy)
    #刷新缓存
    sheet.flush_row_data()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="xml解析")#.decode('utf-8').encode('gbk')
    parser.add_argument('-x',action="store",required=False,dest="xml",type=str,help='nmap result(xml file)')
    parser.add_argument('-o',action="store",required=False,dest="outfile",type=str,help='outputName',default="excel.xls")
    # parser.add_argument('--file',action="store",required=False,dest="file",type=str,help='Input filename eg:a.txt')
    args = parser.parse_args()
    xml = args.xml
    outpath = args.outfile
    if xml:
        excelfile,sheet = excelcsh()
        try:
            parsexml(xml,sheet)
        except FileExistsError as e:
            print("xml文件不存在")
            print(e)
        excelfile.save(outpath)
        print("文件保存至 %s" % outpath)
    else:
        print('Error args')
        print('eg: python3 pythonXml.py -x nmap.xml -o nmap.xls')
