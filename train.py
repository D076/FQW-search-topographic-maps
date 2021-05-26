replace_dict = {'~': '-',
                '!': '1',
                'l': '1',
                '—': '-',
                'У': 'V',
                'Ш': 'III'}

potential_nomenclature = ['l4-44-107', 'l4-44-УШ']
print(potential_nomenclature)
new_potential_nomenclature = []
for word in potential_nomenclature:
    for i in replace_dict:
        print(word)
        print(i)
        j = replace_dict.get(i)
        print(j)
        word = word.replace(i, j)
        print(word)
    new_potential_nomenclature.append(word)

potential_nomenclature = new_potential_nomenclature
print(potential_nomenclature)
