from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import pyqrcode
from pyqrcode import QRCode

app = Flask(__name__)
import os

DOWNLOAD_FOLDER = os.path.join(app.root_path, 'download')

@app.route("/", methods=["GET", "POST"])
def index():

        


    return render_template("input.html")

@app.route('/generateQR', methods=['POST'])
def show_qr_code():
    qr_data = request.form["qr_data"]

    # Check if it's a valid URL
    if not qr_data.startswith(('http://', 'https://')):
        return "Please enter a valid URL"

    # Generate QR Code
    qr = pyqrcode.create(qr_data)
    import os

    DOWNLOAD_FOLDER = os.path.join(app.root_path, 'download')
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    download_path = os.path.join(DOWNLOAD_FOLDER, 'download-qr.png')
    # Save QR Code
    qr.png(download_path, scale=6)
    return render_template('output.html', qr_filename='download-qr.png')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('download', filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
