import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

pattern = re.compile(r'<div\s+class="blog-meta">([\s\S]*?)</div>')

replacement = (
    r'<div class="blog-meta" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">\n'
    r'                    \1\n'
    r'                    <button id="blog-night-mode" class="blog-night-btn" style="background: var(--primary); color: #fff; border: none; padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 6px; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(101, 40, 247, 0.15);">\n'
    r'                        <i class="fas fa-moon"></i> <span>Night Read Mode</span>\n'
    r'                    </button>\n'
    r'                </div>'
)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only update actual blog pages (contain class="blog-meta")
    if 'class="blog-meta"' not in content or 'id="blog-night-mode"' in content:
        continue

    new_content, num_subs = pattern.subn(replacement, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Added Night Mode button to: {filepath}")

print(f"Completed! Added Night Mode button to {count} blog files.")
