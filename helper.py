import ujson as json
import os

def save_to_database(dados:dict, pasta:str, arquivo:str):

    os.system(f'mkdir empresas/{pasta}')

    with open(f'empresas/{pasta}/{arquivo}', "w") as file:
        json.dump(dados, file, indent=4)

def read_database(path):

    with open(path, "r") as file:
        return json.load(file)