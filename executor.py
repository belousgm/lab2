import csv


def delete_keys(n):
    del n['Anime-PlanetID']
    del n['Name']
    del n['Alternative Name']
    del n['Number Votes']
    del n['Synopsis']
    del n['Url']


def return_flag_rating(a, b):
    if b != 'Unknown':
        if float(b) >= float(a):
            return True
        return False
    return False


def include_in(a, b):
    if set(a.split(', ')) <= set(b.split(', ')) != '':
        return True
    return False


def not_include_in(a, b):
    if len(set(a.split(', ')) & set(b.split(', '))) != 0:
        return False
    return True


def return_comparison(a, b):
    if a == b:
        return True
    return False


questions = (
    'Введите желаемый минимальный рейтинг: ',
    'Укажите желаемые теги: ',
    'Какие предупреждения стоит исключить? ',
    'Формат показа (TV, Web, Movie etc): ',
    'Количество эпизодов: ',
    'Аниме должно быть закончено? ',
    'Длительность: ',
    'Год начала показа: ',
    'Год окончания: ',
    'Сезоны: ',
    'Студия: '
)
answers = {
    'Rating Score': '',
    'Tags': '',
    'Content Warning': '',
    'Type': '',
    'Episodes': '',
    'Finished': '',
    'Duration': '',
    'StartYear': '',
    'EndYear': '',
    'Season': '',
    'Studios': ''
}

iter_questions = iter(questions)

for i in answers:
    answers[i] = input(next(iter_questions))
    if (i in 'Finished') and (answers[i] not in ['True', 'False']):
        if answers[i].lower() in 'да':
            answers[i] = 'True'
        else:
            answers[i] = 'False'

result = []
with open("anime.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row_clone = row.copy()
        delete_keys(row_clone)
        flag_row = True
        for i in row_clone:
            if answers[i] == '':
                continue
            if i in 'Rating Score':
                flag_row = return_flag_rating(answers[i], row_clone[i])
            elif i in ['Tags', 'Type', 'Studios'] and flag_row:
                flag_row = include_in(answers[i], row_clone[i])
            elif i in 'Content Warning' and flag_row:
                flag_row = not_include_in(answers[i], row_clone[i])
            elif flag_row:
                flag_row = return_comparison(answers[i], row_clone[i])
        if flag_row:
            result.append(row['Name'])

with open("output.txt", 'w', encoding='utf-8') as answerfile:
    for i in result:
        answerfile.write(f'{i}\n')

print('-----\nРезультаты сформированы и помещены в файл output.txt!')
