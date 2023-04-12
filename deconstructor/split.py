delimiter = "# This file contains crystal structure data downloaded from the "  # строка-разделитель
filename = "deconstructor/CIFs/cifs/(3) 10.1038_s41586-021-03880-x/2080245-2080336.cif"  # имя исходного файла
output_dir = "deconstructor/CIFs/cifs/(3) 10.1038_s41586-021-03880-x/"  # директория для сохранения выходных файлов

# C:\Users\droid\MOF_ML\deconstructor\CIFs\cifs\(3) 10.1038_s41586-021-03880-x\2080245-2080336.cif

import os

#print(os.listdir("deconstructor/CIFs"))

# Чтение исходного файла
with open(filename, "r") as f:
    text = f.read()

# Разделение текста на части по строке-разделителю
parts = text.split(delimiter)

# Сохранение каждой части в отдельный файл
for i, part in enumerate(parts):
    output_filename = f"{output_dir}part_{i}.cif"
    with open(output_filename, "w") as f:
        f.write(part)