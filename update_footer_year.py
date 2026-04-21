import glob

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('&copy; 2025', '&copy; 2026')
    new_content = new_content.replace('© 2025', '© 2026')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files containing the footer year.")
