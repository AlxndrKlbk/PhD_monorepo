# Минимальный рабочий пример для tNavigator_python_API 1.0.0 (23.4)
from __future__ import annotations
import os
from pathlib import Path
from tNavigator_python_API import Connection

TNAV_EXE = Path(r"D:\tNavigator\install\23.4\tNavigator.exe")
CASE_PATH = Path(r"D:\usr\repo\PhD_monorepo\solvers\tnav_py\INIT_Thermal\INIT_Thermal.data")

def require_file(p: Path, desc: str):
    if not p.exists():
        raise FileNotFoundError(f"{desc} не найден: {p}")

def main():
    require_file(TNAV_EXE, "Бинарь tNavigator.exe")
    require_file(CASE_PATH, "Файл модели/проекта")

    con = Connection(str(TNAV_EXE))
    proj = con.open_project(str(CASE_PATH), project_type="md")

    # интроспекцию среды внутреннего Python в tNavigator
    introspect_code = r"""
import sys, builtins

print("PY:", sys.version)
# Посмотрим, какие глобальные имена видны из окружения tNavigator:
names = sorted([k for k in globals().keys() if not k.startswith("_")])
print("GLOBALS:", names)

# Аккуратно попробуем вывести dir() по некоторым кандидатам, если они есть:
candidates = ["model", "grid", "project", "case", "sim", "session", "api"]
for name in candidates:
    if name in globals():
        try:
            obj = globals()[name]
            print(f"== {name} ==")
            print(sorted([a for a in dir(obj) if not a.startswith('_')])[:200])
        except Exception as e:
            print(f"!! dir({name}) failed:", e)

# Если предусмотрен какой-то help()/about(), это тоже покажет зацепки:
try:
    if 'help' in dir(builtins):
        print('HELP_AVAILABLE')
except Exception:
    pass
"""
    out = proj.run_py_code(introspect_code)
    print("=== INTROSPECTION OUTPUT BEGIN ===")
    print(out)
    print("=== INTROSPECTION OUTPUT END ===")

    # close
    proj.close_project()

if __name__ == "__main__":
    main()