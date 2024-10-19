# fuzzy-logic

## Описание проекта
Проект посвящен анализу уровня тревожных расстройств у студентов выпускного курса с использованием нечеткой логики. В работе рассматриваются три базовых модели:

- Поведенческие симптомы
- Физические симптомы
- Когнитивные симптомы
Каждая из этих моделей описывает свой аспект тревожности и объединяется в единую модель, позволяя получить интегральное значение для общей тревожности студентов.

## Техническая реализация
Проект реализован в среде Matlab R2019b, с использованием файлов .fis для описания нечетких моделей пакета fuzzy. Эти модели могут быть легко преобразованы в формат, совместимый с Scilab, однако запуск в Scilab может быть затруднен из-за общих проблем Scilab'а.

## Особенности моделей
- Входные параметры: В каждой модели определены более значимые и менее значимые входные параметры, которые отражают различные проявления тревожности.
- Термы: Для каждого входного параметра в базовых моделях задано по 3 терма (например, низкий, средний, высокий), определяющих степень выраженности в диапазоне 0-100. В результатной модели у одного входного параметра 4 терма, у оставшихся двух - 5 термов. Диапазон 20-90.
- Правила: Логические правила, определяющие взаимосвязь между входными параметрами и уровнем тревожности, описаны формульно в файле инд.ods. В зависимости от количества термов у выходной переменной, для каждой модели предусмотрено 81 или 243 правила.
- Функции принадлежности:
** Для входных значений чаще всего используются 3 функции принадлежности типа gaussmf (гауссовские функции) или комбинация zmf + gaussmf + smf.
** Для выходных значений применяются 4 или 5 треугольных функций принадлежности (trimf).

## Примеры
<img width="800px" src="https://github.com/wybin4/fuzzy-logic/blob/main/surface_example.png"/><img width="800px" src="https://github.com/wybin4/fuzzy-logic/blob/main/terms_example.png"/>

## Запуск Matlab на Linux `/usr/local/Polyspace/R2019b/bin/matlab`
