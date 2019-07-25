'''this program checks to see whether the excel file has the string you are searching for and shows all its occurrences'''
import xlrd


#IMPORTANT:now we write the path of the file we gonna use. i have retained the name of the file i used for test but you have to swap the path for it to work for you

path='D:\Downloads\TT SEM I 19-20 (DRAFT110719).xlsx'
#now we try to make the workbook object
workbook= xlrd.open_workbook(path)
#now we try to make 1st sheet object?
sheet = workbook.sheet_by_index(0)
''' IGNORE:this was me just trying stuff out
    #let us check by asking for C1 
    print(sheet.cell_value(0,2))
    #it worked!!!!!
'''
#now i will try to search for a string
#ask the user for a string like BITS F110 or something
search_string=str(input('Input the word you wish to search:'))
flag=0
found_index=(-1,-1)

for row in range(sheet.nrows):
    for column in range(sheet.ncols):
        flag=0
        if search_string.casefold() in str(sheet.cell(row,column).value).casefold():
            found_index=(row+1,column+1)
            flag=1
        if flag==1:
            print("Found in "+str(found_index)+" box")
            input('Press Enter to continue')
if found_index==(-1,-1):
    print("Not found")
else:
    print("Search finished. No more occurrences")
