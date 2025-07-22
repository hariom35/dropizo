from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    if not video_url:
        return "No URL provided", 400

    # Your download logic here (YouTube DL or pytube etc.)
    # For testing:
    print("URL received:", video_url)

    # Dummy response
    return f"You entered: {video_url}"

from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form.get('video_url')
    print("Got URL:", video_url)
    ...


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

