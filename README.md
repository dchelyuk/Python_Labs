# Python_Labs
***This repo is for storing python labs from LPNU.***
- - - -

## Lab #1: ##
    Creating Python "Drug" class

### Rules:
    Створити консольну програму мовою Python і написати клас <Назва_із_завдання> який міститиме:
    1. Три додаткових поля, які найкраще описують даний клас	
    2. Конструктор (із вказаними дефолтними значеннями)
    3. Деструктор
    4. Метод, що повертає стрічкове представлення класу (__str__())
    5. Статичне поле
    6. Статичний метод, що повертає значення статичного поля
    7. В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі різної кількості
        параметрів) та виведіть інформацію про них з-за допомогою методу з пункту 4 в консоль
    8. Розроблений код має бути залито в гіт репозиторій як pull request! В репозиторії мать бути
        README і .gitignore файли.

#### Task:
    Ukr:
    Створити клас “Лікарський засіб (англійською - Drug)” котрий містить поля:
    - об'єм діючої речовини
    - (у міліграмах)
    - діюча речовина
    - максимальна кількість доз на день
    
    Eng:
    Create "Drug" class, which has these fields:
    - volume of operative substance
    - (in milligrams)
    - operative substance
    - maximum amount of doses per day
- - - -

## Lab #2: ##
    Creating UML classes diagram

### Rules:
    Лабораторне завдання складається з трьох частин:
    1. Намалювати UML діаграму класів
    2. ???
    3. ???

    Загальні рекомендації:
    1. Використовувати можливості ООП: класи, успадкування, поліморфізм, інкапсуляцію
    2. Кожний клас повинен мати назву, яка повністю описує його суть, і інформативний склад. Атрибути і методи
        класів слід визначити самостійно
    3. Успадкування потрібно використовувати тільки тоді, коли воно має сенс. У випадку використання
        наслідування кількість класів-нащадків має бути не меншою 2 і не більшою 4-ьох
    4. При записі програми потрібно використовувати домовленості щодо оформлення коду python code convention
    5. Зображати всі пари set/get (ака сеттери/геттери) для атрибутів класу не потрібно з метою уникнення
        засмічення діаграми
    6. Для реалізації операцій пошуку/сортування слід реалізувати окремий клас (в назві якого має бути присутнє
        слово Manager)
    7. UML діаграму класів можна малювати у draw.io, MS Visio або будь-якому іншому зручному інструментарії
    8. Результуючу діаграму слід залити на Google Drive  у форматі
        ClassDiagram_Programming_FirstName_LastName_GroupNumber.pdf

#### Task:
    Ukr:
    Магазин посуду.
    - Реалізувати ієрархію посуду, присутнього в магазині
    - Реалізувати пошук посуду, необхідного для організації святкування на 12 осіб
    - Вивести результат, відсортований за типом посуду
    - Реалізувати можливість сортування знайденого посуду за ще одним типом параметру (на вибір, реалізовано як
        окремий метод)
    - Реалізація сортування має передбачати можливість сортувати як за спаданням, так і за зростанням.

    Eng:
    Dishes shop.
    - Implement hierarchy of dishes presented in the store
    - Implement search of dishes needed for the organization of celebration for 12 guests
    - Display the result sorted by dishes type
    - Implement the ability to sort selected dishes by additional parameter type (optional, implemented as a
        separate method)
    - Implementation of sorting should provide the ability to sort both in descending or ascending order.
- - - -

## Lab #3: ##
    Creating Python data structure according to UML diagram from Lab2

### Rules: ###
    Лабораторне завдання складається з трьох частин:
    1. Намалювати UML діаграму класів
    2. Написати код до завдання з лабораторної №2
    3. ???

    Загальні рекомендації:
    1. Використовувати можливості ООП: класи, успадкування, поліморфізм, інкапсуляцію
    2. Кожний клас повинен мати назву, яка повністю описує його суть, і інформативний склад. Атрибути і методи
        класів слід визначити самостійно
    3. Успадкування потрібно використовувати тільки тоді, коли воно має сенс. У випадку використання
        наслідування кількість класів-нащадків має бути не меншою 2 і не більшою 4-ьох
    4. При записі програми потрібно використовувати домовленості щодо оформлення коду python code convention
    5. Зображати всі пари set/get (ака сеттери/геттери) для атрибутів класу не потрібно з метою уникнення
        засмічення діаграми
    6. Для реалізації операцій пошуку/сортування слід реалізувати окремий клас (в назві якого має бути присутнє
        слово Manager)
    7. UML діаграму класів можна малювати у draw.io, MS Visio або будь-якому іншому зручному інструментарії
    8. Результуючу діаграму слід залити на Google Drive  у форматі
        ClassDiagram_Programming_FirstName_LastName_GroupNumber.pdf

#### Task: ####
    Ukr:
    Написати код до завдання з лабораторної №2.
    - При записі програми потрібно використовувати домовленості щодо оформлення коду python code convention
    - Класи потрібно грамотно розкласти по пакетах
    - Робота з консоллю або консольне меню повинні бути мінімальними
    - В коді мають бути присутні лиш ті класи, які містяться на діаграмі класів
    - Атрибути класів та їх видимість мають співпадати із зазначеними на діаграмі класів. Те саме стосується
        методів класів
    - Для сортування слід використати вбудовані методи сортування, доступні в мові Python
    - Сортування слід реалізувати в окремому методі
    - Код немає містити статичних методів/атрибутів. Код має використовувати перелічувальний тип (Enum)
    - Код слід залити в окремий репозиторій, попередньо створивши pull request (тобто код слід писати в
        окремому branch на його основі зробити pull request)
    - Для перевірки роботи вашого коду слід створити окремий клас, в якому буде знаходитись main метод.

    Eng:
    Write the code according to the task from the lab 2.
    - Use the python code convention when writing a program
    - Classes should be properly groupped into packages
    - Interaction with the console or console menu should be minimal
    - The code should contain only classes  listed in the diagram
    - Class attributes, methods and their visibility must be identical with the class diagram
    - Use the built-in Python sorting methods
    - Sorting should be implemented in a separate method
    - The code should not contain static methods or attributes. It must use an enum type
    - The code should be in a separate repository, creating a pull request beforehand (the code should be in a
        separate branch with a pull request to master branch)
    - In order to test your code, create a separate class, where the main method will be located.
- - - -

## Lab #4: ##
    Creating Python tests to cover at least 70% of code from Lab3
[Lab3 link](https://github.com/dchelyuk/Python_Labs/tree/master/Lab3 "Lab3")

### Rules: ###
    Лабораторне завдання складається з трьох частин:
    1. Намалювати UML діаграму класів
    2. Написати код до завдання з лабораторної №2
    3. Написати модульні тести для коду лабораторної роботи №3 і досягти рівня покриття тестами 70%

    Загальні рекомендації:
    * В 4-ій лабораторній роботі слід написати модульні тести для коду лабораторної роботи №3 і досягти рівня
        покриття тестами 70%.
    * Очевидно, що ідеалом є покриття на рівні 100% (тобто кожна лінія коду покрита тестами).
    * Також очевидно, що написання тестів потребує значну кількість часу, якого завжди бракує.
    * Одним з варіантів униклення цієї проблеми є підхід TDD.
    * Для даної лабораторної компромісним значенням буде покриття тестами на рівні 70%

#### Task: ####
    Ukr:
    Написати модульні тести для коду лабораторної роботи №3.
    - тести, виконані в 4-й роботі мають бути додані до коду 3-ї роботи
    - Покриття коду тестами має становити 70%
    - Коміт в Github має  бути виконано як окремий pull request (але не потрібно виконувати merge)
    - Код слід перевірити на відповідність вимогам РЕР8 та виправити знайдені зауваження

    Eng:
    Write module testsfor the code of Lab №3.
    - Tests should be added to the code of Lab №3
    - Code coverage with tests should be at least 70%
    - GitHub commit should be done as a separate pull request (but no need to do merge)
    - Code should be checked according PEP8 requirements and corrected in case of mistakes
- - - -

## Lab #5: ##
    Дана лабораторна робота передбачає написання коду, котрий виконує завдання з таблиці на мові Python з
    використанням регулярних виразів

### Rules: ###
    1. Do not use string matching
    2. Read about RE
    3. Read about HTTP codes
    4. Read about User Agent

#### Task: ####
    Ukr:
    Вивести всі успішні GET запити та порахувати їх кількість звернень що повертали файл style.css
    з файлу http://igm.univ-mlv.fr/~cherrier/download/L1/access.log
    Які були виконані в проміжку:
    22/Mar/2009:07:40:06
    30/Mar/2009:13:43:28
    
    Eng:
    Print all succesful GET requests which return file style.css and count them.
    (from file http://igm.univ-mlv.fr/~cherrier/download/L1/access.log)
    Time range:
    22/Mar/2009:07:40:06
    30/Mar/2009:13:43:28

[acess.log](http://igm.univ-mlv.fr/~cherrier/download/L1/access.log)
