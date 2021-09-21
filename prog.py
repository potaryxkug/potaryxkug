import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# importer ma fonction liste_token
from MesFichiersFonctions import liste_prix_token, liste_token

response = requests.get("https://courscryptomonnaies.com/")
content= response.content
parser = BeautifulSoup(content,"html.parser")

# lecture de mes contenu avec la fonction liste_token
my_list_token = liste_token(parser,"span","display:flex")
#print(my_list_token)

# lecture de mes contenu avec la fonction liste_prix_token
my_list_prix_token = liste_prix_token( parser , "span","")
#print(mylist_prix_token)

# Création de data frame
df = pd.DataFrame(list(zip(my_list_token,my_list_prix_token)), columns = ['Token_name','Price'])
print(df)