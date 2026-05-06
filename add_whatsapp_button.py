import os

directory = '.'
whatsapp_html = """
    <a href="https://wa.me/919988688654?text=Hello%20Growth%20School%20Team%2C%20I%20am%20interested%20in%20your%20courses." class="float-whatsapp" target="_blank">
        <i class="fab fa-whatsapp my-float"></i>
    </a>
"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'google89e154771df3f636.html':
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'class="float-whatsapp"' in content:
            continue
            
        # Insert before </body>
        if '</body>' in content:
            new_content = content.replace('</body>', whatsapp_html + '\n</body>')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Added WhatsApp button to {filename}")

print(f"Total files updated: {count}")
