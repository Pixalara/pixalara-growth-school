import re

content = open('blog-quize.html', encoding='utf-8').read()
topics = re.findall(r"topic:\s*'([^']+)'", content)
print("Topics:", set(topics))
