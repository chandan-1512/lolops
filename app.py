from flask import Flask, send_file, jsonify
import pyjokes

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_file("index.html")
@app.route('/index.css')
def serve_css():
    return send_file("index.css")

@app.route('/emobg.webp')
def serve_container_bg():
    return send_file("emobg.webp")
@app.route('/5335982.jpg')
def serve_body_bg():
    return send_file("5335982.jpg")

@app.route('/get-joke')
def get_joke():
    joke = pyjokes.get_joke()
    return jsonify(joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
