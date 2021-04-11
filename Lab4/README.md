# Python_Labs #
***This repo is for storing python labs from LPNU.***

## Lab #4: ##
    Creating Python tests to cover at least 70% of code from Lab3
[Lab3 link](https://github.com/dchelyuk/Python_Labs/tree/master/Lab3 "Named link title")

### Rules: ###
    Лабораторне завдання складається з трьох частин, першою частиною є намалювати UML діаграму класів

    Загальні рекомендації:
    1. Використовувати можливості ООП: класи, успадкування, поліморфізм, інкапсуляцію
    2. Кожний клас повинен мати назву, яка повністю описує його суть, і інформативний склад. Атрибути і методи
        класів слід визначити самостійно
    3. Успадкування потрібно використовувати тільки тоді, коли воно має сенс. У випадку використання наслідування
        кількість класів-нащадків має бути не меншою 2 і не більшою 4-ьох
    4. При записі програми потрібно використовувати домовленості щодо оформлення коду python code convention
    5. Зображати всі пари set/get (ака сеттери/геттери) для атрибутів класу не потрібно з метою уникнення засмічення
        діаграми
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
    - Атрибути класів та їх видимість мають співпадати із зазначеними на діаграмі класів. Те саме стосується методів
        класів
    - Для сортування слід використати вбудовані методи сортування, доступні в мові Python
    - Сортування слід реалізувати в окремому методі
    - Код немає містити статичних методів/атрибутів. Код має використовувати перелічувальний тип (Enum)
    - Код слід залити в окремий репозиторій, попередньо створивши pull request (тобто код слід писати в окремому branch
        на його основі зробити pull request)
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
    - The code should be in a separate repository, creating a pull request beforehand (the code should be in a separate
        branch with a pull request to master branch)
    - In order to test your code, create a separate class, where the main method will be located.