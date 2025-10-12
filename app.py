from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jitendra Kumar Jat - DevOps</title>
        <style>
            body {{ 
                font-family: 'Arial', sans-serif; 
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                margin-bottom: 30px;
            }}
            .profile-section {{
                display: flex;
                gap: 30px;
                margin-bottom: 30px;
            }}
            .profile-card {{
                flex: 1;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }}
            .skills-section {{
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }}
            h1 {{ 
                color: #2c3e50; 
                margin-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
            .highlight {{
                color: #e74c3c;
                font-weight: bold;
            }}
            .success {{ 
                color: #27ae60; 
                font-size: 1.2em;
            }}
            .deployment-info {{
                background: #2ecc71;
                color: white;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }}
            .logo {{
                font-size: 2em;
                margin-bottom: 20px;
            }}
            .skill-item {{
                background: #ecf0f1;
                padding: 10px 15px;
                margin: 5px;
                border-radius: 20px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">🚀</div>
                <h1>Jitendra Kumar Jat</h1>
                <h2>DevOps Engineer</h2>
                <p class="success"><strong>Application Successfully Deployed via Jenkins CI/CD Pipeline</strong></p>
            </div>

            <div class="profile-section">
                <div class="profile-card">
                    <h2>👨‍💻 About Me</h2>
                    <p><strong>Name:</strong> Jitendra Kumar Jat</p>
                    <p><strong>Role:</strong> DevOps Engineer</p>
                    <p><strong>Experience:</strong> CI/CD, Cloud Infrastructure, Automation</p>
                    <p><strong>Passion:</strong> Building scalable and reliable systems</p>
                </div>
                
                <div class="profile-card">
                    <h2>🛠️ This Deployment</h2>
                    <p><strong>App Version:</strong> 2.0.0</p>
                    <p><strong>Deployed On:</strong> AWS EC2</p>
                    <p><strong>Deployment Time:</strong> {current_time}</p>
                    <p><strong>Status:</strong> <span class="highlight">✅ Active & Running</span></p>
                </div>
            </div>

            <div class="deployment-info">
                <h3>🎯 DevOps Pipeline Success</h3>
                <p>This application was automatically deployed using Jenkins 4-stage pipeline:</p>
                <p>GitHub → Jenkins → Docker → AWS EC2</p>
            </div>

            <div class="skills-section">
                <h2>💼 Technical Skills</h2>
                <div class="skill-item">Jenkins</div>
                <div class="skill-item">Docker</div>
                <div class="skill-item">AWS EC2</div>
                <div class="skill-item">CI/CD Pipelines</div>
                <div class="skill-item">Python</div>
                <div class="skill-item">Flask</div>
                <div class="skill-item">GitHub</div>
                <div class="skill-item">Linux</div>
                <div class="skill-item">Bash Scripting</div>
                <div class="skill-item">Infrastructure as Code</div>
            </div>

            <div class="profile-card">
                <h2>📞 Contact Info</h2>
                <p><strong>Email:</strong> jitendra.jat@example.com</p>
                <p><strong>GitHub:</strong> github.com/jitendrajat</p>
                <p><strong>Location:</strong> India</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {
        'status': 'healthy', 
        'service': 'flask-app',
        'maintained_by': 'Jitendra Kumar Jat',
        'role': 'DevOps Engineer'
    }

@app.route('/api/info')
def info():
    return {
        'app_name': 'Jitendra Jat - DevOps Portfolio',
        'version': '2.0.0',
        'developer': 'Jitendra Kumar Jat',
        'role': 'DevOps Engineer',
        'deployment_method': 'Jenkins CI/CD Pipeline',
        'infrastructure': 'AWS EC2 + Docker'
    }

@app.route('/api/skills')
def skills():
    return {
        'devops_skills': [
            'Jenkins CI/CD',
            'Docker Containerization',
            'AWS Cloud Services',
            'Infrastructure Automation',
            'Linux Administration',
            'Python Scripting',
            'Git Version Control',
            'Monitoring & Logging'
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)