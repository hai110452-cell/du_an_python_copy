import requests

url = "https://webmusic-3ssu.onrender.com/api/music/upload/"

data = {
    "title": "test",
    "content": "abc"
}

files = {
    "image": open("a.jpg", "rb"),
    "audio": open("a.mp3", "rb")
}

res = requests.post(url, data=data, files=files)
print(res.json())