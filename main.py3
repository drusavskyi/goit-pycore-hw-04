import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows
init(autoreset=True)

def walk_directory(directory: Path, prefix=""):
    entries = sorted(directory.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
    for index, entry in enumerate(entries):
        connector = "┗━ " if index == len(entries) - 1 else "┣━ "
        if entry.is_dir():
            print(prefix + connector + Fore.CYAN + Style.BRIGHT + entry.name)
            new_prefix = prefix + ("   " if index == len(entries) - 1 else "┃  ")
            walk_directory(entry, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + entry.name)

def main():
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        return

    path = Path(sys.argv[1])
    if not path.exists():
        print(Fore.RED + f"Помилка: шлях '{path}' не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Помилка: шлях '{path}' не є директорією.")
        return

    print(Fore.YELLOW + Style.BRIGHT + str(path.resolve()))
    walk_directory(path)

if __name__ == "__main__":
    main()