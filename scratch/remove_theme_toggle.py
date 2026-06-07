import glob

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

target_block = """                    <li style="margin-left: 15px; display: flex; align-items: center;">
                        <button id="theme-toggle" class="theme-toggle-btn" aria-label="Toggle Theme" style="background: none; border: none; cursor: pointer; color: var(--text-dark); font-size: 1.2rem; transition: color 0.3s ease; display: flex; align-items: center; padding: 5px;">
                            <i class="fas fa-moon"></i>
                        </button>
                    </li>\n"""

# Also handle potential alternative line endings (CRLF vs LF)
target_block_lf = target_block.replace('\r\n', '\n')
target_block_crlf = target_block.replace('\r\n', '\n').replace('\n', '\r\n')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    if target_block_lf in new_content:
        new_content = new_content.replace(target_block_lf, '')
    elif target_block_crlf in new_content:
        new_content = new_content.replace(target_block_crlf, '')
    else:
        # Fallback regex replace for flexibility
        import re
        pattern = re.compile(
            r'\s*<li[^>]*style="[^"]*margin-left:\s*15px[^"]*"[^>]*>\s*<button\s+id="theme-toggle".*?</button>\s*</li>\n?',
            re.DOTALL
        )
        new_content, num_subs = pattern.subn('', content)
        if num_subs == 0:
            continue
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    count += 1
    print(f"Removed theme toggle button from: {filepath}")

print(f"Completed! Removed theme toggle button from {count} HTML files.")
