from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    size_instance = instance.__len__()

    path_list = list()

    if size_instance:
        for index_search in range(size_instance):
            path_list.append(instance.search(index_search)["nome_do_arquivo"])

    if path_file not in path_list:
        read_file = txt_importer(path_file)

        last_file_added = dict()

        last_file_added["nome_do_arquivo"]: path_file
        last_file_added["qtd_linhas"]: len(read_file)
        last_file_added["linhas_do_arquivo"]: read_file

        print("xablau", last_file_added)

        instance.enqueue(last_file_added)
        print(last_file_added, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
