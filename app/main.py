from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Medium ilk yazım için oluşturuldu...</h1>"
