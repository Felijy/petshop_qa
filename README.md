В качестве тестового задания сделаны тесты на 4 различных метода, все они связаны с моделью пользователя.
К сожалению, без полноценной документации многие asserts сделаны по личному восприятию того, как это должно 
выглядеть в идеале, поэтому периодически они не совпадают с реакцией сервера. Несколько слов про стуктуру проекта:

Проект поделен на 2 логические группы: 
- Непосредственно тесты `tests`
- Абстрактные сущности `modules`

В абстрактных сущностях на данном этапе хранится только класс для клиента API, он работает с `requests`, предоставляя
простую возможность изменить ключевые моменты сразу для всего проекта

В тестах лежит более подробный `README.md` файл, описывающий структуру этого раздела

Кроме того, в корне есть файл `report.html`, в нем лежит отчет по всем проведенным тестам в html для 
большей визуальной наглядности.

P.S. В некоторых тестах также есть комментарии по поводу кодов ответа, потому что не всегда было понятно, с чем
нужно сравнивать то, что возвращает сервер. 

Спасибо за уделенное время :)

Запуск:

После клона директории необходимо установить зависимости:\
`pip install pytest requests pytest-html`\
Далее запустить все тесты: `pytest` из корня