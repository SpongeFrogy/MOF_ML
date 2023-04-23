from wrapt_timeout_decorator import *
from mofid.run_mofid import cif2mofid_csv

@timeout(90)
def cif2mof_timeout(file, csv_path):
    """
    file -- path ti cif
    csv_path -- file.csv where to write a row of params with sep=','
    """
    cif2mofid_csv(file, csv_path=csv_path)


if __name__ == '__main__':
    cif2mof_timeout("CIFs/cifs/(1) 10.1038_s41467-021-24188-4/as-MOF-5-C7 2040922.cif", 'test.csv')

