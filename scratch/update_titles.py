import os

title_mapping = {
    "blog-architecture.html": "Modern Cloud Architecture Design | Growth School",
    "blog-cloud-comparison.html": "AWS vs Azure vs GCP: Cloud Comparison | Growth School",
    "blog-devops-sre.html": "DevOps vs SRE: Key Differences & Roles | Growth School",
    "blog-future-devops.html": "The Future of DevOps & Cloud Engineering | Growth School",
    "blog-kubernetes.html": "Kubernetes Deep Dive & Best Practices | Growth School",
    "blog-linux.html": "Linux Command Line Cheat Sheet & Guide | Growth School",
    "blog-playbook.html": "The DevOps Engineer's Playbook | Growth School",
    "blog-ports.html": "Common Networking Ports Every DevOps Engineer Must Know | Growth School",
    "blog-python.html": "Python for DevOps Automation | Growth School",
    "blog-realtime-interview.html": "Real-time DevOps & Cloud Interview Questions | Growth School",
    "course-aws.html": "AWS Cloud Architect Course | Growth School",
    "course-devops.html": "DevOps Masterclass Course | Growth School",
    "course-linux.html": "Linux Administration Course | Growth School",
}

base_dir = "d:/Pixalara Growth School/growth school repo"

for filename, new_title in title_mapping.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_title_tag = "<title>Growth School | DevOps & Cloud Training</title>"
    new_title_tag = f"<title>{new_title}</title>"
    
    if old_title_tag in content:
        content = content.replace(old_title_tag, new_title_tag)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename} -> {new_title}")
    else:
        print(f"Old title tag not found in {filename}")
