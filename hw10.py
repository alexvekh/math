import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split

url = 'https://docs.google.com/spreadsheets/d/1OPnEAT64Patnj_Ifhwn_pM1c15rsBNIoFrtz38A1_W4/edit#gid=1986277343'
url = url[:url.find('/edit')] + '/export?format=csv'
df = pd.read_csv(url)

# діапазони значень, їх середні та дисперсію, розподіли
df.describe() #На виході отримуємо базові статистичні дані: #count - кількість даних, #mean - середнє арифметичне, #std - стандартне відхилення

df.head() # переглянути перші 5 об'єктів (default=5)

df.info() # подивитись типи даних