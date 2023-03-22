import pandas as pd
import numpy as np
import os, fnmatch
from gemmi import cif
from mofid.run_mofid import cif2mofid_csv


"""
 "_cell_length_a", "_cell_length_b", "_cell_length_c", 
 "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma",
 "_symmetry_cell_setting"/"_space_group_crystal_system"
"""
def symmetry_data(ciffile):
    block = cif.read_file(ciffile).sole_block()    
    try:
        attributes = block.find(["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma",
                          "_cell_volume","_symmetry_cell_setting", "_symmetry_space_group_name_Hall"])
    except ValueError:
        attributes = block.find(["_cell_length_a", "_cell_length_b", "_cell_length_c",
                        "_cell_angle_alpha", "_cell_angle_beta", "_cell_angle_gamma",
                          "_cell_volume","_space_group_crystal_system", "_symmetry_space_group_name_Hall"])
    if attributes.width() > 8:
        return attributes
    else:
        return None


"""
надо написать эту часть в баблиотеке
"""
def mofid_attributes(ciffile):
    mofid_key_attributes = cif2mofid_csv(ciffile)
    return mofid_key_attributes


