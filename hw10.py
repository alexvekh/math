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

# Заміна значень бінарних ознак на 0 та 1
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0}).astype(int)
df["Smoking status"] = df["Smoking status"].map({"Yes": 1, "No": 0}).astype(int)
df.head()

# Перетвоння Bedtime та Wakeup time string до float години
def get_hour_float(ts):
  datetime_obj = pd.to_datetime(ts)  # Convert to datetime object
  return datetime_obj.hour + datetime_obj.minute / 60  # Extract hour and add minutes as fraction

df["Bedtime"] = df["Bedtime"].apply(get_hour_float)
df["Wakeup time"] = df["Wakeup time"].apply(get_hour_float)
df.head()

# перевірка на пропущені значення в таблиці
print(df.isnull().sum())
# print(sleep_data.isna().sum())

# видалення пропущених значеннь з таблиці
df = df.dropna(axis=0)
df.head()
df.describe()

# гістограми розподілу
cols = ['Age', 'Gender', 'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency']

def create_histogram(column_name):
    plt.figure(figsize=(4, 3))
    df[col].plot(kind='hist', bins=20, title=col)
    plt.gca().spines[['top', 'right',]].set_visible(False)
    plt.show()
for col in cols:
    create_histogram(col)

# для картинки

plt.figure(figsize=(4, 3))
# Count occurrences of each category (1 - Male, 2 - Female)
gender_counts = df['Gender'].value_counts()

  # Create labels for the bars
labels = ["Male" if val == 1 else "Female" for val in gender_counts.index]

  # Create the histogram with labels
colors = ['blue' if val == 1 else 'red' for val in gender_counts.index]

gender_counts.plot(kind='bar', color=colors, edgecolor='black', title='Gender')

plt.xticks(range(len(labels)), labels)  # Set custom x-axis labels

plt.gca().spines[['top', 'right']].set_visible(False)

plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Подивитись розподіли
sb.pairplot(df.drop('ID', axis=1))

sb.scatterplot(x=df['Bedtime'], y=df['Sleep efficiency'],)

# Зміщення "Bedtime"
df['Bedtime'] = df['Bedtime'].apply(lambda x: (x - 21) % 24)
sb.scatterplot(x=df['Bedtime'], y=df['Sleep efficiency'],)

sb.scatterplot(x=df['Wakeup time'], y=df['Sleep efficiency'],)

df.columns

df.head()

numeric_cols = ['Age', 'Gender', 'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency']
sleep_drop_numeric = df[numeric_cols]
correlation_matrix = sleep_drop_numeric.corr()
# Print the correlation matrix as a table
print(correlation_matrix.to_string())

pearsoncorr = df[['Age', 'Gender', 'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency']].corr(method='pearson')
pearsoncorr

import seaborn as sb
fig, ax = plt.subplots(figsize=(14, 8))
sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=1)
fig.tight_layout()

# Спостерігаємо високу кореляцію:
#              між 'Bedtime' та 'Wakeup time' (0,9) тому  приймаємо рішення видалити 'Bedtime' (тому що воно має сміщені дані)
#              між 'Deep sleep percentage', та 'Light sleep percentage' (-0.98) тому приймаємо рішення видалити 'Light sleep percentage' (який трохи більше корелює з таргетом)


# -----------------------
# Будування моделі
## Модель 1
### Вік стать та показники сну на алгоритмі DecisionTreeRegressor
### 'Age', 'Gender', 'Wakeup time', 'Sleep duration', 'REM sleep percentage', 'Deep sleep percentage'. ('Bedtime' видалено із-за сильної кореляції з 'Wakeup time') ('Light sleep percentage' видалено із-за сильної кореляції з 'Deep sleep percentage')

# Для тренування нам треба два набори даних: параметри та ціль для прогнозування.

sleep_features = ['Age', 'Gender', 'Wakeup time', 'Sleep duration', 'REM sleep percentage', 'Deep sleep percentage']
X = df[sleep_features] # параметри
y = df["Sleep efficiency"] # ціль
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
x_train.head()


from sklearn.tree import DecisionTreeRegressor
model1 = DecisionTreeRegressor(random_state=1)
model1.fit(x_train, y_train)

# зробимо прогнози для тестової групи
# pred_train = model.predict(x_train)
pred_test = model1.predict(x_test)
print("Порівнюємо прогноз для тестової групи:")
print("Передбачення:")
print(pred_test.tolist())
print("Первинні значення:")
print(y_test.values.tolist())

import matplotlib.pyplot as plt

# Assuming you have your actual values (y) and predicted values (predictions)

# Create the comparison plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

plt.scatter(y_test, pred_test, color='blue', label='Actual vs. Predicted')
plt.plot([0.2, 1], [0.2, 1], color='red', linestyle='--', label='Perfect Prediction Line')  # Add a reference line for perfect prediction
plt.xlabel('Actual Sleep Efficiency')
plt.ylabel('Predicted Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.legend()
plt.grid(True)
plt.show()

# Create the bar plot
plt.figure(figsize=(18, 6))  # Adjust figure size as needed
x = range(len(y_test))  # Shared x-positions for both bars
width = 0.35  # Bar width for better separation
plt.bar([i - width for i in x], pred_test, width, color='gray', label='Predicted Sleep Efficiency', alpha=0.7)
plt.bar(x, y_test, width, color='blue', label='Actual Sleep Efficiency', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.xticks([i + width/2 for i in x], range(len(y_test)))  # Set x-ticks in the middle of bar groups
plt.legend()
plt.grid(axis='y')
plt.show()

print(f'MSE: {mean_squared_error(y_test, pred_test)}')  # Середня квадратична похибка
                                                        # MAE = Середня абсолютна похибка
print(f'MAPE: {mean_absolute_percentage_error(y_test, pred_test)}') # Середня похибка у відсотках
print(f'RSQ: {r2_score(y_test, pred_test)}')  #Коефіцент детермінації (наскільки модель краща за середній прогноз) (from 0 to 1, 1 = is perfect, 0 = is nothing - like just say mean, - = very bad)

# -------------------------
# Модель 2
## Шкідливі звички на алгоритмі DecisionTreeRegressor
### 'Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency'.

# Model2
sleep_features2 = ['Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency']
X = df[sleep_features2] # параметри
y = df["Sleep efficiency"] # ціль
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
x_train.head()

model2 = DecisionTreeRegressor(random_state=1)
model2.fit(x_train, y_train)

# зробимо прогнози для тестової групи
# pred_train = model.predict(x_train)
pred_test2 = model2.predict(x_test)

print("Порівнюємо прогноз для тестової групи:")
print("Передбачення:")
print(pred_test2.tolist())
print("Первинні значення:")
print(y_test.values.tolist())


import matplotlib.pyplot as plt
# Assuming you have your actual values (y) and predicted values (predictions)
# Create the comparison plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.scatter(y_test, pred_test2, color='blue', label='Actual vs. Predicted')
plt.plot([0.2, 1], [0.2, 1], color='red', linestyle='--', label='Perfect Prediction Line')  # Add a reference line for perfect prediction
plt.xlabel('Actual Sleep Efficiency')
plt.ylabel('Predicted Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.legend()
plt.grid(True)
plt.show()


# Create the bar plot
plt.figure(figsize=(18, 6))  # Adjust figure size as needed
x = range(len(y_test))  # Shared x-positions for both bars
width = 0.35  # Bar width for better separation
plt.bar([i - width for i in x], pred_test2, width, color='gray', label='Predicted Sleep Efficiency', alpha=0.7)
plt.bar(x, y_test, width, color='blue', label='Actual Sleep Efficiency', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.xticks([i + width/2 for i in x], range(len(y_test)))  # Set x-ticks in the middle of bar groups
plt.legend()
plt.grid(axis='y')
plt.show()

print(f'MSE 2: {mean_squared_error(y_test, pred_test2)}')  # Середня квадратична похибка
print(f'MAPE 2: {mean_absolute_percentage_error(y_test, pred_test2)}') # Середня похибка у відсотках
print(f'RSQ 2: {r2_score(y_test, pred_test2)}')  #Коефіцент детермінації (наскільки модель краща за середній прогноз) (from 0 to 1, 1 = is perfect, 0 = is nothing - like just say mean, - = very bad)

#---------------------------
# Модель 3
## Всі параметри на алгоритмі DecisionTreeRegressor
### 'Age', 'Gender', 'Wakeup time', 'Sleep duration', 'REM sleep percentage', 'Deep sleep percentage','Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency'.
# Model3
sleep_features3 = ['Age', 'Gender', 'Wakeup time', 'Sleep duration', 'REM sleep percentage', 'Deep sleep percentage','Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency']
X = df[sleep_features3] # параметри
y = df["Sleep efficiency"] # ціль
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
x_train.head()

model3 = DecisionTreeRegressor(random_state=1)
model3.fit(x_train, y_train)

# зробимо прогнози для тестової групи
# pred_train = model.predict(x_train)
pred_test3 = model3.predict(x_test)
print("Порівнюємо прогноз для тестової групи:")
print("Передбачення:")
print(pred_test3.tolist())
print("Первинні значення:")
print(y_test.values.tolist())

import matplotlib.pyplot as plt

# Assuming you have your actual values (y) and predicted values (predictions)

# Create the comparison plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.scatter(y_test, pred_test3, color='blue', label='Actual vs. Predicted')
plt.plot([0.2, 1], [0.2, 1], color='red', linestyle='--', label='Perfect Prediction Line')  # Add a reference line for perfect prediction
plt.xlabel('Actual Sleep Efficiency')
plt.ylabel('Predicted Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.legend()
plt.grid(True)
plt.show()

print(f'MSE 3: {mean_squared_error(y_test, pred_test3)}')  # Середня квадратична похибка
print(f'MAPE 3: {mean_absolute_percentage_error(y_test, pred_test3)}') # Середня похибка у відсотках
print(f'RSQ 3: {r2_score(y_test, pred_test3)}')  #Коефіцент детермінації (наскільки модель краща за середній прогноз) (from 0 to 1, 1 = is perfect, 0 = is nothing - like just say mean, - = very bad)


# Модель 4 (RandomForestRegressor)
## Всі параматри на алгоритмі RandomForestRegressor
### 'Age', 'Gender', 'Wakeup time', 'Sleep duration', 'REM sleep percentage', 'Deep sleep percentage','Awakenings', 'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 'Exercise frequency'.

from sklearn.ensemble import RandomForestRegressor
model4 = RandomForestRegressor()
model4.fit(x_train, y_train)

# зробимо прогнози для тестової групи
# pred_train = model.predict(x_train)
pred_test4 = model4.predict(x_test)
print("Порівнюємо прогноз для тестової групи:")
print("Передбачення:")
print(pred_test4.tolist())
print("Первинні значення:")
print(y_test.values.tolist())

import matplotlib.pyplot as plt

# Assuming you have your actual values (y) and predicted values (predictions)

# Create the comparison plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.scatter(y_test, pred_test4, color='blue', label='Actual vs. Predicted')
plt.plot([0.2, 1], [0.2, 1], color='red', linestyle='--', label='Perfect Prediction Line')  # Add a reference line for perfect prediction
plt.xlabel('Actual Sleep Efficiency')
plt.ylabel('Predicted Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.legend()
plt.grid(True)
plt.show()

print(f'MSE 4: {mean_squared_error(y_test, pred_test4)}')  # Середня квадратична похибка
print(f'MAPE 4: {mean_absolute_percentage_error(y_test, pred_test4)}') # Середня похибка у відсотках
print(f'RSQ 4: {r2_score(y_test, pred_test4)}')  #Коефіцент детермінації (наскільки модель краща за середній прогноз) (from 0 to 1, 1 = is perfect, 0 = is nothing - like just say mean, - = very bad)

# Create the bar plot
plt.figure(figsize=(18, 6))  # Adjust figure size as needed
x = range(len(y_test))  # Shared x-positions for both bars
width = 0.35  # Bar width for better separation

plt.bar([i - width for i in x], pred_test4, width, color='gray', label='Predicted Sleep Efficiency', alpha=0.7)
plt.bar(x, y_test, width, color='blue', label='Actual Sleep Efficiency', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Sleep Efficiency')
plt.title('Comparison of Actual vs. Predicted Sleep Efficiency')
plt.xticks([i + width/2 for i in x], range(len(y_test)))  # Set x-ticks in the middle of bar groups
plt.legend()
plt.grid(axis='y')
plt.show()

# ----------------------------------
# Результати:
## -З двох моделей, тренованих на половині даних Модель 2 (тренована на шкідливих звичках) демонструє трохи кращу продуктивність, ніж Модель 1, маючи трохи нижчі значення MSE і MAPE, а також значно вище значення RSQ.
## -Модель 3 показує помітно кращу загальну продуктивність, маючи нижчі значення MSE (0.00332) і MAPE (0.0590), а також вище значення RSQ (0.8463), що пояснюється більшою кількістю параметрів
## -Модель 4 демонструє найкращу загальну продуктивність з усії попередніх, маючи найнижчі значення MSE (0.001655) і MAPE (0.0436), а також найвище значення RSQ (0.9234)

# Висновки:
## -Збільшення параметрів, задіяних у навчанні призводить до покращення продуктивності моделі
## -Достатньо посередні на перший погляд параметри можуть виявитися більш корисними ніж найближчі.
## -RandomForestRegressor більш точний, ніж DecisionTreeRegressor, завдяки агрегуванню передбачень багатьох дерев (ще раз підтверджено).





