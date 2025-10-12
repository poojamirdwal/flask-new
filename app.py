from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins Demo App</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 40px;
                background-color: #f0f8ff;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 { color: #2c3e50; }
            .success { color: #27ae60; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Jenkins Pipeline Success!</h1>
            <p class="success"><strong>Application successfully deployed on EC2 via Jenkins</strong></p>
            <p><strong>Version:</strong> 1.0.0</p>
            <p><strong>Status:</strong> ✅ Running</p>
            <hr>
            <p>This is a simple Flask app deployed using Jenkins CI/CD pipeline</p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'flask-app'}

@app.route('/info')
def info():
    return {
        'app_name': 'Jenkins Demo App',
        'version': '1.0.0',
        'deployed_by': 'Jenkins Pipeline'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)