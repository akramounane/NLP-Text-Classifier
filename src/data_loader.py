import numpy as np
import pandas as pd
'''Ce fichier python contient un seul fonction principal
    et a pour objective de charger le dataset de message labeliser fournie sur la page hugingface suivante
    https://huggingface.co/datasets/dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset
    ce csv ccontient plusieur sms labelise dans plusieur langue 
    donc le fonction integrera le choix de la langue qui sera passer en parametre en plus su dataset
    je m'interserai a la methode de choix de la langue plus tard 
    je teste les commande dans ce google calab
    https://colab.research.google.com/drive/1rr1WtxfhvQiJi8dQWzhzn5Vsv-dWJe15?usp=sharing
'''

def load_dataset(dataset , langue):
    data = pd.read_csv(dataset) # j'aurais pu integrer le chargement automatique du dataset depuis le site d'hugingface mais cette fontion n'aurais plus aucun intert
    data = data[['labels','text_' + langue]]
    return data