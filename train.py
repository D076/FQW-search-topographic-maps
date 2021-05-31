replace_dict = {'~': '-',
                '!': '1',
                'l': '1',
                '—': '-',
                'У': 'V',
                'Ш': 'III'}
spec_symbols = ['°', '`', '‘', '*', '^', '#', '@', '.', '"', "'",
                '%', ':', ';', '$', '№', '~', '=', '+', '(', ')',
                '{', '}', '[', ']']
first_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'G', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'Z'
                'А', 'М', 'О', 'Т', 'Е', 'К', 'Н',
                '0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', '10', '11', '12', '13',
                '14', '15', '16', '17', '18', '19', '20', '21']
second_letter = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
third_letter = ['А', 'Б', 'В', 'Г', '1', '2', '3', '4', 'A',
                '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36',
                'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI',
                'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
                'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII',
                'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI',
                '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014',
                '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028',
                '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042',
                '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056',
                '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070',
                '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084',
                '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098',
                '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
                '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126',
                '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140',
                '141', '142', '143', '144',
                '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
                '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
                '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94',
                '95', '96', '97', '98', '99']
fourth_letter = ['A', 'Б', 'В', 'Г', 'A']
fifth_letter = ['а', 'б', 'в', 'г', 'a']
nomenclature = None
# replace_dict = {'~': '-',
#                 '!': '1',
#                 'l': '1',
#                 '—': '-',
#                 'У': 'V',
#                 'Ш': 'III'}
#
# potential_nomenclature = ['l4-44-107', 'l4-44-УШ']
# print(potential_nomenclature)
# new_potential_nomenclature = []
# for word in potential_nomenclature:
#     for i in replace_dict:
#         print(word)
#         print(i)
#         j = replace_dict.get(i)
#         print(j)
#         word = word.replace(i, j)
#         print(word)
#     new_potential_nomenclature.append(word)
#
# potential_nomenclature = new_potential_nomenclature
# print(potential_nomenclature)
# word = '1-2-3-4'
# print(word.split('-')[6])
# a = []
# for i in range(10, 100):
#     s = str(i)
#
#     a.append(s)

# def checkio(n):
#     result = ''
#     for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
#                              'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
#         result += n // arabic * roman
#         n %= arabic
#         # print('({}) {} => {}'.format(roman, n, result))
#     return result
#
# for i in range(37):
#     a.append(checkio(i))
#
# print(a)
# word = 'A-22-XXX'
# try:
#     if word.split('-')[0] not in first_letter:
#         print(f'Неверное первое слово {word.split("-")[0]}')
# except Exception:
#     pass
# try:
#     if word.split('-')[1] not in second_letter and word.split('-')[1] is not None:
#         print(f'Неверное второе слово {word.split("-")[1]}')
# except Exception:
#     pass
# try:
#     if word.split('-')[2] not in third_letter and word.split('-')[2] is not None:
#         print(f'Неверное третье слово {word.split("-")[2]}')
# except Exception:
#     pass
# try:
#     if word.split('-')[3] not in fourth_letter and word.split('-')[3] is not None:
#         print(f'Неверное четвертое слово {word.split("-")[3]}')
# except Exception:
#     pass
# try:
#     if word.split('-')[4] not in fifth_letter and word.split('-')[4] is not None:
#         print(f'Неверное пятое слово {word.split("-")[4]}')
# except Exception:
#     pass

potential_nomenclature = ['N-22,23-l', '--', '_-', '4-44—107-—-3', '44-84', '1500-1900', 'Becouc-yeanak',
                          'l4—44-107', 'M-44-23-[-6', 'N-44-1', 'N-44-1', 'N-45', 'XX-XxX', 'А-А',
                          'буро-взрывным', 'Р-ы', '', '-']
copy_potential_nomenclature = list(potential_nomenclature)

for word in potential_nomenclature:
    go_next = False
    word_splitted = word.split('-')
    try:

        if word_splitted[0] not in first_letter:
            print(f'{word} Неверное первое слово {word_splitted[0]}')
            # save_logging(str=f'{word} Неверное первое слово {word_splitted[0]}')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        # if ',' in word_splitted[1]:
        #     word2_splitted = word_splitted[1].split(',')
        #     for w in word2_splitted:
        #         if w not in second_letter:
        #             print(f'{word} Неверное второе слово {word_splitted[1]}')
        #             # save_logging(str=f'{word} Неверное второе слово {word_splitted[1]}')
        #             copy_potential_nomenclature.remove(word)
        #             go_next = True
        #             break
        # if go_next:
        #     continue
        if word_splitted[1] not in second_letter:
            print(f'{word} Неверное второе слово {word_splitted[1]}')
            # save_logging(str=f'{word} Неверное второе слово {word_splitted[1]}')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        # if ',' in word_splitted[2]:
        #     word3_splitted = word_splitted[2].split(',')
        #     for w in word3_splitted:
        #         if w not in third_letter:
        #             log = f'{word} Неверное третье слово {word_splitted[2]}'
        #             print(log)
        #             # save_logging(str=log)
        #             copy_potential_nomenclature.remove(word)
        #             go_next = True
        #             break
        # if go_next:
        #     continue
        if word.split('-')[2] not in third_letter and word.split('-')[2] is not None:
            log = f'{word} неверное третье слово {word_splitted[2]}'
            print(log)
            # save_logging(str=log)
            # save_logging(str=f'неверное третье слово')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        if word.split('-')[3] not in fourth_letter and word.split('-')[3] is not None:
            print(f'{word} Неверное четвертое слово {word.split("-")[3]}')
            # save_logging(str=f'{word} Неверное четвертое слово {word.split("-")[3]}')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        if word.split('-')[4] not in fifth_letter and word.split('-')[4] is not None:
            print(f'{word} Неверное пятое слово {word.split("-")[4]}')
            # save_logging(str=f'{word} Неверное пятое слово {word.split("-")[4]}')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        if word.split('-')[5] is not None:
            print(f'{word} Неверная форма номенклатуры')
            # save_logging(str=f'{word} Неверная форма номенклатуры')
            copy_potential_nomenclature.remove(word)
            continue
    except Exception:
        pass
    try:
        for i in spec_symbols:
            if i in word:
                print(f'{word} Запрещенный символ {i}')
                # save_logging(str=f'{word} Запрещенный символ {i}')
                copy_potential_nomenclature.remove(word)
                break
    except Exception:
        pass
potential_nomenclature = list(copy_potential_nomenclature)
print(potential_nomenclature)