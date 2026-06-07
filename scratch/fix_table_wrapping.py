import os
import re

workspace_dir = "d:\\Pixalara Growth School\\growth school repo"

# 1. Fix blog-architecture.html
arch_path = os.path.join(workspace_dir, "blog-architecture.html")
with open(arch_path, 'r', encoding='utf-8') as f:
    arch_content = f.read()

# Replace table with wrapped table and min-width
old_table = '<table style="width:100%; border-collapse: collapse; margin-top: 20px; font-size: 0.9rem;">'
new_table = '<div class="table-wrapper">\n                <table style="width:100%; border-collapse: collapse; margin-top: 20px; font-size: 0.9rem; min-width: 600px;">'

if old_table in arch_content:
    arch_content = arch_content.replace(old_table, new_table)
    # Find matching </table> and append </div>
    table_end = '</table>'
    # We want to replace the first instance after the new table starts
    start_idx = arch_content.find(new_table)
    end_idx = arch_content.find(table_end, start_idx)
    if end_idx != -1:
        arch_content = arch_content[:end_idx + len(table_end)] + '\n                </div>' + arch_content[end_idx + len(table_end):]
        with open(arch_path, 'w', encoding='utf-8') as f:
            f.write(arch_content)
        print("Successfully updated blog-architecture.html table wrapping!")
else:
    print("Could not find table in blog-architecture.html or already updated.")


# 2. Fix blog-playbook.html
playbook_path = os.path.join(workspace_dir, "blog-playbook.html")
with open(playbook_path, 'r', encoding='utf-8') as f:
    playbook_content = f.read()

# Add min-width: 600px; to CSS .cmd-table
old_css_part = """        .cmd-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0 40px 0;
            font-size: 0.95rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border-radius: 8px;
            overflow: hidden;
        }"""

new_css_part = """        .cmd-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0 40px 0;
            font-size: 0.95rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border-radius: 8px;
            overflow: hidden;
            min-width: 600px;
        }"""

if old_css_part in playbook_content:
    playbook_content = playbook_content.replace(old_css_part, new_css_part)
    print("Updated .cmd-table CSS in blog-playbook.html")
else:
    # check if already has min-width
    if "min-width: 600px;" in playbook_content:
        print("CSS already has min-width: 600px; in blog-playbook.html")
    else:
        print("WARNING: Could not find .cmd-table CSS pattern in blog-playbook.html")

# Now wrap all <table class="cmd-table"> ... </table> in <div class="table-wrapper">...</div>
# We can do this using a regex find and replace
table_pattern = re.compile(r'(<table class="cmd-table">.*?</table>)', re.DOTALL)
wrapped_count = 0

def wrap_table(match):
    global wrapped_count
    wrapped_count += 1
    return f'<div class="table-wrapper">\n                {match.group(1)}\n            </div>'

# Only do it if not already wrapped
if '<div class="table-wrapper">\n                <table class="cmd-table">' not in playbook_content:
    playbook_content = table_pattern.sub(wrap_table, playbook_content)
    with open(playbook_path, 'w', encoding='utf-8') as f:
        f.write(playbook_content)
    print(f"Successfully wrapped {wrapped_count} tables in blog-playbook.html!")
else:
    print("Tables in blog-playbook.html appear to be already wrapped.")
