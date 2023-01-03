from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import selenium as sl
import webdriver-manager as wm

# SETUP

#setup the webscrapping

from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
```


```python
#going to the page with all the pokemon names
page_url = "https://pokemondb.net/pokedex/national"
driver.get(page_url)
```


```python
#getting the name of the pokemon
pokemonName = driver.find_elements(By.CLASS_NAME, 'ent-name')
```


```python
#filling a list with the name and URL of each Pokemon

pokemon = []

for apelido in pokemonName:
    pkmn_url = apelido.get_attribute('href')
    NomePkmn = apelido.text
    pokemon.append({'Nome Pokemon': NomePkmn, 'Link': pkmn_url})
```


```python
pokemon
```


```python
#Going through the first list and retrieving the Total Base Power of each Pokemon

lista_base = []

for pkmn in pokemon:
    driver.get(pkmn['Link'])
    time.sleep(0.5)
    elementos = driver.find_elements(By.CLASS_NAME, "cell-total")
    
    for elem in elementos:
        lista_base.append({'Total':elem.text})
```


```python
lista_base
```


```python
dfBase = pd.DataFrame(lista_base)
```


```python
dfBase
```


```python
dfPokemon = pd.DataFrame(pokemon)
```


```python
dfPokemon
```


```python

```
