from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if not url:
        return "No URL provided", 400

    qr = qrcode.make(url)
    qr_io = BytesIO()
    qr.save(qr_io, 'PNG')
    qr_io.seek(0)

    return send_file(qr_io, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    app.run(debug=True)
