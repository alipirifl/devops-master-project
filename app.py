from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 DevOps Master Project - Home Page"

@app.route('/devops')
def devops():
    return "📚 Learning: Docker, CI/CD, Cloud, Kubernetes"

@app.route('/status')
def status():
    return "✅ System Status: All Services Running"

@app.route('/api/info')
def api_info():
    return {
        "project": "DevOps Master",
        "version": "1.0",
        "technologies": ["Docker", "CI/CD", "Python", "Flask"]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)