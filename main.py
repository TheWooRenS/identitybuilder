import json
import random


def get_Identity():

    surname_file = 'surnames.txt'
    with open(surname_file, 'r', encoding='utf-8') as file:
        surnames = file.readlines()
    surnames = [surname.strip() for surname in surnames]
    random_surname = random.choice(surnames)
    json_file_path = 'names.json'
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    name_list = [{'name': item['name'], 'sex': item['sex']} for item in data if 'name' in item and 'sex' in item]
    random_name = random.choice(name_list)
    with open('provinces.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    random_il = random.choice(data["data"])
    random_ilce = random.choice(random_il["ilceler"])

    il = f"{random_il['il_adi']}"
    ilce = f"{random_ilce['ilce_adi']}"
    bilgi = f"{random_il['kisa_bilgi']}"

    country = ilce.capitalize() + " / " + il.upper()

    human = [str(f"{random_name['name']}"), random_surname ,str(f'{random_name['sex']}'), random.randint(10000000000,99999999999), str(country),str(bilgi)]
    return human
