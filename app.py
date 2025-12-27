from flask import Flask, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Python CI/CD Pipeline Demo</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 700px;
            width: 100%;
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .status {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }
        .info-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .label {
            font-weight: bold;
            color: #666;
            font-size: 0.9em;
            margin-bottom: 8px;
        }
        .value {
            color: #333;
            font-size: 1.1em;
        }
        .pipeline-info {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border-left: 4px solid #2196F3;
        }
        .pipeline-info h3 {
            color: #1976d2;
            margin-bottom: 15px;
        }
        .badge {
            display: inline-block;
            padding: 5px 12px;
            background: #667eea;
            color: white;
            border-radius: 20px;
            font-size: 0.85em;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Python CI/CD Pipeline</h1>
        <p class="subtitle">Deployed via AWS CodePipeline & CodeDeploy</p>
        
        <div class="status">
            ✅ Application Successfully Deployed!
        </div>
        
        <div class="info-grid">
            <div class="info-box">
                <div class="label">Python Version</div>
                <div class="value">{{ python_version }}</div>
            </div>
            
            <div class="info-box">
                <div class="label">Deployment Time</div>
                <div class="value">{{ current_time }}</div>
            </div>
            
            <div class="info-box">
                <div class="label">Server Hostname</div>
                <div class="value">{{ hostname }}</div>
            </div>
            
            <div class="info-box">
                <div class="label">Application Port</div>
                <div class="value">5000</div>
            </div>
        </div>
        
        <div class="pipeline-info">
            <h3>📦 CI/CD Pipeline Status</h3>
            <p><strong>Source:</strong> GitHub Repository</p>
            <p><strong>Pipeline:</strong> AWS CodePipeline</p>
            <p><strong>Deployment:</strong> AWS CodeDeploy</p>
            <p><strong>Target:</strong> AWS EC2 Instance</p>
            <span class="badge">Version 1.0</span>
            <span class="badge">Auto-Deploy Enabled</span>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    import sys
    import socket
    
    return render_template_string(
        HTML_TEMPLATE,
        python_version=sys.version.split()[0],
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        hostname=socket.gethostname()
    )

@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
