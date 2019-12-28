import csv
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv(r'Data\Data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))


languages, popularity = map(list, zip(*language_counter.most_common(15)))

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Number Of Users')

plt.tight_layout()

plt.show()
