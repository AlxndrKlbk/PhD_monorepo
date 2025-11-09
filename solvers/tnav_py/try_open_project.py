# tnav_probe_subprojects.py
import time
from tNavigator_python_API import Connection
from const import (
    CASE_PATH,
    TNAV_EXE
)

def wait_runs(proj, timeout_sec=60, note="root"):
    code = 'print("probe:", 1+1)'
    start = time.time()
    last = ""
    while time.time() - start < timeout_sec:
        out = proj.run_py_code(code)
        last = out or ""
        if "probe:" in last:
            return True, last
        time.sleep(0.5)
    return False, last

def main():
    if not TNAV_EXE.exists():
        raise FileNotFoundError(f"tNavigator.exe not found: {TNAV_EXE}")
    if not CASE_PATH.exists():
        raise FileNotFoundError(f"model not found: {CASE_PATH}")

    con = Connection(str(TNAV_EXE))
    proj = con.open_project(str(CASE_PATH), project_type="md")

    print("\n== Subproject list from SDK tnav ==")
    try:
        lst = proj.get_list_of_subprojects(type="nd")
        print(lst)
    except Exception as e:
        print(f"get_list_of_subprojects() упал: {e}")
        lst = None

    print("\n== Test code in Project ==")
    ok_root, out_root = wait_runs(proj, timeout_sec=30, note="root")
    print("OK?", ok_root)
    print("OUT:\n", out_root)

    if not ok_root:
        print("\nNo result from 'run_py_code'. Tru subproject...")
        candidates = ["model", "case", "project", "main", "nd", "md"]
        tried = set()
        for name in candidates:
            if name in tried:
                continue
            tried.add(name)
            try:
                sub = proj.get_subproject_by_name(name, type="nd")
            except Exception:
                continue
            print(f"\n== test execute code '{name}' ==")
            ok_sub, out_sub = wait_runs(sub, timeout_sec=30, note=name)
            print("OK?", ok_sub)
            print("OUT:\n", out_sub)
            if ok_sub:
                out = sub.run_py_code('import sys; print("PY:", sys.version); print("GLOBALS:", '
                                      'sorted([k for k in globals() if not k.startswith("_")])[:200])')
                print("\nINTROSPECTION:\n", out)
                break

        else:
            print("\nnot found subproject GUI.")
    try:
        proj.close_project()
    except Exception as e:
        print("close_project() error:", e)

if __name__ == "__main__":
    main()