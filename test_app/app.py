from flask import Flask, render_template, Response
import time

app = Flask(__name__, template_folder='.')

def generate_stream():
    for i in range(1, 11):  # Generate 10 lines of text
        yield f"data: Line {i}\n\n"
        time.sleep(1)  # Simulate a delay (e.g., fetching data)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/stream')
def stream():
    return Response(generate_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
