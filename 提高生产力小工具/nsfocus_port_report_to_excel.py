# _*_ coding: utf-8 _*_

import xlrd
import xlwt
import sys
import os
import re

path = "C:\\Users\\eanra\\Downloads\\多任务输出_2019_12_02_xls"


if sys.version_info.major < 3:
    print("I need python3.x")


def parseExcel(thePath, path):
    outpath = path + "\\" + thePath[thePath.rfind("\\"):] + ".xls"
    i = 0
    excelfile,sheet = excelcsh()
    #print(outpath)
    for name in os.listdir(thePath):
        portTcpRes = ""
        work = thePath + '\\' + name
        string = ''
        if re.match(r"((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])(\.)(xls)",
                    name):
            
            ip = re.match(r"((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])",
                          name).group()
            workbook = xlrd.open_workbook(work)
            # 获取全部工作表（sheet）以及选取对应的工作表
            sheet_name = workbook.sheet_names()[2]
            host_sheet = workbook.sheet_by_name(sheet_name)
            rows = host_sheet.nrows
            host_datas = read_data(host_sheet,rows)
            for j in range(len(host_datas)):
                a = host_datas[j]
                if (a[0] == "" and a[2]!="" and a[3]!="" and a[4]!="") and re.match(r"(\d+)",a[1]):
                    a[0] = ip
                    string = string + a[1] + '('+a[3]+'),'
                    #print(a)
                    portTcpRes += a[1]+'('+a[3]+'),'
                    
            try:
                if string[-1] == ",":
                    string = string[0:-1]
            except:
                c = None
        else:
            pass
        i += 1
        #print(str(i)+'\t'+ip+'\t'+string)
        output(sheet,ip,portTcpRes.strip(','),i)
    print(outpath)
    excelfile.save(outpath)


def read_data(host_sheet, rows):
    host_data = []
    for row in range(rows):
        host_data += [host_sheet.row_values(row)]
    return host_data[1:]
        #return a

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

if __name__ == '__main__':
    for name in os.listdir(path):
        parseExcel(path + '\\' + name, path)
    
##    outpath = sys.argv[1]
##    i = 0
##    excelfile,sheet = excelcsh()
##    for name in os.listdir(path):
##        portTcpRes = ""
##        work = path + '\\' + name
##        string = ''
##        if re.match(r"((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])(\.)(xls)",
##                    name):
##            
##            ip = re.match(r"((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\d])",
##                          name).group()
##            workbook = xlrd.open_workbook(work)
##            # 获取全部工作表（sheet）以及选取对应的工作表
##            sheet_name = workbook.sheet_names()[2]
##            host_sheet = workbook.sheet_by_name(sheet_name)
##            rows = host_sheet.nrows
##            host_datas = read_data(host_sheet,rows)
##            for j in range(len(host_datas)):
##                a = host_datas[j]
##                if (a[0] == "" and a[2]!="" and a[3]!="" and a[4]!="") and re.match(r"(\d+)",a[1]):
##                    a[0] = ip
##                    string = string + a[1] + '('+a[3]+'),'
##                    #print(a)
##                    portTcpRes += a[1]+'('+a[3]+'),'
##                    
##            try:
##                if string[-1] == ",":
##                    string = string[0:-1]
##            except:
##                c = None
##        else:
##            pass
##        i += 1
##        print(str(i)+'\t'+ip+'\t'+string)
##        output(sheet,ip,portTcpRes.strip(','),i)
##        
##    excelfile.save(outpath)




