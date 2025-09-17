# 📥 utube_downloader Downloader

A lightweight, Python-based media downloader built on [yt-dlp](https://github.com/yt-dlp/yt-dlp).
This project makes it simple to fetch videos, audio, and playlists from YouTube and other supported platforms.

---

## 🚀 Features

* Download videos or extract audio with a single command
* Playlist support (batch downloads)
* Custom output file naming
* Cross-platform (Linux, macOS, Windows)
* Leverages the full power of **yt-dlp**

---

## 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/n-cognto/utube_downloader.git
   cd utube_downloader
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠 Usage

### Download a Video

```bash
python utube_downloader.py <video_url>
```

### Download Audio Only (MP3)

```bash
python utube_downloader.py <video_url> --audio
```

### Download Playlist

```bash
python utube_downloader.py <playlist_url> --playlist
```

### Custom Output Name

```bash
python utube_downloader.py <video_url> -o "myvideo.mp4"
```

---

## 📂 Project Structure

```
yt-dlp-downloader/
│── utube_downloader.py        # Main script
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---

## ⚖️ Disclaimer

This project is for **educational and personal use only**.
Ensure you comply with the **terms of service** of the platforms you use it on.
The maintainers are not responsible for misuse.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a PR.

---

## ⭐ Support

If you find this useful, give the repo a ⭐ on GitHub — it helps a lot!
