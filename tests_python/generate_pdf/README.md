**Дано**: пример макета документа в виде изображения (прилагается к письму), CSV с меняющимися от документа к документу данными
(пример сделать самому по данным, присутствующим в макете).
В csv первая строка должна содержать заголовок с названиями полей, на которые можно по этим названиям ссылаться в шаблоне.

**Задача**: Используя любую удобную библиотеку для обработки шаблонов и любой удобный метод получения PDF, нарисовать шаблон документа, соответствующий
приложенному макету и подставить в него данные из CSV, получая пачку документов соответствующих таблице
(в результате для каждой строки в csv на выходе должна получиться одна страница документа.
Оформить просто как консольную утилиту (никаких django тут не нужно: чистый питон).

1. Предлагается оформить решение в виде законченной консольной утилиты с параметрами
(но без фанатизма: это все-таки тестовое задание, поэтому делать, как будто "завтра в прод" не нужно).
2. Некоторое поле из csv должно выводиться в виде QR кода.
3. Дополнение специально для Вас)): предусмотреть в утилите параметр командной строки, который позволяет сдвигать макет выше ниже на странице,
чтобы решать ту задачу с разными дипломами, что мы с Вами обсуждали.
4. Желательно при разработке утилиты использовать virtualenv
5. Результат нужно оформить в виде репозитория на github.com
6. Также в репку положить тот тестовый csv файл, на котором можно утилиту проверить.


**Решение**:

1. Установить пакеты из requirements.txt

    `pip install -r requirements.txt`
    
2. Опционально: сгенерировать тестовые данные (уже сгенерированы, лежат в persons.csv)

    `python generate_persons <количество персон>`
    
3. Запустить скрипт [generate_pdfs.py](https://github.com/mxmaslin/Test-tasks/blob/master/tests_python/generate_pdf/generate_pdfs.py)

    `python generate_pdfs.py`
    
    Скрипт попросит указать файл к csv-файлу с данными получателей дипломов
    
[Примеры сгенерированных дипломов](https://github.com/mxmaslin/Test-tasks/tree/master/tests_python/generate_pdf/diplomas) 
    
![Что должно напечататься](https://github.com/mxmaslin/Test-tasks/blob/master/tests_python/generate_pdf/diplomas/diplom1.pdf)