from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    url = request.form["link"]
    img = qrcode.make(url)
    img_name = "qr.png"
    img.save(f"static/{img_name}")
    return render_template("index.html", url=url, img_name=img_name)
  else:
    return render_template("index.html")
  

@app.route("/download")
def download_file():
  path="static/qr.png"
  return send_file(path, as_attachment=True)

if __name__ == "__main__":
  app.run(debug=True)