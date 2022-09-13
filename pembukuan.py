import pandas as pd
import glob
import pathlib
import os

download_path = f'{pathlib.Path().home() / "Downloads"}\*.csv'
csv_files = glob.glob(download_path)
csv_files.sort(key=os.path.getmtime)
csv_files = ''.join(csv_files)
read_file = pd.read_csv(csv_files)
new_name = f'{csv_files.strip("csv")}xlsx'
read_file.to_excel(new_name, index=None, header=True)

import openpyxl

wb = openpyxl.load_workbook(new_name)
sheet = wb.active
sheet['F2'] = 'TOTAL'
sheet['G2'] = 'Uang Masuk'
sheet['G3'] = 'Uang Keluar'
sheet['G4'] = 'Uang Final'
sheet['H2'] = '=SUMIF($C$2:$C$100,">0")'
sheet['H3'] = '=SUMIF($C$2:$C$100,"<0")'
sheet['H4'] = '=H2+H3'

wb.save(new_name)
os.startfile(new_name)