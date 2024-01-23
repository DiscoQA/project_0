Тестируем playgames.ru
на примере бизнес-процесса:
Авторизация, переход в каталог, установка фильтров и выбор игры elden ring версии для ps5

setup:
1. Клонируйте репозиторий

git clone https://github.com/DiscoQA/project_0.git

2. Переименуйте .env_example в .env. Введите в .env логин и пароль
3. В терминале:

pip install pytest

pip install selenium

pip install environs

Запуск теста, тк тест всего один - в терминале:

python -m pytest -s -v


ps тестирования считается успешным после заполнения полей на странице заказа (подтверждения заказа не предусмотрено)
