def exists_word(word, instance):
    word_list = list()

    for file_position in range(len(instance)):
        number_of_occurrences = list()
        file = instance.search(file_position)

        for index, word_value in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in word_value.lower():
                number_of_occurrences.append({"linha": index + 1})

        if number_of_occurrences:
            word_list.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": number_of_occurrences
            })

    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
