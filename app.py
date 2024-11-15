from flask import Flask, jsonify, render_template_string

app = Flask(__name__)


# Health Check route
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})


# Data route
@app.route("/data", methods=["GET"])
def get_data():
    data = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
        {"id": 4, "name": "Item 4"},
    ]
    return jsonify(data)


# Kubernetes route (something playful)
@app.route("/k8s", methods=["GET"])
def kubernetes_playful():
    message = "Welcome to the world of Docker!"
    return message


# Fancy new page route
@app.route("/fancy", methods=["GET"])
def fancy_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fancy Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 50px;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Fancy Page!</h1>
            <p>This is a simple example of a fancy page with some basic styling.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
