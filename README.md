# Smart city

## Bot vk


Настройка директории и установка зависимостей (windows)

```console  
$ python -m venv env

$ env/scripts/activate

$ New-Item -ItemType file -Path './resources/config.py'

$ pip install requirements.txt
```

Содержимое config.py
```python
token = ''
group_id = id

```