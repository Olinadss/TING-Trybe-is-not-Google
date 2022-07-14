from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # path_list = list()

    if len(instance):
        for index_search in range(len(instance)):
            if path_file == instance.search(index_search)["nome_do_arquivo"]:
                return None

    read_file = txt_importer(path_file)

    last_file_added = dict()

    last_file_added["nome_do_arquivo"] = path_file
    last_file_added["qtd_linhas"] = len(read_file)
    last_file_added["linhas_do_arquivo"] = read_file

    instance.enqueue(last_file_added)
    print(last_file_added, file=sys.stdout)


def remove(instance):
    if not len(instance):
        print("Não há elementos", file=sys.stdout)
    else:
        remove_instance = instance.dequeue()
        file_remove = remove_instance["nome_do_arquivo"]
        print(f"Arquivo {file_remove} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
