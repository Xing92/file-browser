from flask import Flask, render_template, request, send_from_directory
from file_browser import *
import os

app = Flask (__name__)
basedir = "/repo/xing/"
@app.route("/browser")
def page_browser():
    directory = request.args.get("directory", default="", type=str)
    content = getDirectoryContent(basedir + str(directory))
    return content

@app.route("/temp")
@app.route("/temp/")
def page_browser_temp():
    directory = request.args.get("directory", default="", type=str)

    if directory.endswith('png') :
        print("it's a photo!")
        return render_template("browser_image.html", image=basedir + directory)

    content = getDirectoryContent(basedir + directory)
    return render_template("browser_main.html", content=content, directory=directory) 
@app.route("/lena")
def page_lena():
    return render_template("lena.html")

#@app.route("/")
@app.route("/home")
def page_home():
    return "<p>Home Page</p>"

@app.route("/hello/<name>")
def page_hello(name):
    return f"Hello, {name}"

@app.route("/uploads/<path:name>")
def download_file(name):
    print("XINGA!")
    print(app.config['APPLICATION_ROOT'])
    return send_from_directory(app.config['UPLOAD_FOLDER'], name, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9090))
    app.run(debug=True, host='0.0.0.0', port=port)
#    app.run(debug=True, port=port)
