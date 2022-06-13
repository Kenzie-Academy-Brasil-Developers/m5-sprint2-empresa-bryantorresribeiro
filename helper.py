import ujson as json
import os

def save_to_database(dados:dict, pasta:str, arquivo:str):

    os.system(f'mkdir {pasta}')

    with open(f'{pasta}/{arquivo}', "w") as file:
        json.dump(dados, file, indent=4)

def read_database(path):

    with open(path, "r") as file:
        return json.load(file)