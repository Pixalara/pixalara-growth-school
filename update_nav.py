import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'(<li>\s*<a href="contact\.html">\s*CONTACT\s*</a>\s*</li>)'
    replacement = r'\1\n                    <li style="margin-left: 10px;">\n                        <a href="https://labs.growthschool.cc/" target="_blank" class="nav-btn btn-verify">Interactive Labs</a>\n                    </li>'
    
    new_content, num_subs = re.subn(pattern, replacement, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files in nav-links.")
