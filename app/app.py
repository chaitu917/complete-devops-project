from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Project</title>
    </head>
    <body>
        <h1>Welcome to My DevOps Project</h1>
        <h2>Application Version: 1.0</h2>

        <p>Server: Ubuntu Linux</p>
        <p>CI/CD: Jenkins</p>
        <p>Container: Docker</p>
        <p>Automation: Ansible</p>
        <p>Reverse Proxy: Nginx</p>

        <h3>Status: Application Running Successfully</h3>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
