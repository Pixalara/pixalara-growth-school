import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

pattern = re.compile(
    r'(<a\s+href="https://dashboard\.growthschool\.cc/"\s+target="_blank"\s+class="nav-btn\s+btn-login">\s*Login\s*</a>\s*</li>\s*)(\n?\s*</ul>)',
    re.IGNORECASE
)

replacement = (
    r'\1'
    r'                    <li style="margin-left: 15px; display: flex; align-items: center;">\n'
    r'                        <button id="theme-toggle" class="theme-toggle-btn" aria-label="Toggle Theme" style="background: none; border: none; cursor: pointer; color: var(--text-dark); font-size: 1.2rem; transition: color 0.3s ease; display: flex; align-items: center; padding: 5px;">\n'
    r'                            <i class="fas fa-moon"></i>\n'
    r'                        </button>\n'
    r'                    </li>\n'
    r'                </ul>'
)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if theme toggle button is already injected
    if 'id="theme-toggle"' in content:
        continue

    new_content, num_subs = pattern.subn(replacement, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Injected theme toggle in: {filepath}")

print(f"Completed! Injected theme toggle button into {count} HTML files.")
