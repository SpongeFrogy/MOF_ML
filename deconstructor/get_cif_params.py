from wrapt_timeout_decorator import *
from mofid.run_mofid import cif2mofid_csv

@timeout(90)
def cif2mof_timeout(file, csv_path):
    """
    file -- path ti cif
    csv_path -- file.csv where to write a row of params with sep=','
    """
    cif2mofid_csv(file, csv_path=csv_path)



