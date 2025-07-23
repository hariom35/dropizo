from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Other static pages
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

# YouTube download logic
@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['video_url']
    if not video_url:
        return "URL is required!", 400

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info)

     # After download, render success page
    return render_template('success.html')

if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    app.run(debug=True)

