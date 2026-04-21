import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count = 0

replacement = r'''<div class="phone-input-wrapper">
                                <div class="phone-prefix">
                                    <img src="https://flagcdn.com/w20/in.png" alt="IN">
                                    <span>+91</span>
                                </div>
                                <input type="tel" name="\g<1>" class="form-control" pattern="[0-9]{10}" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '')" title="Please enter exactly 10 digits" required>
                            </div>'''

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<input\s+type="tel"\s+name="(phone|Phone)"\s+class="form-control"\s+required>', re.IGNORECASE)
    
    new_content, num_subs = pattern.subn(replacement, content)
    
    if num_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files containing phone input.")
