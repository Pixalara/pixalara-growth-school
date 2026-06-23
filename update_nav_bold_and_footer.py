import glob
import re

files = glob.glob('d:/Pixalara Growth School/growth school repo/*.html')
count_nav = 0
count_footer = 0

# 1. Pattern to make Interactive Labs bold in the nav bar
nav_pattern = r'class="nav-btn btn-verify">Interactive Labs</a>'
nav_replacement = 'class="nav-btn btn-verify" style="font-weight: 800;">Interactive Labs</a>'

# 2. Pattern to standardize footer Quick Links
footer_pattern = r'(<h4>Quick Links</h4>\s*<ul>)(.*?)(</ul>)'
footer_replacement = r'''\1
                    <li><a href="index.html">Home</a></li>
                    <li><a href="courses.html">Courses</a></li>
                    <li><a href="mentors.html">Mentors</a></li>
                    <li><a href="blogs.html">Blogs</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="https://labs.growthschool.cc/" target="_blank">Interactive Labs</a></li>
                    <li style="margin-top: 10px;">
                        <a href="https://careerhub.growthschool.cc/" target="_blank" style="color: var(--primary); font-weight: 700;">
                            Career Hub
                        </a>
                    </li>
                    <li>
                        <a href="https://resumeai.pixalara.io/" target="_blank" style="color: #1e88e5; font-weight: 700;">
                            ResumeAI
                        </a>
                    </li>
                    <li>
                        <a href="https://dashboard.growthschool.cc/" target="_blank" style="font-weight: 700;">
                            Student Login
                        </a>
                    </li>
                    <li><a href="verify.html" style="color: #4cd137;">Verify Certificate</a></li>
\3'''

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Nav
    new_content, nav_subs = re.subn(nav_pattern, nav_replacement, content)
    if nav_subs > 0:
        count_nav += 1
        
    # Update Footer (reorganize list items)
    new_content, footer_subs = re.subn(footer_pattern, footer_replacement, new_content, flags=re.DOTALL)
    if footer_subs > 0:
        count_footer += 1
        
    if nav_subs > 0 or footer_subs > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Bolded Nav Link in {count_nav} files.")
print(f"Reorganized Footer in {count_footer} files.")
