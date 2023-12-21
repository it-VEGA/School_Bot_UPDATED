import openpyxl
def formating_string(input_msg):
    try:
        numbers = ''.join(filter(str.isdigit, input_msg))
        text = ''.join(filter(str.isalpha, input_msg))
        return numbers,text
    except TypeError as error:
        print(f"formating_string - {error}")
def add_to_excel(target_list):
    workbook = openpyxl.load_workbook('Отсутствующие.xlsx')
    sheet = workbook.active
    sheet.append(target_list)
    workbook.save('Отсутствующие.xlsx')

