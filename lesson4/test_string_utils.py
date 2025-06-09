import pytest
from string_utils import StringUtils

# Заглавная буква в начале
'''Тесты:
1)Слово с маленькой буквы начинается
2)Слово с большой буквы начинается
3)цифры
4)знаки препинания
'''


@pytest.mark.parametrize('word, result', [
  ('skypro', 'Skypro'),
  ('Skypro', 'Skypro'),
  ('123', '123'),
  ("!!!", "!!!"),
  ('скайпро', 'Скайпро'),
  ('skypro skypro', 'Skypro skypro')
  ])
def test_capitalize_positive(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result


@pytest.mark.parametrize('word, result', [
  ('123abc', '123abc'),
  ('!skypro', '!skypro'),
  ('Skypro', 'Skypro'),
  ])
def test_capitalize_negativ(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result


# Удаление пробела в начале строки
'''Тесты:
1)Один пробел в начале строки
2)Три пробела в начале строки
3)Только пробелы
'''


@pytest.mark.parametrize('word, result', [
  (' скайпро', 'скайпро'),
  ('    скайпро', 'скайпро'),
  ('     ', '')
  ])
def test_trim_positive(word, result):
    string_utils = StringUtils()
    res = string_utils.trim(word)
    assert res == result


'''
Тесты:
1)Строка без пробелов в начале должна остаться без изменений
2)Строка с пробелами в конце не должна измениться
'''


@pytest.mark.parametrize('word, result', [
  ('skypro', 'skypro'),
  ('skypro   ', 'skypro   ')
  ])
def test_trim_negative(word, result):
    string_utils = StringUtils()
    res = string_utils.trim(word)
    assert res == result


# Буква в строке
# Удаление пробела в начале строки
'''Тесты позитивные:
1)В строке есть буква - True
2)строка с нижнем регистром, буква с верхним и содержится в слове - True
'''


@pytest.mark.parametrize('string, symbol', [
  ('скайпро', 'с'),
  ('скайпро', 'С')
  ])
def test_contains_positive(string, symbol):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res is True


'''Тесты негативные:
1)Строка пустая, буква есть - False
2)Строка из цифр, буква есть - False
3)В строке нет буквы - False
'''


@pytest.mark.parametrize('string, symbol', [
  ('      ', 'с'),
  ('123654', 'С'),
  ('скайпро', 'в')
  ])
def test_contains_negative(string, symbol):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res is False


# Удаление подстроки из строки
'''Тесты позитивные:
1)Из строки удаляется одна буква
2)Из строки удаляется несколько букв
'''


@pytest.mark.parametrize('string, symbol, expected', [
    ('скайпро', 'к', 'сайпро'),
    ('скайпро', 'про', 'скай')
    ])
def test_delete_symbol_positive(string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == expected


'''Тесты негативные:
1)Из строки не удаляется буква, потому что ее нет в ней
2)Из строки не удаляется буква, потому что ввели цифры
'''


@pytest.mark.parametrize('string, symbol, expected', [
  ('скайпро', 'м', 'скайпро'),
  ('скайпро', '1', 'скайпро')
  ])
def test_delete_symbol_negative(string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == expected
