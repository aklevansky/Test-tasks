# Привет!

Тестовое задание для Wargaming Forge состоит из двух задач. Первая — алгоритмическая, а вторая — о машинном обучении. Ты можешь решить только одну из них, но лучше сделать обе. Это повысит твой шанс попасть в Wargaming Forge.

## Задача 1. Алгоритмы и неравные матчи!

Данные для задачи находятся в папке task_1_data. Нужно написать программу, которая составит матчи между командами игроков. Программа должна учитывать рейтинги игроков, чтобы составленное распределение было сбалансированным.

Сбалансированное распределение — набор матчей, в которых разница между рейтингом играющих команд будет минимальна.

Рейтинг команды — сумма рейтингов игроков, состоящих в команде.

**Входные данные**

|Рейтинги игроков|Команды|
|---|---|
|task_1_data/{test_name}/players.txt|task_1_data/{test_name}/teams.txt|

В папке task_1_data ты найдешь папки с юнит-тестами (test_A, test_b и т. д.). Каждая из папок содержит 2 файла:
- Текстовый файл players.txt содержит записи об игроках и их рейтингах. Один игрок в строке, без заголовка, в формате "<user_id> <rating>".
- Текстовый файл teams.txt содержит строки-записи о командах и список игроков каждой команды. Без заголовка, в формате "<team_id> <user_id> <user_id>... <user_id>".

**Выходные данные**

|Рейтинги игроков|Команды|
|---|---|
|Сбалансированные пары команды|Username_task_1_team_pairs/{test_name}_pairs.txt|
|Исходный код программы|Username_task_1_src/*|

Вместо каждого {test_name}, подставь названия тестов (название папок, в которых лежат тесты). Каждый выходной файл {test_name}_pairs.txt должен иметь формат
"<team_id> <team_id>". Если команд нечетное количество, то без пары должна остаться только одна команда.

## [**Решение**](https://github.com/mxmaslin/Test-tasks/blob/master/tests_python/Wargaming%20Forge%20Task/Username_task_1_src.py "Решение алгоритмического задания конкурса Wargaming Forge")
