import inspect
import importlib

PKG = "tNavigator_python_API"

pkg = importlib.import_module(PKG)
Conn = getattr(pkg, "Connection")
Proj = getattr(pkg, "Project")

def dump_class(cls):
    print(f"\n=== CLASS {cls.__module__}.{cls.__name__} ===")
    methods = []
    for name, obj in inspect.getmembers(cls):
        if name.startswith("_"):
            continue
        if inspect.isfunction(obj) or inspect.ismethoddescriptor(obj):
            try:
                sig = str(inspect.signature(obj))
            except Exception:
                sig = "(...)"
            doc = (inspect.getdoc(obj) or "").strip().splitlines()[:1]
            methods.append((name, sig, "  # " + doc[0] if doc else ""))
    if methods:
        print("Methods:")
        for n, s, d in methods:
            print(f" - {n}{s}{d}")
    else:
        print("No public methods found.")

dump_class(Conn)
dump_class(Proj)

print("\n=== RUNTIME OBJECTS (best-effort) ===")
try:
    c = Conn()
    print("Connection instance created.")
    attrs = [a for a in dir(c) if not a.startswith("_")]
    print("Connection attrs:", attrs)
    simple = {}
    for a in attrs:
        try:
            v = getattr(c, a)
            if isinstance(v, (int, float, str, bool, type(None))):
                simple[a] = v
        except Exception:
            pass
    if simple:
        print("Connection simple fields:", simple)
except Exception as e:
    print("Connection() failed to instantiate:", e)

try:
    p = Proj()
    print("Project instance created.")
    attrs = [a for a in dir(p) if not a.startswith("_")]
    print("Project attrs:", attrs)
    simple = {}
    for a in attrs:
        try:
            v = getattr(p, a)
            if isinstance(v, (int, float, str, bool, type(None))):
                simple[a] = v
        except Exception:
            pass
    if simple:
        print("Project simple fields:", simple)
except Exception as e:
    print("Project() failed to instantiate:", e)