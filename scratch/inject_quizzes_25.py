import json
import os
import re

# Load the questions JSON
with open('scratch/questions.json', encoding='utf-8') as f:
    questions_data = json.load(f)['data']

# Define the 25 Monitoring & Observability questions
monitoring_questions = [
    {
        "q": "What are the three pillars of observability?",
        "options": {
            "A": "Metrics, Logs, and Traces",
            "B": "Servers, Networks, and Databases",
            "C": "Alerts, CPU, and RAM",
            "D": "Dashboards, Codes, and Pipelines"
        },
        "correct": "A",
        "exp": "The three pillars of observability are metrics (numeric telemetry), logs (event records), and traces (request journeys)."
    },
    {
        "q": "Which observability pillar represents numeric telemetry measured over time?",
        "options": {
            "A": "Logs",
            "B": "Traces",
            "C": "Metrics",
            "D": "Alerts"
        },
        "correct": "C",
        "exp": "Metrics are numeric values that track performance indicators like CPU usage, memory, and network throughput over time."
    },
    {
        "q": "Which tool is most commonly used to visualize Prometheus metrics in real-time graphs?",
        "options": {
            "A": "Grafana",
            "B": "Jaeger",
            "C": "Elasticsearch",
            "D": "Git"
        },
        "correct": "A",
        "exp": "Grafana is the industry-standard visualization tool that integrates with data sources like Prometheus to display dashboards."
    },
    {
        "q": "What is a 'Trace' in microservices monitoring?",
        "options": {
            "A": "A log file of database queries",
            "B": "A measurement of CPU heat",
            "C": "The end-to-end journey of a single request across multiple services",
            "D": "A list of open ports"
        },
        "correct": "C",
        "exp": "A trace tracks the path and timing of a single transaction/request as it propagates through a distributed system of microservices."
    },
    {
        "q": "Which tool is an open-source system monitoring and alerting toolkit that pulls/scrapes metrics?",
        "options": {
            "A": "Elasticsearch",
            "B": "Prometheus",
            "C": "Jenkins",
            "D": "Terraform"
        },
        "correct": "B",
        "exp": "Prometheus scrapes metric endpoints from systems and stores them in a time-series database."
    },
    {
        "q": "What is 'Alert Fatigue'?",
        "options": {
            "A": "When servers crash from too many alerts",
            "B": "When engineers ignore alerts because too many non-critical alarms are triggered",
            "C": "When monitoring tools run out of disk space",
            "D": "When a dashboard loads too slowly"
        },
        "correct": "B",
        "exp": "Alert fatigue occurs when users are overwhelmed by a high volume of frequent, low-priority alerts, leading to critical issues being missed."
    },
    {
        "q": "In HTTP status monitoring, which status code range represents server-side errors?",
        "options": {
            "A": "2xx",
            "B": "3xx",
            "C": "4xx",
            "D": "5xx"
        },
        "correct": "D",
        "exp": "5xx status codes (like 500 Internal Server Error, 502 Bad Gateway) represent errors on the server side."
    },
    {
        "q": "Which logging level is typically used for critical errors that cause application crashes?",
        "options": {
            "A": "DEBUG",
            "B": "INFO",
            "C": "FATAL / ERROR",
            "D": "WARN"
        },
        "correct": "C",
        "exp": "FATAL or ERROR logs indicate severe failures that disrupt normal application operations."
    },
    {
        "q": "What does APM stand for in observability?",
        "options": {
            "A": "Application Port Manager",
            "B": "Automated Process Monitor",
            "C": "Application Performance Monitoring",
            "D": "Advanced Pipeline Metrics"
        },
        "correct": "C",
        "exp": "APM stands for Application Performance Monitoring, which tracks transaction response times, code exceptions, and dependencies."
    },
    {
        "q": "Which tool is commonly used to collect and query application logs?",
        "options": {
            "A": "Jaeger",
            "B": "Elasticsearch / Loki",
            "C": "Prometheus",
            "D": "Webpack"
        },
        "correct": "B",
        "exp": "Elasticsearch and Loki are popular log aggregation engines used to search and index massive log files."
    },
    {
        "q": "What is the main difference between Monitoring and Observability?",
        "options": {
            "A": "Monitoring tells you when something is wrong; Observability helps you understand why",
            "B": "Monitoring is free; Observability is paid",
            "C": "Monitoring uses logs; Observability uses databases",
            "D": "There is no difference"
        },
        "correct": "A",
        "exp": "Monitoring tracks known failure modes ('is the system up?'), while Observability provides deep system insights to troubleshoot new or unknown problems."
    },
    {
        "q": "What does 'Scraping' mean in Prometheus?",
        "options": {
            "A": "Deleting old metrics",
            "B": "Extracting files from Docker",
            "C": "Fetching metrics from target HTTP endpoints periodically",
            "D": "Restaring crashed pods"
        },
        "correct": "C",
        "exp": "Prometheus gathers metrics by sending HTTP requests to configured target endpoints (scraping them)."
    },
    {
        "q": "Which of the following is an example of a 'Trace' visualization tool?",
        "options": {
            "A": "Jaeger",
            "B": "Ansible",
            "C": "Nginx",
            "D": "Docker Hub"
        },
        "correct": "A",
        "exp": "Jaeger is a popular open-source tool for distributed tracing, helping visualize the call graph of microservice requests."
    },
    {
        "q": "What does 'SLO' stand for in site reliability engineering?",
        "options": {
            "A": "Service Level Option",
            "B": "Service Level Objective",
            "C": "System Log Operator",
            "D": "Server Load Optimizer"
        },
        "correct": "B",
        "exp": "SLO stands for Service Level Objective, which is a target reliability level for a service (e.g., 99.9% uptime)."
    },
    {
        "q": "What metric measures the percentage of time a service is operational and reachable?",
        "options": {
            "A": "Latency",
            "B": "Throughput",
            "C": "Availability / Uptime",
            "D": "Saturation"
        },
        "correct": "C",
        "exp": "Availability (or uptime) tracks the percentage of time a system is fully functional and serving requests."
    },
    # 10 New Monitoring Questions
    {
        "q": "What is a 'SLA' in service agreements?",
        "options": {
            "A": "Service Level Agreement",
            "B": "Service Log Analyzer",
            "C": "System Load Alert",
            "D": "Scheduled Latency Assessment"
        },
        "correct": "A",
        "exp": "An SLA (Service Level Agreement) is a commitment between a service provider and a client regarding service reliability and performance, often with financial penalties if missed."
    },
    {
        "q": "What is 'PromQL'?",
        "options": {
            "A": "A programming language for Prometheus servers",
            "B": "A query language used to select and aggregate Prometheus time-series data",
            "C": "A protocol for sending logs",
            "D": "A database server"
        },
        "correct": "B",
        "exp": "PromQL (Prometheus Query Language) is the proprietary query language used to retrieve and process metrics data stored in Prometheus."
    },
    {
        "q": "What does 'Golden Signals' of monitoring typically include?",
        "options": {
            "A": "CPU, RAM, Disk, and Network",
            "B": "Latency, Traffic, Errors, and Saturation",
            "C": "Logs, Traces, Metrics, and Alarms",
            "D": "Users, Sales, Clicks, and Revenue"
        },
        "correct": "B",
        "exp": "Google SRE book defines the four Golden Signals of monitoring as Latency, Traffic, Errors, and Saturation."
    },
    {
        "q": "Which tool is commonly used to collect and route logs/metrics as a daemon (agent) on a host?",
        "options": {
            "A": "Fluentd / Promtail",
            "B": "Jenkins",
            "C": "Webpack",
            "D": "Git"
        },
        "correct": "A",
        "exp": "Fluentd, Fluent Bit, and Logstash/Promtail are log shippers or agents that run on hosts to collect and route logs."
    },
    {
        "q": "What is 'Synthetic Monitoring'?",
        "options": {
            "A": "Monitoring artificial intelligence systems",
            "B": "Simulating user transactions and paths periodically to test system availability",
            "C": "Viewing hardware telemetry",
            "D": "Disabling all alerts"
        },
        "correct": "B",
        "exp": "Synthetic monitoring uses simulated queries or user paths (pings, automated scripts) to proactively test if applications are reachable."
    },
    {
        "q": "What does 'Real User Monitoring' (RUM) track?",
        "options": {
            "A": "Telemetry from actual user interactions inside their web browsers",
            "B": "The CPU temp of the server",
            "C": "The count of servers running in AWS",
            "D": "The cost of cloud hosting"
        },
        "correct": "A",
        "exp": "RUM (Real User Monitoring) captures and analyzes every transaction of real users on a website or app, tracking client-side performance."
    },
    {
        "q": "In trace telemetry, what is a 'Span'?",
        "options": {
            "A": "The total memory of a container",
            "B": "A single unit of work (e.g., an individual database query or HTTP call) within a trace",
            "C": "The distance between server racks",
            "D": "A database table index"
        },
        "correct": "B",
        "exp": "A trace is made of multiple 'Spans'. Each span represents a single operation/unit of work with a start time, duration, and metadata."
    },
    {
        "q": "What is the standard format used by Prometheus to expose metric data?",
        "options": {
            "A": "XML",
            "B": "OpenTelemetry / Prometheus text-based line format",
            "C": "JSON",
            "D": "YAML"
        },
        "correct": "B",
        "exp": "Prometheus reads metrics exposed as plain text lines containing metric names, labels, and float64 values (OpenTelemetry standard)."
    },
    {
        "q": "Which alert severity level requires immediate intervention to prevent system downtime?",
        "options": {
            "A": "INFO",
            "B": "WARNING",
            "C": "CRITICAL / PAGER",
            "D": "NOTICE"
        },
        "correct": "C",
        "exp": "CRITICAL or PAGER alerts indicate severe failures (like a database crash) that require instant response from on-call engineers."
    },
    {
        "q": "What does 'System Saturation' measure?",
        "options": {
            "A": "The humidity in the server room",
            "B": "How full your system resources are (e.g., CPU queue length, disk capacity)",
            "C": "The number of active git branches",
            "D": "The security strength of passwords"
        },
        "correct": "B",
        "exp": "Saturation measures how close a resource is to being full or overloaded (e.g., memory limits or disk utilization)."
    }
]

# Map files to topics
file_mappings = {
    "blog-aws-essentials.html": "AWS",
    "blog-linux-basics.html": "Linux",
    "blog-git-basics.html": "Git",
    "blog-docker-beginner.html": "Docker",
    "blog-kubernetes-intro.html": "Kubernetes",
    "blog-terraform-basics.html": "Terraform",
    "blog-cicd-mastery.html": "GitHub CI/CD",
    "blog-monitoring-observability.html": "Monitoring"
}

# Generate quiz HTML for a list of questions
def generate_quiz_html(questions):
    html = """
            <!-- Test Your Knowledge Quiz Section -->
            <section class="quiz-section" style="margin-top: 50px; padding-top: 40px; border-top: 2px solid #eee;">
                <h2 style="font-size: 1.8rem; color: var(--text-dark); margin-bottom: 20px;">
                    <i class="fas fa-question-circle" style="color: var(--primary); margin-right: 10px;"></i>Test Your Knowledge
                </h2>
                <p style="color: #666; margin-bottom: 30px;">
                    Answer these 25 questions to check your understanding of this module. Click on an option to reveal the correct answer instantly.
                </p>
                
                <style>
                    .quiz-section {
                        margin-top: 40px;
                    }
                    .quiz-q-card {
                        background: #fff;
                        border: 1px solid #eee;
                        border-radius: 12px;
                        padding: 25px;
                        margin-bottom: 25px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
                        transition: transform 0.3s ease, box-shadow 0.3s ease;
                    }
                    .quiz-q-card:hover {
                        transform: translateY(-2px);
                        box-shadow: 0 8px 25px rgba(101, 40, 247, 0.05);
                    }
                    .quiz-q-num {
                        font-size: 0.85rem;
                        color: var(--primary);
                        font-weight: 700;
                        text-transform: uppercase;
                        margin-bottom: 8px;
                        letter-spacing: 0.5px;
                    }
                    .quiz-q-text {
                        font-size: 1.2rem;
                        color: var(--text-dark);
                        font-weight: 700;
                        margin-bottom: 20px;
                        line-height: 1.4;
                    }
                    .quiz-options {
                        display: flex;
                        flex-direction: column;
                        gap: 12px;
                    }
                    .quiz-option {
                        padding: 14px 20px;
                        border: 2px solid #f0f0f0;
                        border-radius: 8px;
                        cursor: pointer;
                        transition: all 0.2s ease;
                        font-size: 0.95rem;
                        font-weight: 600;
                        color: #444;
                        display: flex;
                        align-items: center;
                    }
                    .quiz-option:hover {
                        border-color: #dcd6f7;
                        background: #f9f9ff;
                    }
                    .quiz-option.correct {
                        border-color: #28a745 !important;
                        background-color: #d4edda !important;
                        color: #155724 !important;
                    }
                    .quiz-option.incorrect {
                        border-color: #dc3545 !important;
                        background-color: #f8d7da !important;
                        color: #721c24 !important;
                    }
                    .quiz-explanation {
                        margin-top: 20px;
                        padding: 15px 20px;
                        background: #f8f9ff;
                        border-left: 4px solid var(--primary);
                        border-radius: 4px;
                        display: none;
                        font-size: 0.95rem;
                        line-height: 1.6;
                        color: #555;
                        animation: fadeIn 0.4s ease;
                    }
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(5px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                </style>
                
                <div class="quiz-questions-list">
"""

    for i, q in enumerate(questions):
        html += f"""
                    <!-- Question {i+1} -->
                    <div class="quiz-q-card">
                        <div class="quiz-q-num">Question {i+1} of 25</div>
                        <div class="quiz-q-text">{q['q']}</div>
                        <div class="quiz-options">
"""
        for opt_key in sorted(q['options'].keys()):
            opt_val = q['options'][opt_key]
            is_correct = "true" if opt_key == q['correct'] else "false"
            opt_val_escaped = opt_val.replace("'", "&#39;")
            html += f"""                            <div class="quiz-option" data-correct="{is_correct}" onclick="checkQuizAnswer(this)">{opt_key}. {opt_val_escaped}</div>\n"""
        
        exp_escaped = q['exp'].replace("'", "&#39;")
        html += f"""                        </div>
                        <div class="quiz-explanation">
                            <strong>Explanation:</strong> {exp_escaped}
                        </div>
                    </div>
"""

    html += """                </div>
            </section>

            <script>
            function checkQuizAnswer(selectedOption) {
                const parentOptions = selectedOption.parentElement;
                if (parentOptions.classList.contains('answered')) return;
                
                parentOptions.classList.add('answered');
                const options = parentOptions.querySelectorAll('.quiz-option');
                const card = parentOptions.closest('.quiz-q-card');
                const explanation = card.querySelector('.quiz-explanation');
                
                options.forEach(opt => {
                    opt.style.pointerEvents = 'none';
                    if (opt.getAttribute('data-correct') === 'true') {
                        opt.classList.add('correct');
                    }
                });
                
                if (selectedOption.getAttribute('data-correct') === 'false') {
                    selectedOption.classList.add('incorrect');
                }
                
                if (explanation) {
                    explanation.style.display = 'block';
                }
            }
            </script>
"""
    return html

# Process each file
for filename, topic in file_mappings.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename}: file not found.")
        continue

    print(f"Processing {filename} (Topic: {topic})...")
    
    # Get the 25 questions
    if topic == "Monitoring":
        topic_qs = monitoring_questions
    else:
        topic_qs = [q for q in questions_data if q['topic'] == topic][:25]

    if len(topic_qs) < 25:
        print(f"Warning: Only found {len(topic_qs)} questions for topic {topic}!")
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # Generate quiz HTML
    quiz_html = generate_quiz_html(topic_qs)
    
    # Replace pattern
    match = re.search(r'</div>\s*<div class="blog-navigation">', file_content)
    if not match:
        match = re.search(r'</div>\s*</article>', file_content)
        
    if match:
        matched_str = match.group(0)
        replacement = f"</div>\n{quiz_html}\n<div class=\"blog-navigation\">"
        new_content = file_content.replace(matched_str, replacement)
        
        # Save back the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully injected 25-question quiz into {filename}!")
    else:
        print(f"ERROR: Could not find target insertion point in {filename}!")

print("All done!")
