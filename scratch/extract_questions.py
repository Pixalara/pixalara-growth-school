import re
import json

content = open('blog-quize.html', encoding='utf-8').read()

# Let's extract question blocks
# Format: {id: 1, topic: 'Linux', q: '...', options: {A: '...', B: '...', C: '...', D: '...'}, correct: 'B', exp: '...'}
# Note: we can parse it using regex or eval since it is JS object notation. Let's write a parser.
pattern = r"\{\s*id:\s*(\d+),\s*topic:\s*'([^']+)'.*?\}"
matches = re.findall(pattern, content, re.DOTALL)
print(f"Total question matches found: {len(matches)}")

from collections import Counter
topics = [m[1] for m in matches]
print("Questions per topic:", Counter(topics))
