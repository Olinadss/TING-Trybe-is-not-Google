import sys


def txt_importer(path_file):
    file = path_file.split(".")
    file_read = list()

    try:
        if file[1] != 'txt':
            return print("Formato inválido", file=sys.stderr)

        file_open = open(path_file)
        lines = file_open.readlines()

        for line in lines:
            treated_line = line.split('\n')
            file_read.append(treated_line[0])
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return file_read
