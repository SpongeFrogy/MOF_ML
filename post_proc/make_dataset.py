import pandas as pd
import numpy as np
import os, fnmatch
from gemmi import cif
from mofid.run_mofid import cif2mofid_csv





with open('bad_data.txt', 'w') as bad_list:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if fnmatch.fnmatch(file,"*.cif"):
                try:
                    table = cif.read_file(root + '/' + file).sole_block().find(
                        ["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma", "_symmetry_cell_setting"])
                    table = cif.read_file(root + '/' + file).sole_block().find(
                        ["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma", "_space_group_crystal_system"])
                except ValueError:
                    print('что-то с файлом')
                    bad_list.write(file + '\n')

                else:
                    table = cif.read_file(root + '/' + file).sole_block().find(
                        ["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma", "_symmetry_cell_setting"])
                    table_new_name_for_symmetry = cif.read_file(root + '/' + file).sole_block().find(
                        ["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma", "_space_group_crystal_system"])
                    if table.width() > 6:
                        # print(root+'/'+file)
                        new_row = pd.DataFrame(table_to_pdRow(table), columns=columns,  index=[file])
                        df = pd.concat([df, new_row])
                    elif table_new_name_for_symmetry.width() > 6:
                        new_row = pd.DataFrame(table_to_pdRow(table_new_name_for_symmetry), columns=columns,  index=[file])
                        df = pd.concat([df, new_row])
                    else:
                        bad_list.write(file + '\n')
                    print(file)
        df.to_csv('base5k.csv')


