'''
Created on 

@author: le
'''

# -*- coding: utf-8 -*- 
#coding=utf-8
import  xdrlib ,sys
import xlrd
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)
#注释
def excel_table_byindex(file= '1.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows 
    ncols = table.ncols 
    colnames =  table.row_values(colnameindex) 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list


def excel_table_byname(file= '1.xls',colnameindex=0,by_name=u'1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows 
    colnames =  table.row_values(colnameindex) 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                print row[i]
             list.append(app)
    return list

def main():
   tables = excel_table_byindex()
   for row in tables:
       print row

   tables = excel_table_byname()
   for row in tables:
       
       #print row
       str_symptom = str(row).replace('u\'','\'')  
       str_symptom.decode("unicode-escape") 
       print str_symptom
       #print str(row).decode('string_escape')
       #print unicode(, "gbk")
       #continue
       
if __name__=="__main__":
    main()