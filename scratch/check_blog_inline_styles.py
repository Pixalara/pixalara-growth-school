import os
import re

workspace_dir = "d:\\Pixalara Growth School\\growth school repo"
files = [f for f in os.listdir(workspace_dir) if f.startswith("blog") and f.endswith(".html")]

print(f"Found {len(files)} blog-related files.")

pattern = re.compile(r'style\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)

for filename in files:
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    if matches:
        print(f"\n--- {filename} ({len(matches)} inline styles) ---")
        for m in matches:
            # Only print styles containing layout properties
            if any(prop in m.lower() for prop in ["width", "height", "margin", "padding", "display", "flex", "grid", "gap"]):
                print(f"  {m}")
