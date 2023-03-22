from wrapt_timeout_decorator import *
from mofid.run_mofid import cif2mofid_csv
import os, fnmatch

folder = "COD metal-organic_CIFs (5642 items)"

files = list(os.walk(folder))[0][2]


@timeout(90)
def cif2mof_timeout(file, csv_path):
    cif2mofid_csv("COD metal-organic_CIFs (5642 items)" + "/" + file, csv_path=csv_path)


main = files[1684+203:1684+1319]
main2 = files[1684+1319:1684+1319+1319]
main3 = files[1684+1319+1319:]



