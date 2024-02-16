import re
import sys

def parse_log_line(line: str) -> dict:      #парсинг рядка логу: приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення
    log_dict = {}
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) ([A-Z]+) (.*)$'
    pars = re.match(pattern, line)
    log_dict["date"] = pars.group(1)
    log_dict["time"] = pars.group(2)
    log_dict["level"] = pars.group(3)
    log_dict["message"] = pars.group(4)
    return log_dict

def load_logs(file_path: str) -> list:      #завантаження лог-файлів: відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список
    log_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    log_list.append(log)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено!")
    return log_list
    
def filter_logs_by_level(logs: list, level: str) -> list:           #дозволить отримати всі записи логу для певного рівня логування
    level_log = []
    print(f"\nДеталі логів для рівня {level} :")
    for log in logs:
        if log["level"] == level:
            level_log.append(log)
            print(f"{log["date"]} {log["time"]} - {log["message"]}")
    return level_log

def count_logs_by_level(logs: list) -> dict:                        #Підрахунок записів за рівнем логування: проходить по всім записам і підраховує кількість записів для кожного рівня логування
    log_counts = {}
    for log in logs:
        log_counts[log["level"]] = log_counts.get(log["level"], 0) + 1
    return log_counts

def display_log_counts(counts: dict):                               #Вивід результатів: форматує та виводить результати підрахунку в читабельній формі
    print("\nРівень логування    | Кількість")
    print("-"*31)
    for level, count in counts.items():
        print(f"{level:16}| {count}")

def main():
    if len(sys.argv) == 3:
        logs = load_logs(sys.argv[1])
        level = sys.argv[2].upper()
        if logs:
            display_log_counts(count_logs_by_level(logs))
            filter_logs_by_level(logs, level)
        else:
            print("Логи не знайдено")
    elif len(sys.argv) == 2:
        logs = load_logs(sys.argv[1])
        if logs:
            display_log_counts(count_logs_by_level(logs))
        else:
            print("Логи не знайдено")
    else:
        print("Usage: python script.py <log_file> [<log_level>]")


if __name__ == "__main__":
    main()
