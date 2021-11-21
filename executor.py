import csv


with open("anime.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for i in row:
            if row[i] == 'Midoriyama Koukou Koushien-hen':
                print(row['Anime-PlanetID'])

