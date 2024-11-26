import csv


def read_csv(filename):
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдений.")
    except Exception as e:
        print(f"Сталася помилка при відкритті файлу: {e}")
    return data


def print_csv(data):
    if data:
        for row in data:
            print(row)
    else:
        print("Немає даних для виведення.")


def search_country(data, country_name):
    result = [row for row in data if row['Country'] == country_name]
    return result


def write_csv(data, filename):
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Country', 'GDP', 'Life expectancy at birth, total (years)']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Результати записано в файл {filename}")
    except Exception as e:
        print(f"Помилка при записі в файл: {e}")


def main():
    input_filename = 'gdp_life_expectancy_2019.csv'
    data = read_csv(input_filename)

    if not data:
        return

    print("Вміст CSV файлу:")
    print_csv(data)

    country_name = input("Введіть назву країни для пошуку: ").strip()
    search_result = search_country(data, country_name)

    if search_result:
        print(f"Результати для {country_name}:")
        print_csv(search_result)

        output_filename = f"{country_name}_2019_results.csv"
        write_csv(search_result, output_filename)
    else:
        print(f"Дані для країни '{country_name}' не знайдені.")


if __name__ == "__main__":
    main()