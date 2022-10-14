# Техническое задание 2 <hr>

### Входные данные:
На вход программы поступает файл, который состоит из чисел ........ (Описать входные данные)


### Функционал программы:
1. `_min` - какое-то описание функции _min
2. `_mult` - какое-то описание функции _mult
3. и тд 

Пример кнопок отображения результатов для ветки main:
`![](https://github.com/ваш_никнейм/название_репозитория/actions/workflows/название_файла_ворклоф.yml/badge.svg?branch=название_ветки)`</br>
![](https://github.com/Ilyshkadwaushka/hse_tp_hw_cons/actions/workflows/ci.yml/badge.svg?branch=master)
<br/>
<br/>
### Сюда добавить картинку графика:<br/>
![](https://storage.theoryandpractice.ru/tnp/uploads/image_block/000/043/965/image/base_f99e2b8fc5.jpg)



## Информация из консультации
[Cсылка на запись консультации](https://youtu.be/GKMvz0sZBLY)

#### Команды для работы с гит:
* `git init` - инициализация гита
* `git add .` или `git add название.формат` - добавить файл в новый комимит 
* `git commit -m "Git init"` - создать коммит(обновление)
* `git branch -M main` - создать ветку main и сделать ее основной
* `git checkout develop` - переключиться на ветку develop
* `git checkout -b develop` - создаем ветку develop и переключаемся на нее 
* `git push origin main` - публикация коммита на github
* `pip freeze >> requiremenets.txt` - создание файла зависимостей (если есть сторонние библиотеки)


##### Пример yml файла для Github Actions Workflows:
```
name: ci

on:
  push:
    branches: [ "master"]
  pull_request:
    branches: [ "master"]

  workflow_dispatch:

jobs:
  test:
    name: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: requirements install
        run: |
          cd $GITHUB_WORKSPACE
          pip install -r requirements.txt
      - name: Run tests 
        run: python3 -m unittest test
```
