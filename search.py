import re
import requests


def validate_snils(snils):
    pattern = r'^\d{3}-\d{3}-\d{3}\ \d{2}$'
    return bool(re.match(pattern, snils))

def find_snils_in_text(text):
    pattern = r'\b\d{3}-\d{3}-\d{3}\ \d{2}\b'
    return re.findall(pattern, text)

def find_snils_from_url(url):



def find_snils_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return find_snils_in_text(file.read())
    except IOError as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []

# Пример использования
if __name__ == "__main__":
    snils = input("Введите СНИЛС: ")
    if validate_snils(snils):
        print("Введенный СНИЛС корректен")
    else:
        print("Введенный СНИЛС некорректен")

    url = input("Введите URL для поиска СНИЛС: ")
    found_snils = find_snils_from_url(url)
    print(f"Найденные СНИЛС на странице: {found_snils}")

    file_path = input("Введите путь к файлу для поиска СНИЛС: ")
    found_snils = find_snils_in_file(file_path)
    print(f"Найденные СНИЛС в файле: {found_snils}")





