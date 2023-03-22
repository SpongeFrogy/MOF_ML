from func import cif2mof_timeout, main



if __name__ == "__main__":
    for cif in main:
        try:
            cif2mof_timeout(cif, 'all_mofs0.csv')
        except TimeoutError:
            with open('bad_cif.txt', 'w') as bad_list:
                bad_list.write(cif + '\n')