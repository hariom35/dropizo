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
def download_video():
    try:
        video_url = request.form['video_url']
        if not video_url:
            return "URL is required!", 400

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        return render_template('success.html')
    
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
