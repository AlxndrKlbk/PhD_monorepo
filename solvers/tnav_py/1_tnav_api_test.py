# file: probe_1_where_and_top_level.py
import importlib.metadata as md
import pkgutil, sys, pprint, os

dist = md.distribution("tNavigator_python_API")
print("Dist:", dist.metadata["Name"], dist.version)
print("Files sample:", list(dist.files)[:10])

top_levels = [p for p in dist.files or [] if p.parts and len(p.parts)==1 and p.suffix==""]
print("Top-level candidates:", [str(p) for p in top_levels])

locs = [os.path.dirname(f.locate()) for f in dist.files if f.name.endswith("__init__.py")]
print("Possible locations:", locs[:3])

for p in set(locs):
    if p and p not in sys.path:
        sys.path.append(p)

try:
    top_level = dist.read_text("top_level.txt")
    print("top_level.txt:\n", top_level)
except Exception:
    pass