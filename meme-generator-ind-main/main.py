# Impor
from flask import Flask, render_template, request, send_from_directory

# task for x-axes position
app = Flask(__name__)

# Hasil formulir
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # mendapatkan gambar yang dipilih
        selected_image = request.form.get('image-selector')

        # Tugas #2. Menerima teks
        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')
        
        # Tugas #3. Menerima posisi teks
        textTop_y = request.form.get('textTop_y')
        textBottom_y = request.form.get('textBottom_y')
        # Tugas #3. Menerima warna teks
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # Menampilkan gambar yang dipilih
                               selected_image=selected_image, 

                               # Tugas #2. Menampilkan teks
                               textTop=textTop,                
                               textBottom=textBottom, 
                               # Tugas #3. Menampilkan warna
                               selected_color=selected_color,
                               # Tugas #3. Menampilkan posisi teks
                               textTop_y=textTop_y,
                               textBottom_y=textBottom_y
                               )
    else:
        # Menampilkan gambar pertama secara default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
