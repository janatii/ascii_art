from flask import Flask, render_template, request, Response
from video_process import generate_stream

frontend_path = 'static'

app = Flask(__name__, template_folder=frontend_path)


@app.route('/')
def index():
    return render_template('template.html')

@app.route('/stream')
def stream():
    return Response(generate_stream(), content_type='text/event-stream')


if __name__ == "__main__":
    app.run()
