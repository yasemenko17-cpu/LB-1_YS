"""Службовий файл варіанта 17. Не змінюйте його: ви редагуєте файли в папці lab_17/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lab_17"
FILES = ['keys.sh', 'sshd_hardening.conf', 'ufw.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (варіанта 17) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
