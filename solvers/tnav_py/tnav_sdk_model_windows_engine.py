import tNavigator_python_API as tNav
from pathlib import Path
from const import (
    TNAV_EXE,
    CASE_PATH
)

def require_file(p: Path, desc: str):
    if not p.exists():
        raise FileNotFoundError(f"{desc} не найден: {p}")

def main():
    require_file(TNAV_EXE, "Бинарь tNavigator-con")
    require_file(CASE_PATH, "Файл модели/проекта")

    conn = tNav.Connection(str(TNAV_EXE))
    proj = conn.open_project(str(CASE_PATH), project_type=tNav.ProjectType.MD)

    # интроспекцию среды внутреннего Python в tNavigator
    introspect_code = r"""
import sys, builtins

print("PY:", sys.version)
# check global names from tnav env
names = sorted([k for k in globals().keys() if not k.startswith("_")])
print("GLOBALS:", names)

# print dirs
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