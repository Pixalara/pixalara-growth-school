import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')

favicon_block = '''    <link rel="apple-touch-icon" sizes="180x180" href="assets/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16x16.png">'''

count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    # Remove existing favicon rules universally
    new_content = re.sub(r'\s*<link rel="incon".*?>', '', new_content) # safety
    new_content = re.sub(r'\s*<link [^>]*rel="icon"[^>]*>', '', new_content)
    new_content = re.sub(r'\s*<link [^>]*rel="shortcut icon"[^>]*>', '', new_content)
    new_content = re.sub(r'\s*<link [^>]*rel="apple-touch-icon"[^>]*>', '', new_content)
    
    # Also catch <link rel="icon" ...> which was already caught by [^>]*
    
    # Inject standard rules before </head>
    new_content = re.sub(r'(</head>)', '\n' + favicon_block + '\n\g<1>', new_content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files for unified favicons.")
