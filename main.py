from datetime import datetime
import requests


def log(func):
    def ooks(*arguments, **kwarguments):
        datatime = datetime.now()
        functionname = func.__name__
        result = func(*arguments, **kwarguments)
        with open('decoratorlogs.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {datatime}\n'
                       f'Имя функции: {functionname}\n'
                       f'Аргументы: {arguments, kwarguments}\n'
                       f'Результат: {result}\n')
        return result
    return ooks


@log
def status(*arguments, **kwarguments):
    url = ','.join(argumentss)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    status('https://github.com/')

FILE_PATH = ''


def log(path):
    def decorator(func):
        def ooks(*args, **kwargs):
            datatime = datetime.now()
            functionname = func.__name__
            result = func(*arguments, **kwarguments)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {datatime}\n'
                           f'Имя функции: {functionname}\n'
                           f'Аргументы: {arguments, kwarguments}\n'
                           f'Результат: {result}\n')
            return result
        return ooks
    return decorator


@log(FILE_PATH)
def status(*arguments, **kwarguments):
    url = ','.join(arguments)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    status('https://github.com/')
    