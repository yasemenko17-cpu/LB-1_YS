"""Службовий файл варіанта 11. Не змінюйте його: ви редагуєте файли в папці lab_11/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lab_11"
FILES = ['keys.sh', 'sshd_hardening.conf', 'ufw.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (варіанта 11) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
