import importlib, inspect, pkgutil

PKG_NAME = "tNavigator_python_API"
pkg = importlib.import_module(PKG_NAME)

def walk(mod):
    for name, obj in inspect.getmembers(mod):
        if inspect.ismodule(obj) and obj.__name__.startswith(PKG_NAME):
            yield obj
            yield from walk(obj)

mods = {pkg, *walk(pkg)}

candidates = []
for m in mods:
    for name, obj in inspect.getmembers(m):
        if inspect.isclass(obj) or inspect.isfunction(obj):
            lname = name.lower()
            if any(k in lname for k in ["client","connect","session","api",
                                        "model","project","open","case","run","step","timestep"]):
                try:
                    sig = str(inspect.signature(obj))
                except Exception:
                    sig = "(...)"
                candidates.append((m.__name__, name, sig))

print("Possible entrypoints:")
for modname, name, sig in sorted(set(candidates)):
    print(f" - {modname}.{name}{sig}")