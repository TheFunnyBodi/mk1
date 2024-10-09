import os
import json
from module import compare_speeds, translate_text 

def read_data():
    # Функція для зчитування даних з файлу.
    file_name = "MyData.json"
    
    if not os.path.exists(file_name):
        return None

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return None

def write_data(v1, v2, lang_code):
    # Функція для запису даних у файл.
    data = {
        "v1_kmh": v1,
        "v2_ms": v2,
        "lang": lang_code
    }
    with open("MyData.json", 'w') as file:
        json.dump(data, file)

def main():
    data = read_data()
    
    if data is None:  # Якщо файл не знайдений або некоректний
        v1 = float(input("Введіть швидкість v1 (км/год): "))
        v2 = float(input("Введіть швидкість v2 (м/с): "))
        lang_code = input("Введіть мову інтерфейсу (uk/en): ").lower()
        
        write_data(v1, v2, lang_code)
        print("Дані збережено в файл MyData.json")
        return
    
    # Якщо файл успішно зчитано
    v1 = data["v1_kmh"]
    v2 = data["v2_ms"]
    lang_code = data.get("lang", "uk").lower()

    # Функція для порівняння швидкостей
    result = compare_speeds(v1, v2)

    # Результат відповідно до вибраної мови
    print(f"Мова: {translate_text('language', lang_code)}")
    print(f"{translate_text('speed_v1', lang_code)} ({v1} км/год) = {round(result['v1_ms'], 1)} м/с")
    print(f"{translate_text('speed_v2', lang_code)} ({v2} м/с) = {round(result['v2_kmh'], 1)} км/год")
    print(result["comparison"])

if __name__ == "__main__":
    main()
