from func import cif2mof_timeout, main2



if __name__ == "__main__":
    for cif in main2:
        try:
            cif2mof_timeout(cif, 'all_mofs2.csv')
        except TimeoutError:
            with open('bad_cif.txt', 'w') as bad_list:
                bad_list.write(cif + '\n')


