import pandas as pd
import random 
# 1 Dataframe с информацией о 20 сотрудниках компании
print("1. Информация о сотрудниках компании") 
departments = ['Отдел продаж', 'Отдел разработки', 'Отдел маркетинга', 'Отдел финансов']
male_names = ['Павел', 'Егор', 'Иван', 'Сергей', 'Олег']
female_names = ['Мария', 'Анна', 'Марина', 'Екатерина', 'София']
male_surnames = ['Иванов', 'Петров', 'Сидоров', 'Ефремов', 'Николаев']
female_surnames = ['Иванова', 'Петрова', 'Сидорова', 'Ефремова', 'Николаева']
positions = ['Менеджер', 'Разработчик', 'Маркетолог', 'Финансовый аналитик']

# генерируем данные о сотрудниках
employees = []
names_used = set()  # класс множетсва неупорядоченных уникальных элементов
surnames_used = set()

while len(employees) < 20:
    if random.choice([True, False]):
        names = male_names
        surnames = male_surnames
    else:
        names = female_names
        surnames = female_surnames

    department = random.choice(departments)
    position = random.choice(positions)
    salary = random.randint(90000, 280000) # генерация рандомных чисел от 90000 до 280000

    # проверка на уникальное имя и фамилию
    name = random.choice(names)
    surname = random.choice(surnames)
    if (name, surname) in names_used and surname in surnames_used:
        continue

    names_used.add((name, surname))
    surnames_used.add(surname)

    employees.append([name, surname, department, position, salary])

# создаем и выводим DataFrame с данными о сотрудниках
data = pd.DataFrame(employees, columns=['Имя', 'Фамилия', 'Отдел', 'Должность', 'Зарплата'])
print(data)
min_salary = data['Зарплата'].min()
print("Минимальная зарплата:", min_salary)
max_salary = data['Зарплата'].max()
print("Максимальная зарплата:", max_salary)

# 2 вычисление среднего балла успеваемости студентов и сформирует список учащихся по убыванию среднего балла.

print("#2 Информация о успеваемости")
data = pd.read_csv(r'F:/Programming/python labs/4/students.csv')

# вычисляем средний балл каждого студента
data['Средний балл'] = data[['Математика', 'Физика', 'Химия', 'Информатика', 'История']].mean(axis=1).round(2) # round - округление до двух знаков после запятой 

# сортируем список по среднему баллу в порядке убывания
sorted_data = data.sort_values(by='Средний балл', ascending=False)
print(sorted_data)


