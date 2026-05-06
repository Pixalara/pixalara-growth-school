import os

directory = '.'
old_number = '+91 99886 88654'
new_number_link = '<a href="tel:+919988688654" style="color: inherit; text-decoration: none;">+91 99886 88654</a>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated (basic check)
        if 'tel:+919988688654' in content:
            continue
            
        new_content = content.replace(old_number, new_number_link)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
