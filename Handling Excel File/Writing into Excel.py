

'''
openpyxl

'''

from openpyxl import Workbook

## create the new excel workbook
workbook = Workbook()

## initialize the worksheet
worksheet = workbook.active

## set the title for the worksheet (optional)
worksheet.title = 'M16_data'

## Write the data into the excel file
worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'phone_num'
worksheet['D1'] = 'email_id'

# print(worksheet.values)

data_list =[
    ['Nithya', 'Chennai', 9080704050, 'nithya@gmail.com'],
    ['Naveen', 'Delhi', 9181714151, 'naveen@gmail.com'],
    ['Mehak', 'Mumbai', 9282724252, 'mehak@gmail.com'],
    ['Abhishek', 'Bengaluru', 9383736353, 'abhi@gmail.com']
]

for ele in data_list:
    worksheet.append(ele)

# ## save the excel file
# workbook.save('m16.xlsx')

## To save the excel file in different location
workbook.save(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\training\Files\m16.xlsx')

#######################################################################################################################################


