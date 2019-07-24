#this was me trying xlrd out for the first time 
import xlrd
#now we write the path of the file we gonna use
path='D:\Downloads\TT SEM I 19-20 (DRAFT110719).xlsx'
#now we try to make the workbook object
workbook= xlrd.open_workbook(path)
#now we try to make 1st sheet object?
sheet = workbook.sheet_by_index(0)
''' this was me just trying stuff out
    #let us check by asking for C1 
    print(sheet.cell_value(0,2))
    #it worked!!!!!
'''
#now i will try to search for a string
#ask the user for a string like BITS F110 or something
course_code=input('Input the course code in  proper format please like BITS F110:')
flag=0
for row in range(sheet.nrows):
    #since course code in second column, column index is 1
    flag+=1
    if sheet.cell(row,1).value.casefold()==course_code.casefold():
        #Right now it will print the row of first occurrence
        print(str(row)+"meow")
        break
print(flag) 
