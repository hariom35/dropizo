from flask import Flask, render_template, request, send_from_directory
import yt_dlp
import os
from pytube import YouTube
import traceback

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Static Pages
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

# Download Logic
def download_video(video_url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print("Error in download_video:")
        traceback.print_exc()
        return None

# Form Submission Route
@app.route("/download", methods=["POST"])
def download():
    try:
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download("static/downloads")
        return render_template("success.html", title=yt.title)
    except Exception as e:
        print("Download error:", e)   # ← ye line ensure karo
        return render_template("error.html")



# Serve file download
@app.route('/download-file/<filename>')
def download_file(filename):
    file_path = os.path.join('downloads', filename)
    if os.path.exists(file_path):
        return send_from_directory('downloads', filename, as_attachment=True)
    else:
        return "File not found."

# Run Flask App
if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
