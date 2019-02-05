import pandas as pd
import datetime as dt
import re
import os
import numpy as np


class ReaderTable():

    def __init__(self):
        now = dt.datetime.now()
        self.table_name = "Global Mapping Table {}".format(
                                        now.strftime('%m.%d.%Y'))
        try:
            self.table = pd.read_excel(self.table_name,
                                            sheet_name='Domestic Items')
        except IOError as err:
            print('File "{}" was not found in folder.'.format(self.table_name))
            print()
            new_name = re.compile(
                                r'\w+\s\w+\s\w+ (\d?\d).(\d?\d).(\d{4}) V(\d).xlsx')
            names = []
            for f in os.listdir(os.getcwd()):
                if new_name.match(f):
                    catch = new_name.match(f)
                    names.append([catch.group(i) for i in range(1, 5)])
                    #print(names)

            names = sorted(names, key = lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
            self.table_name = "Global Mapping Table {}.{}.{} V{}.xlsx".format(
                                                                        names[0][0],
                                                                        names[0][1],
                                                                        names[0][2],
                                                                        names[0][3])
            print('Accessing file: "{}"'.format(self.table_name))
            self.table = pd.read_excel(
                                self.table_name, sheet_name='Domestic Items').iloc[:,:5]

    def data_getter(self, spc = None, gtin = None, email_title):
        self.user_spc = spc
        self.user_gtin = gtin
        self.user_title = email_title
        table = self.table
        if all([spc, gtin]):
            data = table[(table.SPC == spc) & (table.GTIN == gtin)]
            self.data = data
            return data
        elif spc:
            data = table[table.SPC == spc]
            self.data = data
            return data
        elif gtin:
            data = table[table.GTIN == gtin]
            self.data = data
            return data
        else:
            self.data = None
            return table

    def data_export(self, data):
        #NEED TO CREATE A SEPARATE CLASS FOR FORMATTING EXCEL FILES
        self.data.to_excel(self.email_title + ".xlsx")


if __name__ == "__main__":
    print(ReaderTable().data_getter())
