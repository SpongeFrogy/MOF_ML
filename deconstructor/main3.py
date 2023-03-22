from func import cif2mof_timeout, main3



if __name__ == "__main__":
    for cif in main3:
        try:
            cif2mof_timeout(cif, 'all_mofs3.csv')
        except TimeoutError:
            with open('bad_cif.txt', 'w') as bad_list:
                bad_list.write(cif + '\n')
