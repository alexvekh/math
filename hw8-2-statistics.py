"""
Завантаж набір даних Product Advertising Data (посилання на диск). 
Набір даних складається із семи стовпчиків, що відображають витрати на рекламу на різних платформах — 
телебачення, білборди, Google Ads, соціальні медіа, інфлюенс-маркетинг та партнерський маркетинг.

Останній стовпчик, "Product_Sold", містить кількісну оцінку відповідної кількості проданих одиниць товару. 
Для кожної колонки порахуй середнє значення, дисперсію, стандартне відхилення, 
побудуй гістограму розподілу показника, перевір на нормальність розподілу та порахуй кореляцію з Product_Sold.
"""

from google.colab import drive
drive.mount('/content/drive')


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
#url = '<https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/edit#gid=954244094>'
#url = url[:url.find('/edit')] + '/export?format=csv'
url = '/content/drive/MyDrive/Advertising_Data.csv'
df = pd.read_csv(url)

# Завантажити набір даних
#df = pd.read_csv('/content/drive/MyDrive/Advertising_Data.csv')

# Визначити стовпчики витрат на рекламу
advertising_columns = df.columns#[:-1]

# Цикл по стовпчиках витрат на рекламу
for col in advertising_columns:
    print(col)
    print('-'*10)

    # **1. Середнє значення, дисперсія, стандартне відхилення**
    mean_value = df[col].mean()
    variance = df[col].var()
    std_dev = df[col].std()

    print(f"Середнє значення: {mean_value:.2f}")
    print(f"дисперсія: {std_dev:.2f}")
    print(f"стандартне відхилення: {variance:.2f}")

    # **2. Гістограма розподілу**
    df[col].hist()

    # **3. Перевірка на нормальність розподілу**
    from scipy import stats
    normality_test = stats.jarque_bera(df[col])
    print(f"Тест Jarque-Bera для {col}: p-value = {normality_test[1]:.4f}")

    # **4. Кореляція з Product_Sold**
    correlation = df[col].corr(df['Product_Sold'])
    print(f"Кореляція {col} з Product_Sold: {correlation:.2f}")

    # **5. Візуалізація**
    plt.show()

# **Опис Product_Sold**
print(df['Product_Sold'].describe())