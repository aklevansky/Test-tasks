Необходимо создать небольшое веб приложение, используя любой веб фреймворк (желательно тот, который Вы лучше всего знаете). Верстка не важна, уделяйте основное внимание бэкенду, оформлению кода, мелочам.

Фактически приложение должно состоять из одной страницы, но по желанию можно разделить на несколько (отдельно форму загрузки).
Необходимые элементы — форма загрузки фотографии и таблица со списком загруженных фото. Авторизация не обязательна.

Форма загрузки:
Текстовое поле для ввода названия фото
Выбор файла

Таблица:
Превью фото (необходимо сделать уменьшенную копию фото (миниатюру); также данное превью должно являться ссылкой на оригинальное/полное изображение, которое открывается по клику на превью)
Название фото (которое пользователь указывает при загрузке)
Производитель и модель камеры (из EXIF, если присутствует)
Размер файла
Дата создания фото (из EXIF)
Дата загрузки фото
Кнопка удаления

Требования:
Не сохранять уже существующие фото. Проверять наличие дубликата файла и выдавать ошибку в случае обнаружения.
Проверять, является ли загружаемый файл изображением, если нет — выдавать ошибку. (Не использовать проверку наличия EXIF данных в качестве валидации)
Не позволять сохранять фото, созданные более года назад (проверять дату создания фото из EXIF).
Если отсутствует дата создания фото в EXIF, тогда следует выдать ошибку и не добавлять файл.