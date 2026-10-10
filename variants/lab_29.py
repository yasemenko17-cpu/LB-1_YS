"""Службовий файл варіанта 29. Не змінюйте його: ви редагуєте файли в папці lab_29/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lab_29"
FILES = ['keys.sh', 'sshd_hardening.conf', 'ufw.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (варіанта 29) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
