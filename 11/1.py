import csv
animals = [
    {"id": 1, "Кличка": "Шарик", "Возраст": 3, "Пол": "М", "ID Корма": 1},
    {"id": 2, "Кличка": "Бобик", "Возраст": 4, "Пол": "М", "ID Корма": 2},
    {"id": 3, "Кличка": "Жучка", "Возраст": 2, "Пол": "Ж", "ID Корма": 1}
]

feed = [
    {"id": 1, "Вид": "Еда для собак", "Фирма": "Pedigree", "Цена": 100, "Название": "Питание для взрослых Pedigree"},
    {"id": 2, "Вид": "Еда для собак", "Фирма": "Chappy", "Цена": 120, "Название": "Питание для взрослых Chappy"},
]

def add_animal(animal):
    animals.append(animal)

def remove_animal(id):
    global animals 
    animals = [animal for animal in animals if animal["id"] != id]

def update_animal(id, updated_info):
    for animal in animals:
        if animal["id"] == id:
            animal.update(updated_info)
            break


# Выводим информацию о животных (3-е задание)
for animal in animals:
    feed_info = next(item for item in feed if item["id"] == animal["ID Корма"])
    print(f'{animal["Кличка"]} {animal["Пол"]} {animal["Возраст"]} {feed_info["Название"]} {feed_info["Цена"]}')

# Выводим информацию о том, сколько животных едят каждый вид корма (4-е задание)
for food in feed:
    count = sum(1 for animal in animals if animal['ID Корма'] == food['id'])
    print(f'{food["Название"]}: {count} животных')

# Записываем данные в CSV
with open('animals.csv', 'w', newline='') as csvfile:
    fieldnames = ["id", "Кличка", "Возраст", "Пол", "ID Корма"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(animals)

with open('feed.csv', 'w', newline='') as csvfile:
    fieldnames = ["id", "Вид", "Фирма", "Цена", "Название"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(feed)

# Чтение данных из CSV
def load_data_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

print()
animals_from_file = load_data_from_csv('animals.csv')
feed_from_file = load_data_from_csv('feed.csv')

# Выводим информацию из CSV
for animal in animals_from_file:
    feed_info = next(item for item in feed_from_file if item["id"] == animal["ID Корма"])
    print(f'{animal["Кличка"]} {animal["Пол"]} {animal["Возраст"]} {feed_info["Название"]} {feed_info["Цена"]}')
