from openpyxl import load_workbook

class ExcelReader:
    
    path = "resource/testData.xlsx"
    @staticmethod
    def getTestData(sheetName):
        worksheet = load_workbook(ExcelReader.path)
        sheet = worksheet[sheetName]
        
        data = []
        
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))
            data.append(row_data) 
                
        return data