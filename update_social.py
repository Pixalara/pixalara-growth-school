import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

pattern = re.compile(r'(<div class="social-links"[^>]*>).*?(</div>)', re.DOTALL)

replacement = r'''\1
                    <a href="https://www.instagram.com/growthschool.cc/" target="_blank"><i
                            class="fab fa-instagram"></i></a>
                \2'''

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, num_subs = pattern.subn(replacement, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files containing social links.")
