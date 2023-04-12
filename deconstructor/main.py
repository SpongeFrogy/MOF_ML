from get_cif_params import cif2mof_timeout
import os, fnmatch

main_folder = "deconstructor/CIFs/cifs"


def try_get_cif(path, csv):
    try:
        cif2mof_timeout(path, csv)
    except TimeoutError:
        with open('main_dataset_bad_cif.txt', 'w') as bad:
            bad.write(f"{path}\n")
            bad.close()

if __name__ == '__main__':
    for folder in os.listdir(main_folder):
        for file in os.listdir(f"{main_folder}/{folder}"):
            if fnmatch.fnmatch(file, '*.cif'):
                if file.lower().find('from') != -1 or file.lower().find('initial') != -1 or file.lower().find('phase i') != -1 or file.lower().find('based on') != -1:
                    try_get_cif(f"{main_folder}\{folder}\{file}", 'deconstructor/main_dataset/main_dataset_from.csv')
                elif file.lower().find('to') != -1 or file.lower().find('phase ii') != -1:
                    try_get_cif(f"{main_folder}\{folder}\{file}", 'deconstructor/main_dataset/main_dataset_to.csv')
                else:
                    try_get_cif(f"{main_folder}\{folder}\{file}", 'deconstructor/main_dataset/main_dataset_unmarked.csv')



# if __name__ == "__main__":
#     for cif in main:
#         try:
#             cif2mof_timeout(cif, 'all_mofs0.csv')
#         except TimeoutError:
#             with open('bad_cif.txt', 'w') as bad_list:
#                 bad_list.write(cif + '\n')


