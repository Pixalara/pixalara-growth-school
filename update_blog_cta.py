import os
import re

cta_html = """<!-- START: Interactive Labs CTA -->
            <div class="labs-cta-card">
                <div class="labs-cta-content">
                    <span class="labs-cta-badge"><i class="fas fa-terminal"></i> Live Sandbox</span>
                    <h3 class="labs-cta-title">Don't Just Read. Code Live!</h3>
                    <p class="labs-cta-text">Practice what you just learned in our secure, zero-setup interactive labs. Boot up Linux containers, orchestrate AWS infrastructure, and run Docker right in your browser.</p>
                    <div class="labs-cta-features">
                        <span class="labs-cta-feature"><i class="fas fa-check-circle"></i> 100% Free & Interactive for Growth School Community</span>
                        <span class="labs-cta-feature"><i class="fas fa-check-circle"></i> No Setup Required</span>
                        <span class="labs-cta-feature"><i class="fas fa-check-circle"></i> Real-time Terminal Feedback</span>
                    </div>
                    <a href="https://labs.growthschool.cc/" target="_blank" class="labs-cta-btn">
                        Start Live Sandbox <i class="fas fa-arrow-right"></i>
                    </a>
                </div>
                <div class="labs-cta-visual">
                    <div class="terminal-mock">
                        <div class="terminal-mock-header">
                            <span class="dot red"></span>
                            <span class="dot yellow"></span>
                            <span class="dot green"></span>
                            <span class="terminal-mock-title">ubuntu@growthschool:~</span>
                        </div>
                        <div class="terminal-mock-body">
                            <p class="term-line cmd">docker run -d -p 80:80 nginx</p>
                            <p class="term-line output">Unable to find image 'nginx:latest' locally...</p>
                            <p class="term-line output">latest: Pulling from library/nginx</p>
                            <p class="term-line output">Digest: sha256:4c087b3289aa6b185...</p>
                            <p class="term-line output">Status: Downloaded newer image for nginx:latest</p>
                            <p class="term-line success"><i class="fas fa-check"></i> Container running at http://localhost:80</p>
                            <p class="term-line cursor">_</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- END: Interactive Labs CTA -->"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean existing block
    cleaned_content = re.sub(
        r'<!-- START: Interactive Labs CTA -->.*?<!-- END: Interactive Labs CTA -->\s*', 
        '', 
        content, 
        flags=re.DOTALL
    )

    # Insert CTA before <div class="blog-navigation">
    nav_pattern = r'(<div class="blog-navigation">)'
    if re.search(nav_pattern, cleaned_content):
        # We want to format it nicely with indentation matching the surrounding file structure
        new_content = re.sub(
            nav_pattern, 
            cta_html + '\n\n            \\1', 
            cleaned_content,
            count=1
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"Skipped {os.path.basename(filepath)} (no blog-navigation found)")

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(root_dir):
        if filename.startswith('blog-') and filename.endswith('.html') and filename != 'blog-quize.html':
            filepath = os.path.join(root_dir, filename)
            update_file(filepath)

if __name__ == '__main__':
    main()
