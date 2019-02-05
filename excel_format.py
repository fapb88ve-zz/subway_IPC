import pandas as pd
import xlsxwriter as xlsx

class Writer():

    def __init__(self, title):
        workbook = xlsx.Workbook(title+".xlsx")
        return workbook.add_worksheet()
