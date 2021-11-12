from bs4 import BeautifulSoup
import requests
import os
import django
import logging

logging.basicConfig(level=logging.DEBUG)

# Устанавливаем настройки Django для работы с моделью
os.environ.setdefault("PYTHONPATH", "currency")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency.settings")
django.setup()

from get_currency.models import Currency


def parse_rate():
    """ Парсит данные с сайта cbr.ru """
    try:
        resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        logging.info('Отправили GET запрос')
    except requests.ConnectionError:
        logging.error('Не удалось подключиться к сайту')
    soup = BeautifulSoup(resp.text, 'lxml')
    logging.info('Загрузили html в bs4')
    currency_dict = []
    for key in soup.find_all('valute'):
        name = key.find('name').text
        rate = key.find('value').text.replace(',', '.')
        currency_dict.append((name, rate))
        logging.info(f'Получили {name}')
    return currency_dict


def main():
    """ Основноая функция парсинга """
    currency_dict = parse_rate()
    logging.info('Парсинг окончен, переходим к работе с БД')
    for currency in currency_dict:
        Currency.objects.update_or_create(name=currency[0], defaults={'name': currency[0], 'rate': currency[1]})
    logging.info('Обновление данных завершено')


if __name__ == '__main__':
    logging.info('Начинаем парсинг данных о валюте')
    main()