import importlib, inspect

PKG_NAME = "tNavigator_python_API"

pkg = importlib.import_module(PKG_NAME)
print("Package:", pkg, getattr(pkg, "__file__", None))

public = [a for a in dir(pkg) if not a.startswith("_")]
print("Top-level attrs:", public)

for name in public:
    try:
        obj = getattr(pkg, name)
        if inspect.ismodule(obj):
            print(f"\n[{PKG_NAME}.{name}] module attrs:", [a for a in dir(obj) if not a.startswith("_")])
    except Exception as e:
        print(f"Skip {name}:", e)