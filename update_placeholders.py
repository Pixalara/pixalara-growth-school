import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    # Remove placeholder="John Doe"
    new_content = re.sub(r'\s*placeholder="John Doe"', '', new_content)
    # Remove placeholder="john@example.com"
    new_content = re.sub(r'\s*placeholder="john@example\.com"', '', new_content)
    # Remove placeholder="+91 99999 99999"
    new_content = re.sub(r'\s*placeholder="\+91 99999 99999"', '', new_content)
    # Remove placeholder="dd-mm-yyyy"
    new_content = re.sub(r'\s*placeholder="dd-mm-yyyy"', '', new_content)
    # Remove placeholder="How can we help you?"
    new_content = re.sub(r'\s*placeholder="How can we help you\?"', '', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files removing placeholder details.")
