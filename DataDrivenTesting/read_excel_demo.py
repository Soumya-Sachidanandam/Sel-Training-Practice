
#
# import xlrd
#
# path=r'C:\Users\Naveen\PycharmProjects\Selenium_Training\DataDrivenTesting\TestData.xlsx'
# workbook = xlrd.open_workbook(path)         #book object
#
# worksheet=workbook.sheet_by_name('reg')     #sheet object
#
# rows=worksheet.get_rows()                      #handling sheet object by converting into generator object
#
# header=next(rows)   #to remove header or first row we use next() or first row data i.e header we are storing in rows using next()
#
#
# for ele in rows:
#         print(ele[0].value,ele[1].value)   #Here if we give ele[1] it prints dataset1 and if we give ele[2] it prints data set 2


'''
Note: Above is the approach we follow without using functions. But in above approach filepath and sheetname are the once which vary we

keep them as positional arguments
'''
###########################################################################################################################################
'''
Using functions we are generalizing the approach
'''
#
#
# import xlrd
#
# def reading_testdata(filepath,sheetname):
#     workbook = xlrd.open_workbook(filepath)
#     worksheet=workbook.sheet_by_name(sheetname)
#     rows=worksheet.get_rows()
#     header=next(rows)
#
#     d={}
#
#     for ele in rows:
#             d[ele[0].value]=ele[i].value   #d{firstname:'Ganga',lastname:'Shikre' etc}
#
#     return d
#
#
#     #Here we are returning the dict d value to the function call in Demo_Register file

##############################################################################################





import xlrd

def reading_testdata(filepath,sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet=workbook.sheet_by_name(sheetname)
    rows=worksheet.get_rows()
    header=next(rows)

    d={}

    for i in range(1,5):
        for ele in rows:
            d[ele[0].value]=ele[i].value   #d{firstname:'Ganga',lastname:'Shikre' etc}

    return d


































