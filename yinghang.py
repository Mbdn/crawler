#!/usr/bin/env python
# coding=utf-8
import urllib,re
import xlwt #写入excl库，xlrd读

def getdata():
    url_list = []
    for i in range(1,500):    
        url = 'http://furhr.com/?page='+str(i)
        try:
            html = urllib.urlopen(url).read()
        except Exception as e:
            print e
            continue

        ze = re.compile(r'<tr><td>\d+</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>')
        page_list = re.findall(ze,html)
        url_list.append(page_list)
    return url_list

#创建表格
def excel_write(items):
    newTable = 'text123.xls'  #表格名称
    wb = xlwt.Workbook(encoding='utf-8') #创建文件，设置编码格式
    ws = wb.add_sheet('test1')#创建表格
    headData = ['公司名称','电话','地址']#表头
    for colnum in range(0,3):
        ws.write(0,colnum,headData[colnum],xlwt.easyxf('font:bold on'))#0行colnum列内容
    wb.save(newTable)

    #写入数据
    index = 1
    for item in items:    #银行信息
        for j in range(0,len(item)):
            for i in range(0,3):
                ws.write(index,i,item[j][i])
            index += 1
        wb.save(newTable)#保存

if __name__ == "__main__":
    items = getdata()
    excel_write(items)
