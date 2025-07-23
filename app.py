from flask import Flask, render_template, request, send_file
import yt_dlp
import os

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
        print(f"Error in download_video: {e}")
        return None

# Download Route
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    file_path = download_video(video_url)

    from flask import send_from_directory

    if file_path and os.path.exists(file_path):
        return render_template('success.html', filename=os.path.basename(file_path))
    else:
        return render_template('error.html', message="Could not download the video. Try a different link.")


# Run Flask
if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
